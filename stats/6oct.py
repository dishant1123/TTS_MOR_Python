import  numpy as np  

arr = np.array([12,56,89,51,23])

print("mean is  : ",np.mean(arr))
print("median is  : ",np.median(arr))
print("variance  is  : ",np.var(arr))  # 731 
print("standard deviation is  : ",np.std(arr))  # 27 
coef_var = np.std(arr)/np.mean(arr) * 100 
print("coef_var is  : ",coef_var)

print("min is  : ",np.min(arr))
print("max is  : ",np.max(arr))


