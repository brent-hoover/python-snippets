def uniquer_with_simplest_fallback(seq, f=None):
    if f is None:
        def f(x): return x
    already_seen = set()
    result = []
    for item in seq:
        marker = f(item)
        try:
            new_marker = marker not in already_seen
        except TypeError:
            class TotallyFakeSet(list):
                add = list.append
            already_seen = TotallyFakeSet(already_seen)
            new_marker = marker not in already_seen
         if new_marker:
             already_seen.add(marker)
             result.append(item)
    return result
