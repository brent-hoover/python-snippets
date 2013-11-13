from xml import sax
from xml.sax import handler, saxutils, xmlreader
# the namespace we want to remove in our filter
RDF_NS = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
class RDFFilter(saxutils.XMLFilterBase):
    def __init__ (self, *args):
        saxutils.XMLFilterBase.__init__(self, *args)
        # initially, we're not in RDF, and just one stack level is needed
        self.in_rdf_stack = [False]
    def startElementNS(self, (uri, localname), qname, attrs):
        if uri == RDF_NS or self.in_rdf_stack[-1] == True:
            # skip elements with namespace, if that namespace is RDF or
            # the element is nested in an RDF one -- and grow the stack
            self.in_rdf_stack.append(True)
            return
        # Make a dict of attributes that DON'T belong to the RDF namespace
        keep_attrs = {}
        for key, value in attrs.items():
            uri, localname = key
            if uri != RDF_NS:
                keep_attrs[key] = value
        # prepare the cleaned-up bunch of non-RDF-namespace attributes
        attrs = xmlreader.AttributesNSImpl(keep_attrs, attrs.getQNames())
        # grow the stack by replicating the latest entry
        self.in_rdf_stack.append(self.in_rdf_stack[-1])
        # finally delegate the rest of the operation to our base class
        saxutils.XMLFilterBase.startElementNS(self,
                 (uri, localname), qname, attrs)
    def characters(self, content):
        # skip characters that are inside an RDF-namespaced tag being skipped
        if self.in_rdf_stack[-1]:
            return
        # delegate the rest of the operation to our base class
        saxutils.XMLFilterBase.characters(self, content)
    def endElementNS (self, (uri, localname), qname):
        # pop the stack -- nothing else to be done, if we were skipping
        if self.in_rdf_stack.pop() == True:
            return
        # delegate the rest of the operation to our base class
        saxutils.XMLFilterBase.endElementNS(self, (uri, localname), qname)
def filter_rdf(input, output):
    """ filter_rdf(input=some_input_filename, output=some_output_filename)
        Parses the XML input from the input stream, filtering out all
        elements and attributes that are in the RDF namespace.
    """
    output_gen = saxutils.XMLGenerator(output)
    parser = sax.make_parser()
    filter = RDFFilter(parser)
    filter.setFeature(handler.feature_namespaces, True)
    filter.setContentHandler(output_gen)
    filter.setErrorHandler(handler.ErrorHandler())
    filter.parse(input)
if __name__ == '__main__':
    import StringIO, sys
    TEST_RDF = '''<?xml version="1.0"?>
<metadata xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:dc="http://purl.org/dc/elements/1.1/">
   <title>  This is non-RDF content </title>
   <rdf:RDF>
     <rdf:Description rdf:about="%s">
       <dc:Creator>%s</dc:Creator>
     </rdf:Description>
   </rdf:RDF>
  <element />
</metadata>
'''
    input = StringIO.StringIO(TEST_RDF)
    filter_rdf(input, sys.stdout)
