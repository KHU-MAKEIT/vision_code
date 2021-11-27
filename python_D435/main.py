import ctypes
 
# Load DLL into memory.

#hllDll = ctypes.WinDLL ("c:\\PComm\\ehlapi32.dll")

test_c_codes = ctypes.cdll.LoadLibrary("./libhello.so")
print(test_c_codes)
foo_c_func = test_c_codes.Hello()
foo_c_func = test_c_codes.NotHello()
 
#print bar_c_func("airpage")