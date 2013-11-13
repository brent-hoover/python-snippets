import datetime
from dateutil import rrule, easter
try: set
except NameError: from sets import Set as set
def all_easter(start, end):
    # return the list of Easter dates within start..end
    easters = [easter.easter(y) 
               for y in xrange(start.year, end.year+1)]
    return [d for d in easters if start<=d<=end]
def all_boxing(start, end):
    # return the list of Boxing Day dates within start..end
    one_day = datetime.timedelta(days=1)
    boxings = [easter.easter(y)+one_day 
               for y in xrange(start.year, end.year+1)]
    return [d for d in boxings if start<=d<=end]
def all_christmas(start, end):
    # return the list of Christmas Day dates within start..end
    christmases = [datetime.date(y, 12, 25) 
                   for y in xrange(start.year, end.year+1)]
    return [d for d in christmases if start<=d<=end]
def all_labor(start, end):
    # return the list of Labor Day dates within start..end
    labors = rrule.rrule(rrule.YEARLY, bymonth=9, byweekday=rrule.MO(1),
                         dtstart=start, until=end)
    return [d.date() for d in labors]   # no need to test for in-between here
def read_holidays(start, end, holidays_file='holidays.txt'):
    # return the list of dates from holidays_file within start..end
    try:
        holidays_file = open(holidays_file)
    except IOError, err:
        print 'cannot read holidays (%r):' % (holidays_file,), err
        return []
    holidays = []
    for line in holidays_file:
        # skip blank lines and comments
        if line.isspace() or line.startswith('#'):
            continue
        # try to parse the format: YYYY, M, D
        try:
            y, m, d = [int(x.strip()) for x in line.split(',')]
            date = datetime.date(y, m, d)
        except ValueError:
            # diagnose invalid line and just go on
            print "Invalid line %r in holidays file %r" % (
                line, holidays_file)
            continue
        if start<=date<=end:
            holidays.append(date)
    holidays_file.close()
    return holidays
holidays_by_country = {
    # map each country code to a sequence of functions
    'US': (all_easter, all_christmas, all_labor),
    'IT': (all_easter, all_boxing, all_christmas),
}
def holidays(cc, start, end, holidays_file='holidays.txt'):
    # read applicable holidays from the file
    all_holidays = read_holidays(start, end, holidays_file)
    # add all holidays computed by applicable functions
    functions = holidays_by_country.get(cc, ())
    for function in functions:
        all_holidays += function(start, end)
    # eliminate duplicates
    all_holidays = list(set(all_holidays))
    # uncomment the following 2 lines to return a sorted list:
    # all_holidays.sort()
    # return all_holidays
    return len(all_holidays)    # comment this out if returning list
if __name__ == '__main__':
    test_file = open('test_holidays.txt', 'w')
    test_file.write('2004, 9, 6\n')
    test_file.close()
    testdates = [ (datetime.date(2004, 8,  1), datetime.date(2004, 11, 14)),
                  (datetime.date(2003, 2, 28), datetime.date(2003,  5, 30)),
                  (datetime.date(2004, 2, 28), datetime.date(2004,  5, 30)),
                ]
    def test(cc, testdates, expected):
        for (s, e), expect in zip(testdates, expected):
            print 'total holidays in %s from %s to %s is %d (exp %d)' % (
                    cc, s, e, holidays(cc, s, e, test_file.name), expect)
            print
    test('US', testdates, (1,1,1) )
    test('IT', testdates, (1,2,2) )
    import os
    os.remove(test_file.name)
