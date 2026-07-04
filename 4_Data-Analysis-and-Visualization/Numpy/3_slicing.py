import numpy as np
a = np.array([1,2,3,4,5])
d = a[2:4]  #elements at index after 2 till 4
print(d)
a[2:4] = 300,400    #updating by slicing
print(a)