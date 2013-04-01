#!/usr/bin/env python
#-*- coding: utf-8-*-

# [SNIPPET_NAME: GConf: get/set values]
# [SNIPPET_CATEGORIES: PyGTK] 
# [SNIPPET_DESCRIPTION: Demonstrates getting and setting values using GConf]
# [SNIPPET_AUTHOR: Florian Diesch <diesch@spamfence.net>]
# [SNIPPET_DOCS: http://library.gnome.org/devel/gconf/stable/]
# [SNIPPET_LICENSE: MIT]

# Copyright 2010 Florian Diesch <diesch@spamfence.net>
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


import gconf

my_gconf_dir='/just-testing'  # a namespace in GConf for our tests


gclient = gconf.client_get_default()  # create a client object


## set a string value
gvalue = gconf.Value(gconf.VALUE_STRING)
gvalue.set_string('A string value')
gclient.set(my_gconf_dir+'/some_string', gvalue)

## get a string value
gvalue = gclient.get(my_gconf_dir+'/some_string')
print "Some string:", gvalue.get_string()


## set an int value
gvalue = gconf.Value(gconf.VALUE_INT)
gvalue.set_int(23)
gclient.set(my_gconf_dir+'/some_int', gvalue)

## get an int value
gvalue = gclient.get(my_gconf_dir+'/some_int')
print "Some int:", gvalue.get_int()


## set a pair value
gvalue = gconf.Value(gconf.VALUE_PAIR)
car = gconf.Value(gconf.VALUE_STRING)
car.set_string('First value')
gvalue.set_car(car)

cdr = gconf.Value(gconf.VALUE_BOOL)
cdr.set_bool(True)
gvalue.set_cdr(cdr)

gclient.set(my_gconf_dir+'/some_pair', gvalue)

## get a pair value
gvalue = gclient.get(my_gconf_dir+'/some_pair')
print "Some pair:", gvalue.get_car().get_string(), gvalue.get_cdr().get_bool()



## set a list value
gvalue = gconf.Value(gconf.VALUE_LIST)
gvalue.set_list_type(gconf.VALUE_FLOAT)
l = []
for i in range(5):
    gv = gconf.Value(gconf.VALUE_FLOAT)
    gv.set_float(i/2.0)
    l.append(gv)
gvalue.set_list(l)

gclient.set(my_gconf_dir+'/some_list', gvalue)

## get a list value
gvalue = gclient.get(my_gconf_dir+'/some_list')
print "Some list:", [gv.get_float() for gv in gvalue.get_list()]



    
## unset values
for val in ('some_string', 'some_int', 'some_pair', 'some_list'):
  gclient.unset('%s/%s'%(my_gconf_dir, val))

## Tell GConfd that's now a good time for syncing
gclient.suggest_sync()

