def curry(f, *a, **kw):
    def curried(*more_a, **more_kw):
        return f(*(a+more_a), dict(kw, **more_kw))
    return curried
