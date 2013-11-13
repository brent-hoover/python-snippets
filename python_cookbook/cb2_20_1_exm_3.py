import new
def make_adder(addend):
  def adder(augend): return augend+addend
  return new.function(adder.func_code, adder.func_globals, 'add_%s' % (addend,),
                      adder.func_defaults, adder.func_closure)
