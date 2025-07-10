import numpy as np

vec1 = np.array([1,0])
vec2 = np.array([0,1])
result = vec1 + vec2
#vector subtraction can be done by vec1-vec2
print(result)

#without numpy it would be slower and look like this
#result=[]
#forn,m in zip(vec1,vec2):
#z.append(vec1+vec2)

result *= 2 #scalar multiplication
print(result)

vectorProduct = vec1*vec2
print(vectorProduct)

vectorProduct += 1  #constant addition 
print(vectorProduct)

dotProduct = np.dot(vectorProduct,result)
print(dotProduct)