if __name__ == '__main__':
    arr = [0.123456789012345]*10000000
    true_answer = arr[0] * len(arr)
    print '"True" result: %r' % true_answer
    sum_result = sum(arr)
    print '"sum"  result: %r' % sum_result
    sum_p_resu = sum_with_partials(arr)
    print 'sum_p. result: %r' % sum_p_resu
# emits:
# "True" result: 1234567.89012345
# "sum"  result: 1234567.8902233159
# sum_p. result: 1234567.89012345
