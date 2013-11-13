# prepare two auxiliary tables tables (using a function, for speed),
# then remove the function, since it's not needed any more:
CRCTableh = [0] * 256
CRCTablel = [0] * 256
def _inittables(CRCTableh, CRCTablel, POLY64REVh, BIT_TOGGLE):
    for i in xrange(256):
        partl = i
        parth = 0L
        for j in xrange(8):
            rflag = partl & 1L
            partl >>= 1L
            if parth & 1:
                partl ^= BIT_TOGGLE
            parth >>= 1L
            if rflag:
                parth ^= POLY64REVh
        CRCTableh[i] = parth
        CRCTablel[i] = partl
# first 32 bits of generator polynomial for CRC64 (the 32 lower bits are
# assumed to be zero) and bit-toggle mask used in _inittables
POLY64REVh = 0xd8000000L
BIT_TOGGLE = 1L << 31L
# run the function to prepare the tables
_inittables(CRCTableh, CRCTablel, POLY64REVh, BIT_TOGGLE)
# remove all names we don't need any more, including the function
del _inittables, POLY64REVh, BIT_TOGGLE
# this module exposes the following two functions: crc64, crc64digest
def crc64(bytes, (crch, crcl)=(0,0)):
    for byte in bytes:
        shr = (crch & 0xFF) << 24
        temp1h = crch >> 8L
        temp1l = (crcl >> 8L) | shr
        tableindex = (crcl ^ ord(byte)) & 0xFF
        crch = temp1h ^ CRCTableh[tableindex]
        crcl = temp1l ^ CRCTablel[tableindex]
    return crch, crcl
def crc64digest(aString):
    return "%08X%08X" % (crc64(bytes))
if __name__ == '__main__':
    # a little test/demo, for when this module runs as main-script
    assert crc64("IHATEMATH") == (3822890454, 2600578513)
    assert crc64digest("IHATEMATH") == "E3DCADD69B01ADD1"
    print 'crc64: dumb test successful'
