#!/usr/bin/env python
# -*- coding: utf-8 -*-

#! /usr/bin/python

import unittest
from mock import Mock, MagicMock
from itertools import chain


def trigger_handlers(top_level):
    ctx = {}
    for event in chain([top_level], top_level.extra):
        if event.handler:
            ctx.update({'event': event})
            event.handler.trigger(ctx)


class TestNestedCalls(unittest.TestCase):

    def test_top_level(self):
        top_level = MagicMock()
        top_level.extra = []

        trigger_handlers(top_level)

        ctx = {'event': top_level}
        top_level.handler.trigger.assert_called_once_with(ctx)

    def test_extra(self):
        top_level = MagicMock()
        top_level.handler = None
        nested = Mock()
        top_level.extra = [nested]

        trigger_handlers(top_level)

        ctx = {'event': nested}
        nested.handler.trigger.assert_called_once_with(ctx)

    def test_top_level_and_extra(self):
        top_level = MagicMock()
        nested = Mock()
        top_level.extra = [nested]

        trigger_handlers(top_level)

        print
        print "Mock: top_level: {0}".format(top_level)
        print "Call Args, top_level.handler.trigger: {0}".format(top_level.handler.trigger.call_args_list)
        print "Mock: nested: {0}".format(nested)
        print "Call Args, nested.handler.trigger: {0}".format(nested.handler.trigger.call_args_list)
        print

        ctx = {'event': top_level}
        top_level.handler.trigger.assert_called_once_with(ctx)

        ctx = {'event': nested}
        nested.handler.trigger.assert_called_once_with(ctx)


if __name__ == '__main__':
    unittest.main()
