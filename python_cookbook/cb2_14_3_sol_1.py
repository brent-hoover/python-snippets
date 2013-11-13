#!/usr/local/bin/python
import cgi
import cgitb; cgitb.enable()
import os, sys
try: import msvcrt             # are we on Windows?
except ImportError: pass       # nope, no problem
else:                          # yep, need to set I/O to binary mode
    for fd in (0, 1): msvcrt.setmode(fd, os.O_BINARY)
UPLOAD_DIR = "/tmp"
HTML_TEMPLATE = \
"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><head><title>Upload Files</title>
</head><body><h1>Upload Files</h1>
<form action="%(SCRIPT_NAME)s" method="POST" enctype="multipart/form-data">
File name: <input name="file_1" type="file"><br>
File name: <input name="file_2" type="file"><br>
File name: <input name="file_3" type="file"><br>
<input name="submit" type="submit">
</form> </body> </html>"""
def print_html_form():
    """ print the form to stdout, with action set to this very script (a
       'self-posting form': script both displays AND processes the form). """
    print "content-type: text/html; charset=iso-8859-1\n"
    print HTML_TEMPLATE % {'SCRIPT_NAME': os.environ['SCRIPT_NAME']}
def save_uploaded_file(form_field, upload_dir):
    """ Save to disk a file just uploaded, form_field being the name of the
        file input field on the form.  No-op if field or file is missing. """
    form = cgi.FieldStorage()
    if not form.has_key(form_field): return
    fileitem = form[form_field]
    if not fileitem.file: return
    fout = open(os.path.join(upload_dir, fileitem.filename), 'wb')
    while True:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        fout.write(chunk)
    fout.close()
save_uploaded_file("file_1", UPLOAD_DIR)
save_uploaded_file("file_2", UPLOAD_DIR)
save_uploaded_file("file_3", UPLOAD_DIR)
print_html_form()
