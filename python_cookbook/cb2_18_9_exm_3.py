def cond(test, when_true, when_false):
    if test:
        return when_true()
    else:
        return when_false()
