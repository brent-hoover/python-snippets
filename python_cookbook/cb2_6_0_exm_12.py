if '__metaclass__' in d: M = d['__metaclass__']
elif b: M = type(b[0])
elif '__metaclass__' in globals(): M = globals()['__metaclass__']
else: M = types.ClassType
