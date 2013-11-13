import calldll, struct
# some helpful auxiliary functions
def myPrintLong(vVar):
    ''' print a long contained in a membuf '''
    print calldll.read_long(vVar.address())
def myPrintString(vVar):
    ''' print a string contained in a membuf '''
    a = calldll.read_string(vVar.address())
    print a, len(a)
def mySetLong(vMemBuf, vValueToSet):
    ''' set to an unsigned long the value of a membuf with len == 4 '''
    vMemBuf.write(struct.pack('L', vValueToSet))
def mySetString(vMemBuf, vValueToSet):
    ''' set to a string (with \0 terminator) the value of a membuf '''
    pack_format = "%ds" % 1+len(vValueToSet)              # +1 for the \0
    string_packed = struct.pack(pack_format, vValueToSet) # pack() adds the \0
    vMemBuf.write(string_packed)
# load 'Ehllapi.dll' (from current dir), and function 'hllapi' from the DLL
dll_handle = calldll.load_library ('.\\Ehllapi')
function_address = calldll.get_proc_address (dll_handle, 'HLLAPI')
# allocate and init three membufs with the size to hold an unsigned long
Lsize = struct.calcsize('L')
vFunction = calldll.membuf(Lsize)
mySetLong(vFunction, 1)
vTextLen = calldll.membuf(Lsize)
vResult = calldll.membuf(Lsize)
mySetLong(vResult, 1)
# allocate a membuf as large as the DLL requires; in this case, space
# for 24 x 80 characters + 1 for a \0 terminator
vText = calldll.membuf(1921)
# init the text and text-length variables based on string of interest
string_value_to_write = 'A'
mySetString(vText, string_value_to_write)
mySetLong(vTextLen, len(string_value_to_write))
# call the function, print the results, and clean up
calldll.call_foreign_function(function_address, 'llll', 'l',
  (vFunction.address(), vText.address(), vTextLen.address(), vResult.address()))
myPrintLong(vResult)
myPrintString(vText)
calldll.free_library(dll_handle)
