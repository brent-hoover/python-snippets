import collections
class CCM_with_deque(ChangeCheckerMixin):
    containerItems = dict(ChangeCheckerMixin)
    containerItems[collections.deque] = enumerate
