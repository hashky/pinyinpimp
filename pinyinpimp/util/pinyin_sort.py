import numpy as np

# import matplotlib.pyplot as plt
from .. import data as pin

n = len(pin.allpin)
M = np.zeros((n, n))


def sord(p) -> int:
    return ord(p.lower()) - 96


def sordm(p1, p2):
    return np.abs(sord(p1) - sord(p2))


def pin_adic(pin1, pin2, p=29, n=6, metric=sordm):
    """specialized function for computing p-adic based ultrametric between objects composed of at most p-1 distinct elements of maximum length n with provided metric metric (any,any) -> float. p must be prime,"""
    j = 0
    s = 0
    for (p1, p2) in zip(pin1.ljust(n), pin2.ljust(n)):
        j += 1
        if p1 != p2:
            s = s + metric(p1, p2) / (p ** j)
            return s
        return float(s)


def hamdist(str1, str2):
    """weighted hamming distance between two strings, aligned left to right in the conventional manner. case differences account for half of a 'change' and numbers are weighted as 1/10th of an 'edit'. the standard hamming distance is an ultrametric, and simply computed by couunting the number of positions that are not the same. for a set of strings of variable length, this is not uniquely determined without a declared deterministic method of aligning the strings. """
    numz = [str(a) for a in range(10)]
    diffs = abs(len(str1) - len(str2))
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            if ch1 in numz and ch2 in numz:
                diffs += 0.1
            else:
                diffs += 0.5
                if ch1.lower() != ch2.lower():
                    diffs += 0.5

    return diffs


def nhamdist(str1, str2):
    """above hamming distance weighed by length of the strings, IE, normalized, so that it can be used to compare strings of nonequal length"""
    n = max(len(str1), len(str2))
    return hamdist(str1, str2) / n


def mk_distance_matrix(pinset=pin.allpin, metric=nhamdist, N=25):
    """pinset= list of strings
    metric = string metric, function (x,y) -> float
    N = integer, positive, number of elements to generate
    returns distance matrix
    """
    NN = len(pinset)
    M = np.zeros((NN, NN))
    for (i, pin1) in enumerate(pinset):
        for (j, pin2) in enumerate(pinset):
            M[i, j] = metric(pin1, pin2)
    return M


def mkdecoder(pinset=pin.allpin, metric=pin_adic, N=256):
    """pinset= list of strings
    metric = string metric, function (x,y) -> float
    N = integer, positive, number of elements to generate
    """
    M = mk_distance_matrix(pinset, metric, N)
    total = np.sum(M, 1)
    pasc = total.argsort()
    pdesc = list(np.flip(pasc))
    out = [pdesc[0]]
    while len(out) < N + 1:
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
