if __name__ == '__main__':
    tk = Tkinter.Tk()
    length = 10
    dd = DDList(tk, height=length)
    dd.pack()
    for i in xrange(length):
        dd.insert(Tkinter.END, str(i))
    def show():
        ''' show the current ordering every 2 seconds '''
        for x in dd.get(0, Tkinter.END):
            print x,
        print
        tk.after(2000, show)
    tk.after(2000, show)
    tk.mainloop()
