import codecs
from ..util import mkdecoder

pin256 = mkdecoder()


class binyin(codecs.Codec):
    """defines a class of codecs for encoding bytes in list(str) as pinyin phonemes. the default supplied code table is 256 pinyin of various lengths hierarchically ordered to spread them out in an ultrametric space formed by a string metric combined with the set of candidate strings
    encode: bytes -> list(str)
    decode: list(str) -> bytes"""

    def __init__(self, codemap=pin256):
        """table is a 256 element tupple
        to map a byte numeric value(as theindex of the tupple to one of these
        items, the reverse isd constructed automatically below"""
        self.table = codemap
        self.encoding_table = codecs.make_encoding_map(self.table)

    def encode(self, inpt, errors="strict"):
        """input is bytes or iterable with elements castable as of 0-256 ints, output is list of pinyin"""
        out = []
        for a in list(inpt):
            out = out + [self.encoding_table[a]]
        return out

    def decode(self, inpt, errors="strict"):
        out = b""
        for i, a in enumerate(inpt):
            out = out + self.table.get(a, 0).to_bytes(1, "big")
        return out
