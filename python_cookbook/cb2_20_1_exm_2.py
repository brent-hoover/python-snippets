def make_adder(addend):
    def adder(augend):
        return augend+addend
    adder.__name__ = 'add_%s' % (addend,)
    return adder
