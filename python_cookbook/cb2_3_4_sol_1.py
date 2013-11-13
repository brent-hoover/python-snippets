import datetime
def totaltimer(times):
    td = datetime.timedelta(0)    # initial value of sum (must be a timedelta)
    duration = sum([
        datetime.timedelta(minutes=m, seconds=s) for m, s in times],
        td)
    return duration
if __name__== '__main__':         # test when module run as main script
    times1 = [(2, 36),            # list containing tuples (minutes, seconds)
              (3, 35),
              (3, 45),]
    times2 = [(3, 0),
              (5, 13),
              (4, 12),
              (1, 10),]
    assert totaltimer(times1) == datetime.timedelta(0, 596)
    assert totaltimer(times2) == datetime.timedelta(0, 815)
    print ("Tests passed.\n"
           "First test total: %s\n"
           "Second test total: %s" % (
            totaltimer(times1), totaltimer(times2)))
