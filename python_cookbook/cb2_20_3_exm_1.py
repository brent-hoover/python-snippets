class Book(object):
    def __init__(self, title, shortTitle=None):
        self.title = title
        if shortTitle is not None:
            self.shortTitle = shortTitle
    shortTitle = DefaultAlias('title')
b = Book('The Life and Opinions of Tristram Shandy, Gent.')
print b.shortTitle
# emits: The Life and Opinions of Tristram Shandy, Gent.
b.shortTitle = "Tristram Shandy"
print b.shortTitle
# emits: Tristram Shandy
del b.shortTitle
print b.shortTitle
# emits: The Life and Opinions of Tristram Shandy, Gent.
