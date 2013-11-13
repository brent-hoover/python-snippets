def rcurry(f, *a, **kw):
    def curried(*more_a, **more_kw):
        return f(*(more_a+a), dict(kw, **more_kw))
    return curried
