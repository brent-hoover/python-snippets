def cross_list(*sequences):
    result = [[]]
    for seq in sequences:
        result = [sublist+[item] for sublist in result for item in seq]
    return result
