import reco, pickle
def f(x):
    print 'Hello,', x
pickle.dump(f.func_code, open('saved.pickle','wb'))
