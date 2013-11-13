import tkSimpleDialog
_dispatch = { str: tkSimpleDialog.askstring,
              int: tkSimpleDialog.askinteger,
              float: tkSimpleDialog.askfloat,
            }
def getinput(title, prompt, type=str, default=None, min=None, max=None):
    ''' gets from the user an input of type `type' (str, int or float),
        optionally with a default value, and optionally constrained to
        lie between the values `min' and `max' (included).
    '''
    f = _dispatch.get(type)
    if not f:
        raise TypeError, "Can't ask for %r input" % (type,)
    return f(title, prompt, initialvalue=default, minvalue=min, maxvalue=max)
