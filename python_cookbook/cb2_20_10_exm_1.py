new_thing = X.__new__(X, *a, **k)
    if isinstance(new_thing, X):
        X.__init__(new_thing, *a, **k)
