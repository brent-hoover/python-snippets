file_object = open('thefile.txt')
try:
    for line in file_object:
        ## process line
finally:
    file_object.close()
