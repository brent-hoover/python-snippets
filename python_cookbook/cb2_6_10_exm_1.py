class proxy(ref):
    def __call__(self, *args, **kwargs):
        func = ref.__call__(self)
        if func is None:
            raise weakref.ReferenceError('referent object is dead')
        else:
            return func(*args, **kwargs)
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return ref.__call__(self) == ref.__call__(other)
