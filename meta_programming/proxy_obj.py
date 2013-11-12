#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_proxy(obj):
    class Proxy(object):
        def __getattr__(self, name):
            return getattr(obj, name)
        def __setattr__(self, name, value):
            setattr(obj, name, value)
        def __delattr__(self, name):
            delattr(obj, name)
    return Proxy()