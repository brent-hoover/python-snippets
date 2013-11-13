from ctypes import oledll
dll = oledll[r'C:\Path\To\Some.DLL']
dll.DllRegisterServer()
dll.DllUnregisterServer()
