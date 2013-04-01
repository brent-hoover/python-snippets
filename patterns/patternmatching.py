"""
Erlang-style pattern matching.  This defines a decorator ``Inbox``
which turns a function into an inbox that accepts messages (through
calling) and dispatches to an implementation.

Examples::

    >>> @Inbox
    ... def process(*args, **kw):
    ...     raise NotImplementedError('Nothing matched')

This defines our inbox, ``process``.  This is the default
implementation; in our case we raise NotImplementedError because we
want every case to match.  We'll make an implementation::

    >>> @process.match('request', {'type': 'email', 'to': var.to, 'from': var.from_, '_': any})
    ... def process_request(to, from_):
    ...     print 'Request from:%s to:%s' % (from_, to)
    >>> @process.match('request', {'type': 'http', 'host': var.host, 'path': var.path, '_': any})
    ... def process_http(host, path):
    ...     print 'Request for http://%s%s' % (host, path)
    >>> @process.match([any(var.requests)])
    ... def process_many(requests):
    ...     for req in requests:
    ...         process('request', req)

Now to use them::

    >>> process('request', dict(type='http', host='localhost', path='/foo', remote_addr='127.0.0.1'))
    Request for http://localhost/foo
    >>> process([dict(type='http', host='127.0.0.1', path='/'),
    ...          {'type': 'email', 'to': 'bob@example.com', 'from': 'joe@example.com'}])
    Request for http://127.0.0.1/
    Request from:joe@example.com to:bob@example.com

    >>> print process.explain('request', dict(type='http', host='localhost', path='/foo', remote_addr='127.0.0.1'))
    Failed <Implementation for <Inbox for process>: process_request>:
      Doesn't match; 'http'!='email'
    Succeeded <Implementation for <Inbox for process>: process_http>
      arguments: (host='localhost', path='/foo')
    Failed <Implementation for <Inbox for process>: process_many>:
      Wrong length (2>1 in ([patmatch.any(patmatch.var.requests)],))
    >>> print process.explain([dict(type='http', host='127.0.0.1', path='/'),
    ...          {'type': 'email', 'to': 'bob@example.com', 'from': 'joe@example.com'}])
    Failed <Implementation for <Inbox for process>: process_request>:
      Doesn't match; [{'path': '/', 'host': '127.0.0.1', 'type': 'http'}, {'to': 'bob@example.com', 'type': 'email', 'from': 'joe@example.com'}]!='request'
    Failed <Implementation for <Inbox for process>: process_http>:
      Doesn't match; [{'path': '/', 'host': '127.0.0.1', 'type': 'http'}, {'to': 'bob@example.com', 'type': 'email', 'from': 'joe@example.com'}]!='request'
    Succeeded <Implementation for <Inbox for process>: process_many>
      arguments: (requests=[{'path': '/', 'host': '127.0.0.1', 'type': 'http'}, {'to': 'bob@example.com', 'type': 'email', 'from': 'joe@example.com'}])


"""

class Inbox(object):

    def __init__(self, func):
        self.func = func
        self.name = self.func.func_name
        self.module = self.func.func_globals.get('__name__')
        self.implementations = []

    def __repr__(self):
        return '<%s for %s>' % (
            self.__class__.__name__,
            self.func.func_name)

    def __call__(self, *args, **kw):
        possible = []
        for impl in self.implementations:
            try:
                matching = impl.match_call(*args, **kw)
            except Failure:
                pass
            else:
                possible.append((impl, matching))
        if not possible:
            return self.func(*args, **kw)
        if len(possible) > 1:
            raise TypeError(
                "Multiple implementations match the signature (%s): %s"
                % (format_args(*args, **kw), ', '.join(map, [repr(f) for f, m in possible])))
        impl, match = possible[0]
        return impl(*match[0], **match[1])

    def explain(self, *args, **kw):
        results = []
        any_match = False
        for impl in self.implementations:
            try:
                matching = impl.match_call(*args, **kw)
            except Failure, e:
                results.append('Failed %r:\n  %s' % (impl, e))
            else:
                any_match = True
                results.append('Succeeded %r\n  arguments: (%s)' % (impl, format_args(*matching[0], **matching[1])))
        if not any_match:
            results.append('Default implementation will be used')
        return '\n'.join(results)

    def match(self, *match_args, **match_kw):
        def decorate(func):
            self.implementations.append(Implementation(self, func, match_args, match_kw))
            prev = func.func_globals.get(func.func_name)
            if prev is not None:
                return prev
            return func
        return decorate

def format_args(*args, **kw):
    parts = [repr(v) for v in args]
    parts.extend([
        '%s=%r' % (n, v) for n, v in sorted(kw.items())])
    return ', '.join(parts)

