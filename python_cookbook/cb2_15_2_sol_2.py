# Client code sxr_client.py
import xmlrpclib
server = xmlrpclib.Server('http://localhost:8000')
print server.chop_in_half('I am a confident guy')
# emits: I an a con
print server.repeat('Repetition is the key to learning!\n', 5)
# emits 5 lines, all Repetition is the key to learning!
print server._string('<= underscore')
# emits _<= underscore
print server.python_string.join(['I', 'like it!'], " don't ")
# emits I don't like it!
print server._privateFunction()    # this will throw an exception
# terminates client script with traceback for xmlrpclib.Fault
