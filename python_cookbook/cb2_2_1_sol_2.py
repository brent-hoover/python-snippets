file_object = open('thefile.txt')
try:
    all_the_text = file_object.read()
finally:
    file_object.close()
