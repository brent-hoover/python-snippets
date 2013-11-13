import Tkinter
def hello(name):
    print "Hello", name
root = Tk()
# the lambda way of doing it:
Button(root, text="Guido", command=lambda name="Guido": hello(name)).pack()
# using the Command class:
Button(root, text="Guido", command=command(hello, "Guido")).pack()
