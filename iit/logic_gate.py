from iit.mechanism import Mechanism

import numpy


__author__ = 'Filip Bartek'


class LogicGate(Mechanism):
    pass


class And(LogicGate):
    def activate(self, input):
        input = numpy.array(input, dtype=numpy.bool)
        return numpy.bool(numpy.prod(input))


class Or(LogicGate):
    def activate(self, input):
        input = numpy.array(input, dtype=numpy.bool)
        return numpy.bool(numpy.sum(input))


class Xor(LogicGate):
    def activate(self, input):
        input = numpy.array(input, dtype=numpy.bool)
        s = numpy.sum(input)
        return s % 2 != 0


class Nand(LogicGate):
    def activate(self, input):
        input = numpy.array(input, dtype=numpy.bool)
        return not numpy.bool(numpy.prod(input))


class Nor(LogicGate):
    def activate(self, input):
        input = numpy.array(input, dtype=numpy.bool)
        return not numpy.bool(numpy.sum(input))
