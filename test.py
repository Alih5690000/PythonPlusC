import module 
import time
import ctypes
arr=range(999999)
start=time.time()
sum(arr)
end=time.time()
print(f"spend {end-start}")
arr=range(999999)
raw_arr_t=ctypes.c_int*999999
raw_arr=raw_arr_t(*arr)
start=time.time()
module.sumof_raw(raw_arr,999999)
end=time.time()
print(f"spend {end-start}")