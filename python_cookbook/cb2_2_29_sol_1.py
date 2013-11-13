def VersionFile(file_spec, vtype='copy'):
    import os, shutil
    if os.path.isfile(file_spec):
        # check the 'vtype' parameter
        if vtype not in ('copy', 'rename'):
             raise ValueError, 'Unknown vtype %r' % (vtype,)
        # Determine root filename so the extension doesn't get longer
        n, e = os.path.splitext(file_spec)
        # Is e a three-digits integer preceded by a dot?
        if len(e) == 4 and e[1:].isdigit():
            num = 1 + int(e[1:])
            root = n
        else:
            num = 0
            root = file_spec
        # Find next available file version
        for i in xrange(num, 1000):
             new_file = '%s.%03d' % (root, i)
             if not os.path.exists(new_file):
                  if vtype == 'copy':
                      shutil.copy(file_spec, new_file)
                  else:
                      os.rename(file_spec, new_file)
                  return True
        raise RuntimeError, "Can't %s %r, all names taken"%(vtype,file_spec)
    return False
if __name__ == '__main__':
      import os
      # create a dummy file 'test.txt'
      tfn = 'test.txt'
      open(tfn, 'w').close()
      # version it 3 times
      print VersionFile(tfn)
      # emits: True
      print VersionFile(tfn)
      # emits: True
      print VersionFile(tfn)
      # emits: True
      # remove all test.txt* files we just made
      for x in ('', '.000', '.001', '.002'):
          os.unlink(tfn + x)
      # show what happens when the file does not exist
      print VersionFile(tfn)
      # emits: False
      print VersionFile(tfn)
      # emits: False
