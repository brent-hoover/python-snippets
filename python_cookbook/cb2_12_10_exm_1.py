def parse(self, source):
        # force connection of self as the lexical handler
        self._parent.setProperty(property_lexical_handler, self)
        # Delegate to XMLFilterBase for the rest
        XMLFilterBase.parse(self, source)
