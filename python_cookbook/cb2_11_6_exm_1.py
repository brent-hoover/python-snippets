def makeImageWidget(icondata, *args, **kwds):
    if args:
        klass = args.pop(0)
    else:
        klass = Tkinter.Button
    class Widget(klass):
        def __init__(self, image, *args, **kwds):
            kwds['image'] = image
            klass.__init__(self, *args, **kwds)
            self.__image = image
    return Widget(Tkinter.PhotoImage(data=icondata), *args, **kwds)
