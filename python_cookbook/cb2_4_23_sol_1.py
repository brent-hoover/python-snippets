import __builtin__
def ensureDefined(name, defining_code, target=__builtin__):
    if not hasattr(target, name):
	d = {}
        exec defining_code in d
	assert name in d, 'Code %r did not set name %r' % (
	    defining_code, name)
	setattr(target, name, d[name])
