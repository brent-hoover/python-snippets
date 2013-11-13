def packitem(item, pkg=None):
    if pkg is None:
        pkg = []
    pkg.append(item)
    return pkg
