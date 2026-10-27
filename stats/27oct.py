import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Assumed probability of purchase
p = 0.70

# Example dataset: 1 = purchase, 0 = no purchase
data = {
    "Customer_ID": range(1, 11),
    "Purchase": [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
}

# print(data)

# convert in pandas dataframe

df =pd.DataFrame(data)
print(df)

# mean : 

mean_of_purchase = df['Purchase'].mean()
print(mean_of_purchase)

variance_of_purchase = df['Purchase'].var()
print(variance_of_purchase)

std_of_purchase = df['Purchase'].std()
print(std_of_purchase)

outcomes = [0, 1]
probabilities = [1 - p, p]
plt.bar(outcomes, probabilities)
plt.xlabel("Outcome (0 = No Purchase, 1 = Purchase)")
plt.ylabel("Probability")
plt.title("Bernoulli Distribution")
plt.xticks([0, 1])
plt.show()
