from abc import ABCMeta, abstractmethod
from datetime import datetime


class ApiInterface(object):
    """ Define the interface that all implementations of the interface must implement """

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_provider_lots(self, urls):
        pass

    @abstractmethod
    def fetch_rates(self, master_dict):
        pass


class BaseAPI(object):
    """ A common parent class that contains utility functions and initalizes variables """

    assumptions = {
        'prefix': '',
        'postfix': ''
    }

    def __init__(self):
        self.lots = {}
        self.start_time = datetime.now()


class MyAPI(BaseAPI, ApiInterface):
    """ A specific implementation of the parent class that implements the interface
    It will not let you instantiate the class if you have not implemented all abstract methods
    """
    def get_provider_lots(self, urls):
        provider_lots = list()
        return provider_lots

    def fetch_rates(self, master_dict):
        rates = list()
        return rates


myapi = MyAPI()
print(vars(myapi))
print(dir(myapi))
