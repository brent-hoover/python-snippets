def avgsum(data):       # Sum all of the elements, then divide
    return sum(data, F(0)) / len(data)
def avgrun(data):       # Make small adjustments to a running mean
    m = data[0]
    k = 1
    for x in data[1:]:
        k += 1
        m += (x-m)/k    # Recurrence formula for mean
    return m
def avgrun_kahan(data): # Adjustment method with Kahan error correction term
    m = data[0]
    k = 1
    dm = 0
    for x in data[1:]:
        k += 1
        adjm = (x-m)/k - dm
        newm = m + adjm
        dm = (newm - m) - adjm
        m = newm
    return m
