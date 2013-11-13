import csv
    sales = sorted(cvs.reader(open('sales.csv', 'rb')),
                   key=itemgetter(1))
    for region, total in summary(sales, field=itemgetter(2)):
        print "%10s: %d" % (region, total)
