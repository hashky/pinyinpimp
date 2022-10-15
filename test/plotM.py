#!/usr/bin/python3
import numpy as np
import pinyinpimp as pp
from matplotlib import pyplot as plt


M = pp.util.mk_distance_matrix(metric=pp.util.pin_adic)

print(M[1:255,1:255])
plt.imshow(M)
plt.show()

plt.figure ()
M = pp.util.mk_distance_matrix()

print(M[1:255,1:255])
plt.imshow(M)
plt.show()


