r"""This parses Python code that contains variable assignments.

It uses the Python tokenizer, but doesn't execute any code.  It only
accepts variable assignments, with values that are strings, numbers,
or the special values True, False, and None.

Currently lists, tuples, dictionaries, and class definitions are not
supported.  All of these could be if there was a desire (the tokenize
module that this is based upon doesn't care about structure).

Double assignments (like ``a = b = None``) are not allowed.

The primary method is ``parse_assignments(source)``, which you can use
like::

    >>> vars = parse_assignments('''# this is a python-like file
    ... smtp_server = "localhost"
    ... smtp_port = 443
    ... smtp_use_tls = False
    ... # No username or password:
    ... smtp_username = None
    ... smtp_password = None
    ... message_template = \'\'\'This is a template for the message
    ... that goes over multiple lines\
    ... with a continuation\'\'\'
    ... ''')
    >>> for name, value in vars:
    ...     print '%s=%r' % (name, value)
    smtp_server='localhost'
    smtp_port=443
    smtp_use_tls=False
    smtp_username=None
    smtp_password=None
    message_template='This is a template for the message\nthat goes over multiple lineswith a continuation'
"""

import tokenize
from cStringIO import StringIO

class ParserSyntaxError(SyntaxError):
    """
    Raised when there is a syntax error with the form of the file,
    including statements that are outside the limited scope of things
    that this will parse.
    """
    def __init__(self, message, start, end):
        SyntaxError.__init__(self, message)
        self.message = message
        self.start = start
        self.end = end
    def __str__(self):
        return '%s at line %s' % (self.message, self.start[0])

def parse_assignments(source):
    tokens = tokenize.generate_tokens(StringIO(source).readline)
    assignments = []
    state = 'need_variable'
    variable_name = None
    for token_type, token_string, start, end, line in tokens:
        if token_type == tokenize.NL:
            if state == 'need_variable':
                continue
            raise ParserSyntaxError("Newline not expected", start, end)
        if token_type == tokenize.COMMENT:
            continue
        if token_type == tokenize.ENDMARKER:
            break
        if (state == 'need_value' and token_type == tokenize.NAME
            and token_string in ('True', 'False', 'None')):
            token_type = 'SPECIAL_VALUE'
        if token_type == tokenize.NAME:
            if state != 'need_variable':
                raise ParserSyntaxError("Variable not expected (got %s)" % token_string,
                                        start, end)
            variable_name = token_string
            state = 'need_assignment'
        if token_type == tokenize.OP:
            if token_string != '=':
                raise ParserSyntaxError("Only assignments are allowed (got operator %s)" % token_string,
                                        start, end)
            if state != 'need_assignment':
                raise ParserSyntaxError("Assignment not expected", start, end)
            state = 'need_value'
        if token_type in (tokenize.STRING, tokenize.NUMBER, 'SPECIAL_VALUE'):
            if token_type == 'SPECIAL_VALUE':
                if token_string == 'True':
                    value = True
                elif token_string == 'False':
                    value = False
                elif token_string == 'None':
                    value = None
                else:
                    assert 0, 'Unknown value: %r' % token_string
            elif token_type == tokenize.STRING:
                value = parse_string(token_string, start, end)
            elif token_type == tokenize.NUMBER:
                if '.' in token_string or 'e' in token_string:
                    value = float(token_string)
                elif token_string.startswith('0x'):
                    value = int(token_string[2:], 16)
                elif token_string.startswith('0b'):
                    value = int(token_string[2:], 2)
                elif token_string.startswith('0o'):
                    value = int(token_string[2:], 8)
                elif token_string.startswith('0'):
                    value = int(token_string, 8)
                else:
                    value = int(token_string)
            else:
                raise ParserSyntaxError("Unknown value type: %s" % token_string, start, end)
            if not state == 'need_value':
                raise ParserSyntaxError("Value not expected (got value %s)" % token_string, start, end)
            assert variable_name
            assignments.append((variable_name, value))
            variable_name = None
            state = 'need_variable'
    if state != 'need_variable':
        raise ParserSyntaxError("Unfinished assignment (of variable %s)" % variable_name, start, end)
    return assignments

def parse_string(s, start, end):
    """
    Parses a string literal to its true form
    """
    unquote = True
    unicode = False
    if s.startswith('u'):
        s = s[1:]
        unicode = True
    if s.startswith('"""') or s.startswith("'''"):
        s = s[3:-3]
    elif s.startswith("'") or s.startswith('"'):
        s = s[1:-1]
    elif s.startswith('r"""') or s.startswith("r'''"):
        s = s[4:-3]
        unquote = False
    elif s.startswith('r"') or s.startswith("r'"):
        s = s[2:-1]
        unquote = False
    else:
        raise ParserSyntaxError("Unknown string format: %s" % s, start, end)
    if unquote:
        s = s.decode('string_escape')
    if unicode:
        ## FIXME: what encoding would it be?
        s = s.decode('unicode_escape')
    return s

if __name__ == '__main__':
    import doctest
    doctest.testmod()

