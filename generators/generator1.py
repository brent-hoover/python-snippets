def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

if __name__ == '__main__':
    sum_of_first_n = sum(firstn(1000000))
    print(sum_of_first_n)