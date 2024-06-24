from matplotlib import pyplot as plt
import numpy as np
data=np.genfromtxt('D:/univercity/article/STGN-main/nparray/test.out', dtype=None, delimiter=',')
plt.imshow(data, interpolation='nearest')
plt.show()