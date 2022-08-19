from . import data
from . import codec
from . import util
import uuid
from hashlib import sha256


class uuidyin:
    """arguments are an instantiation of pinyin codec, uuid generating function(attribute .bytes is accessedin the object a blind call to the function returns, so you can pass it anything that returns a class wth an attribute bytes that returns a  byte array. """

    def __init__(self, codec=codec.binyin(), uuid=uuid.uuid1, p_mod=16):
        self.p_mod = p_mod
        self.binyin = codec
        self.uuidX = uuid

    def tobinyin(self, sumbytes):
        return self.binyin.encode(sumbytes)

    def uuid(self):
        bytesid = self.uuidX().bytes
        pinlist = self.tobinyin(bytesid)
        out = ""
        shasa = sha256()
        shasa.update(bytesid)
        shadig = shasa.digest()
        for j, p in enumerate(pinlist):
            out = out + p
            if j < (len(pinlist) - 1):
                out = out + str(int(shadig[j] % self.p_mod))
        return out


class pinyindao:
    """this is a neumonic encoding that consists of pinyin values and numbers between 1 and 5 that are a checksum of the underlying data, making this an error correcting and detecting encoding. a partial of the string can be used to reconstruct the whole, or a space of candidates thereof, by cracking the hash to fill in what remains"""

    def __init__(self, codec=codec.binyin(), p_mod=5):
        self.binyin = codec
        self.p_mod = p_mod

    def tobinyin(self, sumbytes):
        return self.binyin.encode(sumbytes)

    def decode(self, pinjin):
        # pinjin = piinyin(yinpin)
        pa = pinjin.translate(pinjin.maketrans("123456789", " " * 9)).split(" ")
        out = self.binyin.decode(pa[0 : len(pa) - 1])
        return out

    def encode(self, bytesid):
        hsize = 32  # bytes
        pinlist = self.tobinyin(bytesid)
        out = ""
        shasa = sha256()
        Nbin = len(bytesid)
        Nch = int(Nbin / hsize) + 1
        hashl = []
        p_mod = self.p_mod  # for tones
        for j in range(0, Nch):
            shasa.update(bytesid[j * hsize : min((j + 1) * hsize, Nbin % hsize)])
            hashl.append(shasa.digest())
        for j, p in enumerate(pinlist):
            out = out + p
            out = out + str((int(hashl[int(j / 32)][j % 32] % p_mod) + 1))
        return out


# here properly over-ride abve with decorators
class daotepin(pinyindao):
    """This is class framework for creating codecs to encode pinyin from pinyindao into chinese chars sequence"""

    def __init__(self, codec=codec.binyin()):
        super().__init__(codec=codec, p_mod=5)

    def decode(self, yinpin):
        _out = ""
        yinhuoli = super().decode(util.pinyin.get(yinpin, format="numerical"))
        return yinhuoli

    def encode(self, inpt):
        chipindao = super().encode(inpt)
        digits_single = chipindao.maketrans("123456789", " " * 9)
        alphabet = chipindao.maketrans("abcdefghijklmnopqrstuvwxyz", " " * 26)
        tonez = (
            chipindao.translate(alphabet)
            .replace("  ", " ")
            .replace("  ", " ")
            .replace("  ", " ")
            .replace("  ", " ")
            .replace("  ", " ")
            .strip(" ")
            .split(" ")
        )
        pinpowping = (
            chipindao.translate(digits_single)
            .replace("  ", " ")
            .replace("  ", " ")
            .strip(" ")
            .split(" ")
        )

        # brak up on the numbers(tokenize)
        # separate the tones and use in lookup
        out = ""
        for j in range(len(pinpowping)):
            out = out + util.pin2chin(pinpowping[j], "tone" + str(tonez[j]))
        return out
