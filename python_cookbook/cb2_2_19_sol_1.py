import glob, os
def all_files(pattern, search_path, pathsep=os.pathsep):
    """ Given a search path, yield all files matching the pattern. """
    for path in search_path.split(pathsep):
	for match in glob.glob(os.path.join(path, pattern)):
            yield match
