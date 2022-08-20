import pinyinpimp


def bxor(b1, b2):
    out = 0
    for b1, b2 in zip(b1, b2):
        out = out + int(b1 ^ b2)
    return int(out)


b = pinyinpimp.uuidyin()
print(b.uuid())
print(b.uuid())
print(b.uuid())
print(b.uuid())


def testencdec(codec, baite=b"deadbeef666"):
    C = codec.encode(baite)
    print(C)
    E = codec.decode(C)
    print(E)
    print("error ", bxor(E, baite))


testencdec(pinyinpimp.daotepin())
testencdec(pinyinpimp.pinyindao())

c = pinyinpimp.pinyindao()
g = pinyinpimp.daotepin()

testencdec(c, b"\xde\xad\xbe\xef")
testencdec(g, b"\xde\xad\xbe\xef")

testencdec(c, b"a\xde\xad\xbe\xef")
testencdec(g, b"a\xde\xad\xbe\xef")

testencdec(
    g,
    "bi bi bi bi bi bi faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    c,
    "ji ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)

testencdec(
    g,
    "ji ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    g,
    "ji ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    g,
    "bi ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    g,
    "bi bi bi bi bi bi faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    c,
    "ji ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    c,
    "ji ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    c,
    "bi ji ji ji ji ji faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
testencdec(
    c,
    "bi bi bi bi bi bi faf fafaf afaf af af faf fafaf fafdfsdfsdfsdfsdfsd".encode(
        "utf-8"
    ),
)
