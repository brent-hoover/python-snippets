def make_adder(addend):
    def adder(augend): return augend+addend
    return adder
