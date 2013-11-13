if __name__ == '__main__':
    import copy
    y = YourClass()    # This, of course, does run __init__
    print y
    z = copy.copy(y)   # ...but this doesn't
    print z
