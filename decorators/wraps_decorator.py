#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps


def my_decorator(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        print('calling wrapper')
        if request.get('some_data'):
            request['user'] = 'brent'
        return view_func(request, *args, **kwargs)
    return wrapper


@my_decorator
def example(request):
    """ Docstring """
    print('calling example function')
    print(request)

if __name__ == '__main__':
    request = dict(some_data='has_value')
    example(request)
