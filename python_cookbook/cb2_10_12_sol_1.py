from ctypes import windll
dll = windll[r'C:\Path\To\Some.DLL']
result = dll.DllRegisterServer()
result = dll.DllUnregisterServer()
