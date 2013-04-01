"""Helps visualize diffs by giving you two parallel lists to print."""
import difflib

def diffprint(a, b):
    sm = difflib.SequenceMatcher(None, a, b)
    opcodes = sm.get_grouped_opcodes().next()

    padded_a = []
    padded_b = []
    for op, i1, i2, j1, j2 in opcodes:
        if op in ('equal', 'replace'):
            padded_a.extend(a[i1:i2])
            padded_b.extend(b[j1:j2])
        elif op == 'insert':
            padded_a.extend([None] * (j2 - j1))
            padded_b.extend(b[j1:j2])
        elif op == 'delete':
            padded_a.extend(a[i1:i2])
            padded_b.extend([None] * (i2 - i1))
    return padded_a, padded_b

if __name__ == "__main__":
    print diffprint('0123', '1234')
    print diffprint('0123', '123')
    print diffprint('123', '153')
    print diffprint('123', '153333')
    print diffprint('153333', '123')
    print diffprint('1112211121', '212111212222')
