"""
	days    sales (clothes)

	1	2000
	2   2200
	3	2800
	4	2000
	5	3000
	6	3400
	7	2100
	8	3000
	9	3500
	10	45000
		=======
		69000   ----->avg  sales per  day  = 6900
	
	2 method  : 

	IQR : inter Quartile Range 
		
	IQR = Q3 -Q1 
	
	Q3 = sales * 0.75 
	Q1 =sales  * 0.25 
	IQR = Q3-Q1 

	lower_limit = Q1 - 1.5*IQR ----->4500
	upper_limit = Q3 + 1.5*IQR -----> 7000

	
"""

import numpy as np
import matplotlib.pyplot as plt  # pip  install matplotlib

# plot  : 
"""
sales = np.array([2000,2200,2800,2000,3000,3400,2100,3000,3500,45000])
days = np.array([1,2,3,4,5,6,7,8,9,10])

plt.plot(days,sales)
plt.xlabel('days')
plt.ylabel('sales')
plt.title('sales per day')
plt.show()

"""

# box  plot  : 

sales = np.array([2000,3200,4800,5000,7000,8400,6100,9000,10500,45000])

plt.boxplot(sales)
# plt.show()

# IQR : 
Q3 = np.percentile(sales,75)
Q1= np.percentile(sales,25)
print("Q3 : ",Q3)
print("Q1 : ",Q1)

IQR = Q3 - Q1
print("IQR : ",IQR)

lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR

print("lower_limit : ",lower_limit)
print("upper_limit : ",upper_limit)
