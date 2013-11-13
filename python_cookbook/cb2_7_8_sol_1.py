try:
    from bsddb import db                  # first try release 4
except ImportError:
    from bsddb3 import db                 # not there, try release 3 instead
print db.DB_VERSION_STRING
# emits, e.g: Sleepycat Software: Berkeley DB 4.1.25: (December 19, 2002)
