def command(callback, *args, **kwargs):
    def do_call():
        return callback(*args, **kwargs)
    # 2.4 only: do_call.__name__ = callback.__name__
    return do_call
