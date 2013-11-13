def remove_whilespace_nodes(node):
    """ Removes all of the whitespace-only text decendants of a DOM node. """
    # prepare the list of text nodes to remove (and recurse when needed)
    remove_list = []
    for child in node.childNodes:
        if child.nodeType == dom.Node.TEXT_NODE and not child.data.strip():
            # add this text node to the to-be-removed list
            remove_list.append(child)
        elif child.hasChildNodes():
            # recurse, it's the simplest way to deal with the subtree
            remove_whilespace_nodes(child)
    # perform the removals
    for node in remove_list:
        node.parentNode.removeChild(node)
        node.unlink()
