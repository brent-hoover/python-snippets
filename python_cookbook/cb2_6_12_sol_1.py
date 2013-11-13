import copy
class ChangeCheckerMixin(object):
    containerItems = {dict: dict.iteritems, list: enumerate}
    immutable = False
    def snapshot(self):
        ''' create a snapshot of self's state -- like a shallow copy, but
            recursing over container types (not over general instances:
            instances must keep track of their own changes if needed).  '''
        if self.immutable:
            return
        self._snapshot = self._copy_container(self.__dict__)
    def makeImmutable(self):
        ''' the instance state can't change any more, set .immutable '''
        self.immutable = True
        try:
            del self._snapshot
        except AttributeError:
            pass
    def _copy_container(self, container):
        ''' semi-shallow copy, recursing on container types only '''
        new_container = copy.copy(container)
        for k, v in self.containerItems[type(new_container)](new_container):
            if type(v) in self.containerItems:
                new_container[k] = self._copy_container(v)
            elif hasattr(v, 'snapshot'):
                v.snapshot()
        return new_container
    def isChanged(self):
        ''' True if self's state is changed since the last snapshot '''
        if self.immutable:
            return False
        # remove snapshot from self.__dict__, put it back at the end
        snap = self.__dict__.pop('_snapshot', None)
        if snap is None:
            return True
        try:
            return self._checkContainer(self.__dict__, snap)
        finally:
            self._snapshot = snap
    def _checkContainer(self, container, snapshot):
        ''' return True if the container and its snapshot differ '''
        if len(container) != len(snapshot):
            return True
        for k, v in self.containerItems[type(container)](container):
            try:
                ov = snapshot[k]
            except LookupError:
                return True
            if self._checkItem(v, ov):
                return True
        return False
    def _checkItem(self, newitem, olditem):
        ''' compare newitem and olditem.  If they are containers, call
            self._checkContainer recursively.  If they're an instance with
            an 'isChanged' method, delegate to that method.  Otherwise,
            return True if the items differ. '''
        if type(newitem) != type(olditem):
            return True
        if type(newitem) in self.containerItems:
            return self._checkContainer(newitem, olditem)
        if newitem is olditem:
            method_isChanged = getattr(newitem, 'isChanged', None)
            if method_isChanged is None:
                return False
            return method_isChanged()
        return newitem != olditem
