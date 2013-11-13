def smallmerge(*subsequences):
    result = []
    for subseq in subsequences: result.extend(subseq)
    result.sort()
    return result
