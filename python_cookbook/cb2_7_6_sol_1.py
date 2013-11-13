import new, types, copy_reg
def code_ctor(*args):
    # delegate to new.code the construction of a new code object
    return new.code(*args)
def reduce_code(co):
    # a reductor function must return a tuple with two items: first, the
    # constructor function to be called to rebuild the argument object
    # at a future de-serialization time; then, the tuple of arguments
    # that will need to be passed to the constructor function.
    if co.co_freevars or co.co_cellvars:
        raise ValueError, "Sorry, cannot pickle code objects from closures"
    return code_ctor, (co.co_argcount, co.co_nlocals, co.co_stacksize,
        co.co_flags, co.co_code, co.co_consts, co.co_names,
        co.co_varnames, co.co_filename, co.co_name, co.co_firstlineno,
        co.co_lnotab)
# register the reductor to be used for pickling objects of type 'CodeType'
copy_reg.pickle(types.CodeType, reduce_code)
if __name__ == '__main__':
    # example usage of our new ability to pickle code objects
    import cPickle
    # a function (which, inside, has a code object, of course)
    def f(x): print 'Hello,', x
    # serialize the function's code object to a string of bytes
    pickled_code = cPickle.dumps(f.func_code)
    # recover an equal code object from the string of bytes
    recovered_code = cPickle.loads(pickled_code)
    # build a new function around the rebuilt code object
    g = new.function(recovered_code, globals())
    # check what happens when the new function gets called
    g('world')
