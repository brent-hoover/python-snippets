if __name__ == "__main__":
    from time import sleep
    pb = progressbar(8, "*")
    for count in range(1, 9):
        pb.progress(count)
        sleep(0.2)
    pb = progressbar(100)
    pb.progress(20)
    sleep(0.3)
    pb.progress(47)
    sleep(0.3)
    pb.progress(90)
    sleep(0.3)
    pb.progress(100)
    print "testing 1:"
    pb = progressbar(1)
    pb.progress(1)
