from ctypes import windll, c_int, c_string, byref
# load 'Ehllapi.dll' (from current dir), and function 'hllapi' from the DLL
Ehllap32 = windll.ehllapi
hllapi = Ehllap32.hllapi
# prepare the arguments with types and initial values
h_func = c_int(1)
h_text = c_string('A')
h_len = c_int(1)
h_ret = c_int(999)
# call the function
hllapi(byref(h_func), h_text, byref(h_len), byref(h_ret))
# print the resulting values of all arguments after the call
print h_func.value, h_text.value, h_len.value, h_ret.value
