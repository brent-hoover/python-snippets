import operator
numbers = [1, 2, 3, 0, 0, 6, 5, 3, 0, 12]
bunch_up = paragraphs
for s in bunch_up(numbers, operator.not_, sum): print 'S', s
for l in bunch_up(numbers, bool, len): print 'L', l
