import os, sys, EasyDialogs, Image
# instead of relying on sys.argv, ask the user via a simple dialog:
rotater = ('Rotate right', 'Rotate image by 90 degrees clockwise')
rotatel = ('Rotate left', 'Rotate image by 90 degrees anti-clockwise')
scale = ('Makethumb', 'Make a 100x100 thumbnail')
str = ['Format JPG', 'Format PNG']
cmd = [rotater, rotatel, scale]
optlist = EasyDialogs.GetArgv(str, cmd,
              addoldfile=False, addnewfile=False, addfolder=True)
# now we can parse the arguments and options (we could use getopt, too):
dirs = []
format = "JPEG"
rotationr = False
rotationl = False
resize = False
for arg in optlist:
    if arg == "--Format JPG":
        format = "JPEG"
    if arg == "--Format PNG":
        format = "PNG"
    if arg == "Rotate right":
        rotationr = True
    if arg == "Rotate left":
        rotationl = True
    if arg == "Makethumb":
        resize = True
    if os.path.isdir(arg):
        dirs.append(arg)
if len(dirs) == 0:
    EasyDialogs.Message("No directories specified")
    sys.exit(0)
# Now, another, simpler dialog, uses the system's folder-chooser dialog:
path = EasyDialogs.AskFolder("Choose destination directory")
if not path:
    sys.exit(0)
if not os.path.isdir(path) :
    EasyDialogs.Message("Destination directory not found")
    sys.exit(0)
# and now a progress bar:
tot_numfiles = sum([ len(os.listdir(d)) for d in dirs ])
bar = EasyDialogs.ProgressBar("Processing", tot_numfiles)
for d in dirs:
    for item in os.listdir(d):
        bar.inc()
        try:
            objpict = Image.open(d + "/" + item)
            if resize: objpict.thumbnail((100, 100, 1))
            if rotationr: objpict = objpict.rotate(-90)
            if rotationl: objpict = objpict.rotate(90)
            objpict.save(path + "/" + item + "." + format, format)
        except:
            print item + " is not an image"
# and one last dialog...:
score = EasyDialogs.AskYesNoCancel("Do you like this program?")
if score == 1:
    EasyDialogs.Message("Wwowowowow, EasyDialog roolz, ;-)")
elif score == 0:
    EasyDialogs.Message("Sigh, sorry, will do better next time!-(")
elif score == -1:
    EasyDialogs.Message("Hey, you didn't answer?!")
