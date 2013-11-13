from xml.sax.saxutils import XMLFilterBase
class text_normalize_filter(XMLFilterBase):
    """ SAX filter to ensure that contiguous text nodes are merged into one
    """
    def __init__(self, upstream, downstream):
        XMLFilterBase.__init__(self, upstream)
        self._downstream = downstream
        self._accumulator = []
    def _complete_text_node(self):
        if self._accumulator:
            self._downstream.characters(''.join(self._accumulator))
            self._accumulator = []
    def characters(self, text):
        self._accumulator.append(text)
    def ignorableWhitespace(self, ws):
        self._accumulator.append(text)
def _wrap_complete(method_name):
    def method(self, *a, **k):
        self._complete_text_node()
        getattr(self._downstream, method_name)(*a, **k)
    # 2.4 only: method.__name__ = method_name
    setattr(text_normalize_filter, method_name, method)
for n in '''startElement startElementNS endElement endElementNS
            processingInstruction comment'''.split():
    _wrap_complete(n)
if __name__ == "__main__":
    import sys
    from xml import sax
    from xml.sax.saxutils import XMLGenerator
    parser = sax.make_parser()
    # XMLGenerator is a special predefined SAX handler that merely writes
    # SAX events back into an XML document
    downstream_handler = XMLGenerator()
    # upstream, the parser; downstream, the next handler in the chain
    filter_handler = text_normalize_filter(parser, downstream_handler)
    # The SAX filter base is designed so that the filter takes on much of the
    # interface of the parser itself, including the "parse" method
    filter_handler.parse(sys.argv[1])
