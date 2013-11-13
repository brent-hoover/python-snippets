for index in range(len(sequence)):
    if sequence[index] > 23:
        sequence[index] = transform(sequence[index])
