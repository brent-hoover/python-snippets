from Tkinter import *
from notebook import *
# make a toplevel with a notebook in it, with tabs on the left:
root = Tk()
nb = notebook(root, LEFT)
# make a few diverse frames (panels), each using the NB as 'master':
f1 = Frame(nb())
b1 = Button(f1, text="Button 1")
e1 = Entry(f1)
# pack your widgets in the frame before adding the frame to the
# notebook, do NOT pack the frame itself!
b1.pack(fill=BOTH, expand=1)
e1.pack(fill=BOTH, expand=1)
f2 = Frame(nb())
b2 = Button(f2, text='Button 2')
b3 = Button(f2, text='Beep 2', command=Tk.bell)
b2.pack(fill=BOTH, expand=1)
b3.pack(fill=BOTH, expand=1)
f3 = Frame(nb())
# add the frames as notebook 'screens' and run this GUI app
nb.add_screen(f1, "Screen 1")
nb.add_screen(f2, "Screen 2")
nb.add_screen(f3, "dummy")
root.mainloop()
