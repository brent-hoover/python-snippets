#!/usr/bin/env python
import os, os.path, sys
from Tkinter import *
from tkFileDialog import *
import Image
openfile = '' # full pathname: dir(abs) + root + ext
indir = ''
outdir = ''
def getinfilename():
    global openfile, indir
    ftypes=(('Gif Images', '*.gif'),
            ('Jpeg Images', '*.jpg'),
            ('Png Images', '*.png'),
            ('Tiff Images', '*.tif'),
            ('Bitmap Images', '*.bmp'),
            ("All files", "*"))
    if indir:
        openfile = askopenfilename(initialdir=indir, filetypes=ftypes)
    else:
        openfile = askopenfilename(filetypes=ftypes)
    if openfile:
        indir = os.path.dirname(openfile)
def getoutdirname():
    global indir, outdir
    if openfile:
        indir = os.path.dirname(openfile)
        outfile = asksaveasfilename(initialdir=indir, initialfile='foo')
    else:
        outfile = asksaveasfilename(initialfile='foo')
    outdir = os.path.dirname(outfile)
def save(infile, outfile):
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "Cannot convert", infile
def convert():
    newext = frmt.get()
    path, file = os.path.split(openfile)
    base, ext = os.path.splitext(file)
    if var.get():
        ls = os.listdir(indir)
        filelist = []
        for f in ls:
            if os.path.splitext(f)[1] == ext:
                filelist.append(f)
    else:
        filelist = [file]
    for f in filelist:
        infile = os.path.join(indir, f)
        ofile = os.path.join(outdir, f)
        outfile = os.path.splitext(ofile)[0] + newext
        save(infile, outfile)
    win = Toplevel(root)
    Button(win, text='Done', command=win.destroy).pack()
# Divide GUI into 3 frames: top, mid, bot
root = Tk()
root.title('Image Converter')
topframe = Frame(root, borderwidth=2, relief=GROOVE)
topframe.pack(padx=2, pady=2)
Button(topframe, text='Select image to convert',
       command=getinfilename).pack(side=TOP, pady=4)
multitext = "Convert all image files\n(of this format) in this folder?"
var = IntVar()
chk = Checkbutton(topframe, text=multitext, variable=var).pack(pady=2)
Button(topframe, text='Select save location',
       command=getoutdirname).pack(side=BOTTOM, pady=4)
midframe = Frame(root, borderwidth=2, relief=GROOVE)
midframe.pack(padx=2, pady=2)
Label(midframe, text="New Format:").pack(side=LEFT)
frmt = StringVar()
formats = ['.bmp', '.gif', '.jpg', '.png', '.tif']
for item in formats:
    Radiobutton(midframe, text=item, variable=frmt, value=item).pack(anchor=NW)
botframe = Frame(root)
botframe.pack()
Button(botframe, text='Convert', command=convert).pack(
       side=LEFT, padx=5, pady=5)
Button(botframe, text='Quit', command=root.quit).pack(
       side=RIGHT, padx=5, pady=5)
root.mainloop()
