class LookBeforeYouLeap(X, Y, Z):
    def __init__(self):
        for base in self__class__.__bases__:
            if hasattr(base, '__init__'):
                base.__init__(self)
        ## initialization specific to subclass LookBeforeYouLeap
