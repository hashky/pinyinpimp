import numpy as np

# import matplotlib.pyplot as plt
from .. import data as pin

n = len(pin.allpin)
M = np.zeros((n, n))

def sord(p) -> int:
    return ord(p.lower())-96
def sordm(p1,p2):
    return np.abs(sord(p1)-sord(p2))
def pin_adic(pin1, pin2, p=29, n=6,dmetrik=sordm):
    """specialized function for computing p-adic based ultrametric between objects composed of at most p-1 distinct elements of maximum length n with provided metric dmetrik (any,any) -> float. p must be prime,"""
    s = 0
    for j, (p1, p2) in enumerate(zip(pin1.ljust(n), pin2.ljust(n))):
        if p1 != p2:
            s = dmetrik(p1,p2)/ (p ** j)
            return s
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
    while len(out) < N+1:
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
