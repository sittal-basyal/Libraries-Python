import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,2,3,4,5,6,7,8])
y1=np.array([40,60,65,62,68,70,75,78,82])

x2=[0,1,4,8,9,6,7,1,5]
y2=[40,25,46,29,50,45,47,33,49]

plt.title("RelationShip between hrs studied and marks obtained ")

plt.xlabel("Hours Studied ")
plt.ylabel("Marks obtained ")

plt.scatter(x1,y1,
            color="skyblue",
            alpha=0.7,
            label="class A")

plt.scatter(x2,y2,
            color="green",
            alpha=0.7,
            label="class B")

plt.legend(loc="upper left")
plt.show()