class Implementation(object):

    def __init__(self, inbox, func, match_args, match_kw):
        self.inbox = inbox
        self.func = func
        self.match_args = match_args
        self.match_kw = match_kw

    def __repr__(self):
        return '<%s for %r: %s>' % (
            self.__class__.__name__,
            self.inbox,
            self.func.func_name)

    def match_call(self, *args, **kw):
        bindings = {}
        bindings.update(match_list(args, self.match_args))
        bindings.update(match_dict(kw, self.match_kw))
        return ((), bindings)

    def __call__(self, *args, **kw):
        return self.func(*args, **kw)

def match_obj(arg, match):
    if isinstance(match, (list, tuple)):
        return match_list(arg, match)
    elif isinstance(match, dict):
        return match_dict(arg, match)
    elif hasattr(match, '__match__'):
        return match.__match__(arg)
    elif match == arg:
        return {}
    else:
        raise Failure("Doesn't match; %r!=%r", arg, match)

def match_list(arg, match):
    if (isinstance(arg, dict)
        or hasattr(arg, 'items')):
        raise Failure('Dict-like object, not list-like object: %r (for %r)', arg, match)
    if not isinstance(arg, (list, tuple)):
        try:
            iterator = iter(arg)
            if iterator is arg:
                raise Failure('Cannot use iterators, only iterables (%r)', arg)
            arg = list(iterator)
        except (TypeError, AttributeError), e:
            raise Failure('Expected a sequence (%r)', e)
    elif not arg and not match:
        return {}
    if match and getattr(match[-1], '__any__', False):
        any = match[-1]
        match = match[:-1]
    else:
        any = None
    if any is None and len(arg) > len(match):
        raise Failure('Wrong length (%r>%r in %r)', len(arg), len(match), match)
    if len(arg) < len(match):
        arg = list(arg)
        arg.extend([Nil]*(len(match)-len(arg)))
    bindings = {}
    for arg_item, match_item in zip(arg, match):
        bindings.update(match_obj(arg_item, match_item))
    if any is not None:
        bindings.update(match_obj(arg[len(match):], any))
    return bindings

def match_dict(arg, match):
    if not isinstance(arg, dict):
        try:
            ## FIXME: could consume iterator
            arg = dict(arg)
        except (TypeError, ValueError):
            raise Failure('Expected a dict-like object (got %r)', arg)
    else:
        if not arg and not match:
            return {}
        arg = arg.copy()
    if '_' in match and getattr(match['_'], '__any__', False):
        any = match['_']
    else:
        any = None
    extra_args = {}
    for name in arg.keys():
        if name not in match:
            if any is None:
                raise Failure('Unexpected key: %s (for %r)', name, match)
            extra_args[name] = arg.pop(name)
    bindings = {}
    for name in match:
        if any is not None and name == '_':
            continue
        bindings.update(match_obj(arg.get(name, Nil), match[name]))
    if any is not None and extra_args:
        bindings.update(match_obj(extra_args, any))
    return bindings

class Failure(Exception):
    """
    Raised for a failed match
    """

    def __str__(self):
        msg = self.args[0]
        args = self.args[1:]
        if args:
            msg = msg % args
        return msg

class NilType(object):
    Nil = None
    def __init__(self):
        if self.Nil is not None:
            raise TypeError("Can only be instantiated once")
    def __repr__(self):
        return 'Nil'
    def __nonzero__(self):
        return False
    def __match__(self, arg):
        return {}
Nil = NilType()
NilType.Nil = Nil
del NilType

class VarType(object):
    def __getattr__(self, attr):
        if attr.startswith('_'):
            raise AttributeError("Invalid name: %r" % attr)
        return Variable(attr)
    def __repr__(self):
        return 'patmatch.var'
var = VarType()
del VarType

class Variable(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'patmatch.var.%s' % self.name
    def __str__(self):
        return self.name
    def __match__(self, arg):
        return {self.name: arg}

class AnyType(object):
    __any__ = True
    def __match__(self, arg):
        return {}
    def __repr__(self):
        return 'patmatch.any'
    def __call__(self, matcher):
        return AnyMatch(matcher)
any = AnyType()
del AnyType

class AnyMatch(object):
    __any__ = True
    def __init__(self, matcher):
        self.matcher = matcher
    def __match__(self, arg):
        return match_obj(arg, self.matcher)
    def __repr__(self):
        return 'patmatch.any(%r)' % (self.matcher)

class Instance(object):
    def __init__(self, klass, matcher=any):
        self.klass = klass
        self.matcher = matcher
    def __match__(self, arg):
        if not isinstance(arg, self.klass):
            raise Failure('%r not an instance of %s', arg, self.klass)
        return match_obj(arg, self.matcher)

class Condition(object):
    def __init__(self, func, matcher=any):
        self.func = func
        self.matcher = matcher
    def __match__(self, arg):
        if self.func(arg):
            return match_obj(arg, self.matcher)
        raise Failure('%r fails condition', arg)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

