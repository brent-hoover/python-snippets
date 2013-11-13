import sys, os, shutil, filecmp
MAXVERSIONS=100
def backup(tree_top, bakdir_name='bakdir'):
    for dir, subdirs, files in os.walk(tree_top):
        # ensure each directory has a subdir called bakdir
        backup_dir = os.path.join(dir, bakdir_name)
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        # stop any recursing into the backup directories
        subdirs[:] = [d for d in subdirs if d != bakdir_name]
        for file in files:
            filepath = os.path.join(dir, file)
            destpath = os.path.join(backup_dir, file)
            # check existence of previous versions
            for index in xrange(MAXVERSIONS):
                backup = '%s.%2.2d' % (destpath, index)
                if not os.path.exists(backup): break
            if index > 0:
                # no need to backup if file and last version are identical
                old_backup = '%s.%2.2d' % (destpath, index-1)
                try:
                    if os.path.isfile(old_backup
                       ) and filecmp.cmp(abspath, old_backup, shallow=False):
                        continue
                    except OSError:
                        pass
            try:
                shutil.copy(filepath, backup)
            except OSError:
                pass
if __name__ == '__main__':
    # run backup on the specified directory (default: the current directory)
    try: tree_top = sys.argv[1]
    except IndexError: tree_top = '.'
    backup(tree_top)
