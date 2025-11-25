import numpy as np
scores=np.array([35,27,96,85])
scores[scores<35]=0
print(scores)