if __name__ == '__main__':
    def main():
        root = Tk()
        sw = StopWatch(root)
        sw.pack(side=TOP)
        Button(root, text='Start', command=sw.Start).pack(side=LEFT)
        Button(root, text='Stop', command=sw.Stop).pack(side=LEFT)
        Button(root, text='Reset', command=sw.Reset).pack(side=LEFT)
        Button(root, text='Quit', command=root.quit).pack(side=LEFT)
        root.mainloop()
    main()
