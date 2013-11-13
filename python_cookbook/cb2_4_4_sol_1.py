for index, item in enumerate(sequence):
    if item > 23:
        sequence[index] = transform(item)
