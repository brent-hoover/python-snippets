list_of_all_the_lines = file_object.read().splitlines()
list_of_all_the_lines = file_object.read().split('\n')
list_of_all_the_lines = [L.rstrip('\n') for L in file_object]
