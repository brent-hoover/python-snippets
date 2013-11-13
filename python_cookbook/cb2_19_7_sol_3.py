def chop(iterable, length=2):
    return itertools.izip(*(iter(iterable),)*length)
