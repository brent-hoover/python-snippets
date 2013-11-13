if result:
        result.extend(itertools.repeat(None, length-len(result)))
        yield result
