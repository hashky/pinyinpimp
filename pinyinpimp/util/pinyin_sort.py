import numpy as np

# import matplotlib.pyplot as plt
from .. import data as pin

n = len(pin.allpin)
M = np.zeros((n, n))


def pin_adic(pin1, pin2, p=3):
    """specialized function for p-adic ultrametric between two elements of a set that is max 6 chars"""
    s = 0
    for j, (p1, p2) in enumerate(zip(pin1.ljust(6), pin2.ljust(6))):
        if p1 != p2:
            s += 1 / (p ** j)
    return s


def mkdecoder(pinset=pin.allpin, metric=pin_adic, N=256):
    """pinset= list of strings
    metric = string metric, function (x,y) -> float
    N = integer, positive, number of elements to generate
    """
    for (i, pin1) in enumerate(pinset):
        for (j, pin2) in enumerate(pinset):
            M[i, j] = metric(pin1, pin2)
    total = np.sum(M, 1)
    pasc = total.argsort()
    pdesc = list(np.flip(pasc))
    out = [pdesc[0]]
    while len(out) < N:
        ma = []
        for p2 in pdesc:
            s = 0
            ma.append(metric(pinset[out[-1]], pinset[p2]))
        maa = np.array(ma)
        jm = maa.argmax()
        out.append(pdesc[jm])
        pdesc.remove(pdesc[jm])

    codebook = {}
    for j, o in enumerate(out):
        codebook[pinset[o]] = j - 1
    return codebook
