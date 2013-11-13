from sgmllib import SGMLParser
class XMLJustText(SGMLParser):
    def handle_data(self, data):
        print data
XMLJustText().feed(open('text.xml').read())
