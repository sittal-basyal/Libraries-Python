import matplotlib.pyplot as plt
import numpy as np

# bar_style=dict(
                
                # linestyle="dashed",
                # linewidth=6)

categories=np.array(["Grains","Fruit","Vegetable","Protein","Dairy"])
value=np.array([4,3,2,5,3])
colors=['red','blue','green','yellow','gray']
plt.title("Daily Consumption")


plt.xlabel("Food")
plt.ylabel("Quantity")

plt.bar(categories,value,color="skyblue")
plt.show()

#Piechart
plt.title("Daily Consumption")

plt.pie(value,
        labels=categories,
        autopct="%.1f%%",
        colors=colors,
        explode=[0,0,0,0,0.1],
        shadow=True,
        startangle=180)

plt.show()