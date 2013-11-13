import Tkinter
if __name__ == '__main__':
    root = Tkinter.Tk()
    iconImage = Tkinter.PhotoImage(master=root, data=icon)
    Tkinter.Button(image=iconImage).pack()
