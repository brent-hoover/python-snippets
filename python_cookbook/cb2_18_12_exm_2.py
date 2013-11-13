digs = [ d+'-' for d in
         'zero one two three four five six seven eight nine'.split() ]
print format(315, 10, digs).rstrip('-')
# emits: three-one-five
