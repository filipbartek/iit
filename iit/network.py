from iit.mechanism import Mechanism


__author__ = 'Filip Bartek'


class Node(object):
    def __init__(self, mechanism=None, state=None, name=None, input_nodes=[]):
        self.mechanism = mechanism
        self.state = state
        self.name = name
        self.input_nodes = input_nodes
        pass
    
    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return super(object, self).__str__()
    
    @property
    def input_nodes(self):
        return self._input_nodes
    
    @input_nodes.setter
    def input_nodes(self, input_nodes):
        assert type(input_nodes) is list # TODO: Generalize to iterables
        for node in input_nodes:
            assert type(node) is Node
        self._input_nodes = input_nodes
        pass
    
    def activate(self):
        if self.mechanism is None:
            # Default behavior: keep previous state
            # TODO: Reconsider this behavior
            return self.state
        assert self.input_nodes is not None
        input_vector = []
        for node in self.input_nodes:
            input_vector.append(node.state)
        assert isinstance(self.mechanism, Mechanism)
        return self.mechanism.activate(input_vector)


class Network(object):
    def __init__(self, nodes):
        assert type(nodes) is list
        for node in nodes:
            assert type(node) is Node
        self.nodes = nodes
        pass
    
    def activate(self):
        states = {}
        for node in self.nodes:
            states[node] = node.activate()
        for node, state in states.iteritems():
            node.state = state
        pass
    
    @property
    def state(self):
        states = {}
        for node in self.nodes:
            states[node] = node.state
        return states
    
    @state.setter
    def state(self, states):
        for node, state in states.iteritems():
            assert node in self.nodes
            node.state = state
        pass
