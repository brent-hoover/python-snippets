import email, email.FeedParser
import re, sys, sgmllib
# what chars are non-Ascii, what max fraction of them can be in a text part
kGuessBinaryThreshold = 0.2
kGuessBinaryRE = re.compile("[\\0000-\\0025\\0200-\\0377]")
# what max fraction of HTML tags can be in a text (non-HTML) part
kGuessHTMLThreshold = 0.05
class Cleaner(sgmllib.SGMLParser):
    entitydefs = {"nbsp": " "}  # I'll break if I want to
    def __init__(self):
        sgmllib.SGMLParser.__init__(self)
        self.result = []
    def do_p(self, *junk):
        self.result.append('\n')
    def do_br(self, *junk):
        self.result.append('\n')
    def handle_data(self, data):
        self.result.append(data)
    def cleaned_text(self):
        return ''.join(self.result)
def stripHTML(text):
    ''' return text, with HTML tags stripped '''
    c = Cleaner()
    try:
      c.feed(text)
    except sgmllib.SGMLParseError:
      return text
    else:
      return c.cleaned_text()
def guessIsBinary(text):
    ''' return whether we can heuristically guess 'text' is binary '''
    if not text: return False
    nMatches = float(len(kGuessBinaryRE.findall(text)))
    return nMatches/len(text) >= kGuessBinaryThreshold
def guessIsHTML(text):
    ''' return whether we can heuristically guess 'text' is HTML '''
    if not text: return False
    lt = len(text)
    textWithoutTags = stripHTML(text)
    tagsChars = float(lt-len(textWithoutTags))
    return tagsChars/lt >= kGuessHTMLThreshold
def getMungedMessage(openFile):
    openFile.seek(0)
    p = email.FeedParser.FeedParser()
    p.feed(openFile.read())
    m = p.close()
    # Fix up multipart content-type when message isn't multi-part
    if m.get_main_type()=="multipart" and not m.is_multipart():
        t = m.get_payload(decode=1)
        if guessIsBinary(t):
            # Use generic "opaque" type
            m.set_type("application/octet-stream")
        elif guessIsHTML(t):
            m.set_type("text/html")
        else:
            m.set_type("text/plain")
    return m
