if __name__ == '__main__':
    root = Tk()
    le1 = LabeledEntry(root, name='label1', text='Label 1: ',
                       width=5, relief=SUNKEN, bg='white', padx=3)
    le2 = LabeledEntry(root, name='label2', text='Label 2: ',
                       relief=SUNKEN, bg='red', padx=3)
    le3 = LabeledEntry(root, name='label3', text='Label 3: ',
                       width=40, relief=SUNKEN, bg='yellow', padx=3)
    le1.pack(expand=1, fill=X)
    le2.pack(expand=1, fill=X)
    le3.pack(expand=1, fill=X)
    root.mainloop()
