# array  :  -----> pip install numpy

import numpy as np
from scipy import stats

arr =np.array([90,45,90,67,89,90,27,99,11,45,45])

print("mean of  array is  : ",np.mean(arr)) 
print("median of array is  : ",np.median(arr))

print("mode of array is  : ",stats.mode(arr)[0])

