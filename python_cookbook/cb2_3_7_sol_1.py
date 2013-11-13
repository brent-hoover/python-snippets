import datetime
import dateutil.parser
def tryparse(date):
    # dateutil.parser needs a string argument: let's make one from our
    # `date' argument, according to a few reasonable conventions...:
    kwargs = {}                                    # assume no named-args
    if isinstance(date, (tuple, list)):
        date = ' '.join([str(x) for x in date])    # join up sequences
    elif isinstance(date, int):
        date = str(date)                           # stringify integers
    elif isinstance(date, dict):
        kwargs = date                              # accept named-args dicts
        date = kwargs.pop('date')                  # with a 'date' str
    try:
        try:
            parsedate = dateutil.parser.parse(date, **kwargs)
            print 'Sharp %r -> %s' % (date, parsedate)
        except ValueError:
            parsedate = dateutil.parser.parse(date, fuzzy=True, **kwargs)
            print 'Fuzzy %r -> %s' % (date, parsedate)
    except Exception, err:
        print 'Try as I may, I cannot parse %r (%s)' % (date, err)
if __name__ == "__main__":
    tests = (
            "January 3, 2003",                     # a string
            (5, "Oct", 55),                        # a tuple
            "Thursday, November 18",               # longer string without year
            "7/24/04",                             # a string with slashes
            "24-7-2004",                           # European-format string
            {'date':"5-10-1955", "dayfirst":True}, # a dict including the kwarg
            "5-10-1955",                           # dayfirst, no kwarg
            19950317,                              # not a string
            "11AM on the 11th day of 11th month, in the year of our Lord 1945",
            )
    for test in tests:                             # testing date formats
        tryparse(test)                             # try to parse
