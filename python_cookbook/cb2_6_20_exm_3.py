def somename(self, *args):
    ## ...some preliminary task...
    try:
        super_method = super(cls, self).somename
    except AttributeError:
        return None
    else:
        return super_method(*args)
