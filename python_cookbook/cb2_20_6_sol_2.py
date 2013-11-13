def tracing_processor(original_callable, *args, **kwargs):
    r_name = getattr(original_callable, '__name__', '<unknown>')
    r_args = map(repr, args)
    r_args.extend(['%s=%r' % x for x in kwargs.iteritems()])
    print "begin call to %s(%s)" % (r_name, ", ".join(r_args))
    try:
        result = call(*args, **kwargs)
    except:
        print "EXCEPTION in call to %s" %(r_name,)
        raise
    else:
        print "call to %s result: %r" %(r_name, result)
        return result
def add_tracing_prints_to_method(class_object, method_name):
    wrapfunc(class_object, method_name, tracing_processor)
