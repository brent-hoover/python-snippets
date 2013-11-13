try:
    sorted
except:
    def sorted(data):
        data = list(data)
        data.sort()
        return data
import itertools
def top10(data, howtosort):
    return list(itertools.islice(howtosort(data), 10))
