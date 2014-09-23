#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import datetime


class Affiliate(object):
    """ Prototype Class. All common attributes/interface here """
    __metaclass__ = abc.ABCMeta

    date_format = ''
    user_format = ''

    def add_date(self, date, url):
        return url + '?' + date.strftime(self.date_format)


class ParkWhiz(Affiliate):
    date_format = '%Y-%m-%d %H:%m:%S.%z'


class ParkingPanda(Affiliate):
    date_format = '%Y-%m-%d %H:%m:%S.%z'


class SpotHero(Affiliate):
    date_format = '%Y-%m-%d %H:%m:%S.%z'


class AffiliateFactory(object):

    affiliate_objects = dict()
    for x in Affiliate.__subclasses__():
        affiliate_objects[x.__name__.lower()] = x

    def get_affiliate(self, typ):
        return self.affiliate_objects[typ]()

affiliate_obj = AffiliateFactory()
affiliates = ['parkwhiz', 'parkingpanda', 'spothero']
for b in affiliates:
    but = affiliate_obj.get_affiliate(b)
    now = datetime.datetime.now()
    print but.add_date(now, 'http://www.example.com/')
    
for x in Affiliate.__subclasses__():
    print x.__name__.lower()