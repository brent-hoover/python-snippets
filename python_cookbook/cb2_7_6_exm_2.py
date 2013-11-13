import new, cPickle
c = cPickle.load(open('saved.pickle','rb'))
g = new.function(c, globals())
g('world')
