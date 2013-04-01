"""
color class
"""

class color(object):

    def __init__(self, r, g, b, a=None):
        assert 0 <= r <= 1, "Red must be in range 0-1 (%r)" % r
        assert 0 <= g <= 1, "Green must be in range 0-1 (%r)" % g
        assert 0 <= b <= 1, "Blue must be in range 0-1 (%r)" % b
        assert a is None or 0 <= a <= 1, "Transparency (alpha) must be in range 0-1 (%r)" % a
        self._r = r
        self._g = g
        self._b = b
        self._a = a
        self._v = None

    def fromhex(cls, hex):
        if hex.startswith('#'):
            hex = hex[1:]
        if len(hex) == 3:
            r, g, b = hex
            a = None
            range = 16.
        elif len(hex) == 4:
            r, g, b, a = hex
            range = 16.
        elif len(hex) == 6:
            r, g, b = hex[0:2], hex[2:4], hex[4:6]
            a = None
            range = 255.
        elif len(hex) == 8:
            r, g, b, a = hex[0:2], hex[2:4], hex[4:6], hex[6:8]
            range = 255.
        elif len(hex) == 12:
            r, g, b = hex[0:4], hex[4:8], hex[8:12]
            a = None
            range = 65025.
        elif len(hex) == 16:
            r, g, b, a = hex[0:4], hex[4:8], hex[8:12], hex[12:16]
            range = 65025.
        else:
            raise ValueError, 'Hex codes should be of length 3, 6, or 12; you gave: %r' % hex
        if a is not None:
            a = int(a, 16)/range
        return cls(int(r, 16)/range,
                   int(g, 16)/range,
                   int(b, 16)/range,
                   a)
    fromhex = classmethod(fromhex)

    def fromhsv(cls, h, s, v, a=None):
        # from http://www.cs.rit.edu/~ncs/color/t_convert.html
        assert 0 <= h <= 360, "Hue must be in range 0-360 (%r)" % h
        assert 0 <= s <= 1, "Saturation must be in range 0-1 (%r)" % s
        assert 0 <= v <= 1, "Value must be in range 0-1 (%r)" % v
        if not s:
            r = g = b = v
        else:
            sector = (h / 60.0) % 6.0 # 0 to 5
            i = int(sector)
            f = sector - i # factorial part of sector
            p = v * (1 - s)
            q = v * (1 - s * f)
            t = v * (1 - s * (1 - f))
            if i == 0:
                r, g, b = v, t, p
            elif i == 1:
                r, g, b = q, v, p
            elif i == 2:
                r, g, b = p, v, t
            elif i == 3:
                r, g, b = p, q, v
            elif i == 4:
                r, g, b = t, p, v
            else:
                r, g, b = v, p, q
        return cls(r, g, b, a)
    fromhsv = classmethod(fromhsv)

    def fromname(cls, name, a=None):
        if name.startswith('#'):
            return cls.fromhex(name[1:])
        if not _colornames:
            _loadColornames()
        if not _colornames.has_key(name):
            raise ValueError, "I do not know any color by the name %r" % name
        r, g, b = _colornames[name]
        return cls(r, g, b, a)
    fromname = classmethod(fromname)

    def _get_red(self): return self._r
    red = property(_get_red)

    def _get_green(self): return self._g
    green = property(_get_green)

    def _get_blue(self): return self._b
    blue = property(_get_blue)

    def _get_alpha(self):
        return self._a or 0
    alpha = property(_get_alpha)

    def websafe(self):
        return self.__class__(self._webSafeComponent(self.r),
                              self._webSafeComponent(self.g),
                              self._webSafeComponent(self.b))

    def _webSafeComponent(self, color):
        return round(color*5)/5

    def _genHSV(self):
        maxVal = max(self._r, self._g, self._b)
        minVal = min(self._r, self._g, self._b)
        delta = maxVal - minVal
        self._v = maxVal
        if maxVal != 0:
            self._s = delta / maxVal
        else:
            self._s = 0
        if not self._s:
            self._h = None
        else:
            if self._r == maxVal:
                self._h = (self._g - self._b)*255 / delta
            elif self._g == max:
                self._h = 2 + (self._b - self._r)*255 / delta
            else:
                self._h = 4 + (self._r - self._g)*255 / delta
        if self._h > 360:
            self._h -= 360
        elif self._h < 0:
            self._h += 360

    def _get_hue(self):
        if self._v is None:
            self._genHSV()
        return self._h
    hue = property(_get_hue)

    def _get_saturation(self):
        if self._v is None:
            self._genHSV()
        return self._s
    saturation = property(_get_saturation)

    def _get_value(self):
        if self._v is None:
            self._genHSV()
        return self._v
    value = property(_get_value)

    def __repr__(self):
        if self._a is None:
            return 'color(%r, %r, %r)' % (self._r, self._g, self._b)
        else:
            return 'color(%r, %r, %r, %r)' \
                   % (self._r, self._g, self._b, self._a)


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (
            self.red == other.red
            and self.blue == other.blue
            and self.green == other.green
            and self.alpha == other.alpha)

_colornames = {}
_colornameFilename = '/usr/lib/X11/rgb.txt'

def _loadColornames():
    f = open(_colornameFilename)
    for line in f:
        if line.startswith('!'):
            continue
        line = line.strip()
        if not line:
            continue
        r, g, b, n = line.split(None, 3)
        _colornames[n] = int(r)/255.0, int(g)/255.0, int(b)/255.0


if __name__ == '__main__':
    c1 = color(1, 0, 0)
    c2 = color.fromname('red')
    c3 = color.fromname('#ff0000')
    c4 = color.fromhex('ff0000')
    c5 = color.fromhsv(0, 1, 1)
    assert c1 == c2 == c3 == c4 == c5
    assert (color(0, 1, 0)
            == color.fromname('green')
            == color.fromhex('#00ff00')
            == color.fromhsv(120, 1, 1))

