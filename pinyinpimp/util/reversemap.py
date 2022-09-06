import numpy as np
import pinyin

hit = np.array(list(pinyin.pinyin.pinyin_dict.items()))
zhongren = [[a[0], a[1]] for a in hit]
zhongaa = np.array(zhongren)
tones = pinyin.pinyin.pinyin_tone

yinbin = {}
for d in zhongaa:
    if len(yinbin.get(d[1], [])) == 0:
        yinbin[d[1]] = [d[0]]
    else:
        yinbin[d[1]].append(d[0])


def reverseUCODE(fourhex):
    try:
        out = pinyin.pinyin.unicodedata.ucd_3_2_0.lookup(
            "CJK UNIFIED IDEOGRAPH-" + (fourhex)
        )
    except:
        out = pinyin.pinyin.unicodedata.ucd_3_2_0.lookup(
            "CJK COMPATIBILITY IDEOGRAPH-" + (fourhex)
        )
    return out


def pin2chin(pin, choose=0):
    """pin is a string, single pinyin phoneme on ascii, no accents, output is chinese char from thegive it the number(index of the one u want, 'rand', or tone1-tone5 to choose that tone, as this is a one to many mapping"""
    if type(choose) is str:
        n = len(yinbin[pin.lower()])
        if "rand" in choose:
            return reverseUCODE(yinbin[pin.lower()][np.random.randint(n)])
        elif "tone" in choose.lower():
            out = ""
            tnum = int(choose.lower()[-1]) % 5 + 1
            for j in range(n):
                if tones[yinbin[pin.lower()][j]] == tnum:
                    out = reverseUCODE(yinbin[pin.lower()][j])
            if len(out) == 0:
                out = reverseUCODE(yinbin[pin.lower()][np.random.randint(n)])
            return out

        else:
            raise NotImplementedError("wat")
    else:
        return reverseUCODE(yinbin[pin.lower()][choose])
