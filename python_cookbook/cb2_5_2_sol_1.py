def case_insensitive_sort(string_list):
    auxiliary_list = [(x.lower(), x) for x in string_list]    # decorate
    auxiliary_list.sort()                                     # sort
    return [x[1] for x in auxiliary_list]                     # undecorate
