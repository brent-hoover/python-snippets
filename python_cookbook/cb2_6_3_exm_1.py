class Person(NoNewAttrs):
    firstname = ''
    lastname = ''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __repr__(self):
        return 'Person(%r, %r)' % (self.firstname, self.lastname)
me = Person("Michere", "Simionato")
print me
# emits: Person('Michere', 'Simionato')
# oops, wrong value for firstname, can we fix it?  Sure, no problem!
me.firstname = "Michele"
print me
# emits: Person('Michele', 'Simionato')
