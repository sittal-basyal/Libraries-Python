import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("dog_data.csv")
type_count=df["Breed"].value_counts(ascending=True)

plt.barh(type_count.index,type_count.values)

plt.tight_layout()

plt.show()