memoized_metaclasses_map = {}
def _get_noconflict_metaclass(bases, left_metas, right_metas):
     # make tuple of needed metaclasses in specified order
     metas = left_metas + tuple(map(type, bases)) + right_metas
     needed_metas = remove_redundant(metas)
     # return existing confict-solving meta, if any
     try: return memoized_metaclasses_map[needed_metas]
     except KeyError: pass
     # compute, memoize and return needed conflict-solving meta
     if not needed_metas:         # whee, a trivial case, happy us
         meta = type
     elif len(needed_metas) == 1: # another trivial case
         meta = needed_metas[0]
     else:                        # nontrivial, darn, gotta work...
         # ward against non-type root metatypes
         for m in needed_metas:
             if not issubclass(m, type):
                 raise TypeError( 'Non-type root metatype %r' % m)
         metaname = '_' + ''.join([m.__name__ for m in needed_metas])
         meta = classmaker()(metaname, needed_metas, {})
     memoized_metaclasses_map[needed_metas] = meta
     return meta
def classmaker(left_metas=(), right_metas=()):
     def make_class(name, bases, adict):
         metaclass = _get_noconflict_metaclass(bases, left_metas, right_metas)
         return metaclass(name, bases, adict)
     return make_class
