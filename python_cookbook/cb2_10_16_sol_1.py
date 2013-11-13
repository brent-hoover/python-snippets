from win32com.client import gencache, constants
DEBUG = False
class MSOutlook(object):
    def __init__(self):
        try:
            self.oOutlookApp = gencache.EnsureDispatch("Outlook.Application")
            self.outlookFound = True
        except:
            print "MSOutlook: unable to load Outlook"
            self.outlookFound = False
        self.records = []
    def loadContacts(self, keys=None):
        if not self.outlookFound: return
        onMAPI = self.oOutlookApp.GetNamespace("MAPI")
        ofContacts = onMAPI.GetDefaultFolder(constants.olFolderContacts)
        if DEBUG: print "number of contacts:", len(ofContacts.Items)
        for oc in range(len(ofContacts.Items)):
            contact = ofContacts.Items.Item(oc + 1)
            if contact.Class == constants.olContact:
                if keys is None:
                    # no keys were specified, so build up a list of all keys
                    # that belong to some types we know we can deal with
                    good_types = int, str, unicode
                    keys = [key for key in contact._prop_map_get_
                        if isinstance(getattr(contact, key), good_types) ]
                    if DEBUG:
                        print "Fields\n=================================="
                        keys.sort()
                        for key in keys: print key
                record = {}
                for key in keys:
                    record[key] = getattr(contact, key)
                self.records.append(record)
                if DEBUG:
                    print oc, contact.FullName
if __name__ == '__main__':
    if '-d' in sys.argv:
        DEBUG = True
    if DEBUG:
        print "attempting to load Outlook"
    oOutlook = MSOutlook()
    if not oOutlook.outlookFound:
        print "Outlook not found"
        sys.exit(1)
    fields = ['FullName', 'CompanyName',
              'MailingAddressStreet', 'MailingAddressCity',
              'MailingAddressState', 'MailingAddressPostalCode',
              'HomeTelephoneNumber', 'BusinessTelephoneNumber',
              'MobileTelephoneNumber', 'Email1Address', 'Body',
             ]
    if DEBUG:
        import time
        print "loading records..."
        startTime = time.time()
    # to get all fields just call oOutlook.loadContacts()
    # but getting a specific set of fields is much faster
    oOutlook.loadContacts(fields)
    if DEBUG:
        print "loading took %f seconds" % (time.time() - startTime)
    print "Number of contacts: %d" % len(oOutlook.records)
    print "Contact: %s" % oOutlook.records[0]['FullName']
    print "Body:\n%s" % oOutlook.records[0]['Body']
