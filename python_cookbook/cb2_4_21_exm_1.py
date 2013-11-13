assert len(some_list) == len(probabilities)
    assert 0 <= min(probabilities) and max(probabilities) <= 1
    assert abs(sum(probabilities)-1.0) < 1.0e-5
