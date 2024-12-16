import numpy as np
arr=np.arange(20)
print(arr)
arr_slice=slice(1,10,2)
element=arr[6]
print(f"{element}: {type(element)}")
print(arr[arr_slice])
print(arr[1:10:2])
