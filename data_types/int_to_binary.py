#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(int_to_binary):
    x = '{0:08b}'.format(int_to_binary)
    if int_to_binary == 6:
        assert(x == '00000110')
    return x


def main_other(int_to_binary):
    bin8 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(8)]))
    x = bin8(6)
    if int_to_binary == 6:
        assert(x == '00000110')
    return x

if __name__ == '__main__':
    main(6)
    main_other(6)
