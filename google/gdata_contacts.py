import sha
import atom
import gdata.contacts
import gdata.contacts.service
 
gd_client = gdata.contacts.service.ContactsService()

# Change this obviously 
gd_client.email = ''brent@thebuddhalodge.com''
gd_client.password = ''u&K8&a4&''
gd_client.ProgrammaticLogin()

"""
This is used like a case statement later on.
It''s apparently a slightly slow way to do it but it just seems so elegant to me.  I''m not a Pythonista at all though so there may be a more Pythonic way to do it that I''m not aware of.
""" 
rel_list = {gdata.contacts.REL_WORK: "Work",
            gdata.contacts.REL_HOME: "Home",
            gdata.contacts.REL_OTHER: "Other",
            gdata.contacts.PHONE_MOBILE: "Mobile"}

# This is the date used for "updated_min" below.
date = ''2009-08-12T00:00:00''
 
query = gdata.contacts.service.ContactsQuery()
