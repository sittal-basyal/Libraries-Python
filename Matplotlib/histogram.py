import matplotlib.pyplot as plt
import numpy as np

scores=np.random.normal(loc=80,scale=50,size=100)
scores=np.clip(scores,0,100)

plt.title("Class 12 A")
plt.xlabel("MArks obtained")
plt.ylabel("Students frquency")
plt.hist(scores,bins=10,
         color="lightgreen",
         edgecolor="black")
plt.show()