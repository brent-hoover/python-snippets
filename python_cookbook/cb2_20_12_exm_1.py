if __name__ == "__main__":
    class B(Cooperative):
        def say(self):
            print "B",
    class C(B):
        def say(self, super):
            super.say()
            print "C",
    class D(B):
        def say(self, super):
            super.say()
            print "D",
    class CD(C, D):
        def say(self, super):
            super.say()
            print '!'
    CD().say()
# emits: B D C !
