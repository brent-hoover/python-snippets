if __name__ == '__main__':
    a = Fifo()
    a.append(10)
    a.append(20)
    print a.pop(),
    a.append(5)
    print a.pop(),
    print a.pop(),
    print
# emits: 10 20 5
