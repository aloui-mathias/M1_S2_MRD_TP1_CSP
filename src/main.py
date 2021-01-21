from pycsp3 import *

k, n = data

box = VarArray (size = n, dom = range(k))

satisfy(
    (box[i-1]!=box[j-1]) & (box[i-1]!=box[i+j-1]) & (box[j-1]!=box[i+j-1])
    for i in range(1,n+1) for j in range(i+1,n+1-i)
)