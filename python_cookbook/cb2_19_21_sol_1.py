from itertools import groupby
from operator import itemgetter
def summary(data, key=itemgetter(0), field=itemgetter(1)):
    """ Summarise the given data (a sequence of rows), grouped by the
        given key (default: the first item of each row), giving totals
        of the given field (default: the second item of each row).
        The key and field arguments should be functions which, given a
        data record, return the relevant value.
    """
    for k, group in groupby(data, key):
        yield k, sum(field(row) for row in group)
if __name__ == "__main__":
    # Example: given a sequence of sales data for city within region,
    # _sorted on region_, produce a sales report by region
    sales = [('Scotland', 'Edinburgh', 20000),
             ('Scotland', 'Glasgow', 12500),
             ('Wales', 'Cardiff', 29700),
             ('Wales', 'Bangor', 12800),
             ('England', 'London', 90000),
             ('England', 'Manchester', 45600),
             ('England', 'Liverpool', 29700)]
    for region, total in summary(sales, field=itemgetter(2)):
        print "%10s: %d" % (region, total)
