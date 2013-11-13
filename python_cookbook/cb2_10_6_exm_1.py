def edited_text(starting_text=''):
    temp_file = tempfile.NamedTemporaryFile()
    temp_file.write(starting_text)
    temp_file.seek(0)
    editor = what_editor()
    x = os.spawnlp(os.P_WAIT, editor, editor, temp_file.name)
    if x:
        raise RuntimeError, "Can't run %s %s (%s)" % (editor, temp_file.name, x)
    return temp_file.read()
