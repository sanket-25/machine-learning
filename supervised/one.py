import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tf = pd.read_csv('corporate.csv')

print(tf.head())

fig = plt.scatter(tf, x="country", y="year")
fig.show()