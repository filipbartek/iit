import abc


__author__ = 'Filip Bartek'


class Mechanism(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def activate(self, input):
        """
        Return the next state according to input
        :param input: 
        :return:
        """
        raise NotImplementedError('Abstract')


class Const(Mechanism):
    def __init__(self, value):
        self.value = value
        pass
    
    def activate(self, input=None):
        return self.value


class First(Mechanism):
    def activate(self, input):
        return input[0]
