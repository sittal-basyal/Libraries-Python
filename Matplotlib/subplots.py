import matplotlib.pyplot as plt
import numpy as np

#returns tuple
#axes is technically a numoy array
x=np.array([1,2,3,4,5,6])
figure ,axes=plt.subplots(2,2)
axes[0,0].plot(x,x)
axes[0,0].set_title("x")

axes[0,1].plot(x,x**2)
axes[0,1].set_title("x**2")

axes[1,0].plot(x,x**3)
axes[1,0].set_title("x**3")

axes[1,1].plot(x,x**10)
axes[1,1].set_title("x**10")


plt.tight_layout()

plt.show()