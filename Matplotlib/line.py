import matplotlib.pyplot as plt
import numpy as np



x=np.array([2023,2024,2025,2026])
y=np.array([15,30,36,25])

y2=np.array([50,51,54,45])
# plt.plot(x,y)

plt.title("Class Size",
          fontsize=25,
          family="Arial",
          fontweight="10")

plt.xlabel("Years")
plt.ylabel("No of students")

line_style=dict(marker=".",
                markersize=30,
                mfc="cyan",
                mec="red",
                linestyle="dashed",
                linewidth=6)

plt.xticks(x)
plt.yticks(y)
plt.grid(axis="x",
         linewidth=2,
         color="gray",
         linestyle="dashed"
         )

plt.plot(x,y,color="pink",**line_style)
plt.plot(x,y2,color="blue",**line_style)

plt.show()