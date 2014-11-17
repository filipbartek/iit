from iit.logic_gate import Or, And, Xor
from iit.mechanism import First
from iit.network import Node, Network


__author__ = 'Filip Bartek'


if __name__ == '__main__':
    A = Node(Or(), True, name='A')
    B = Node(And(), False, name='B')
    C = Node(Xor(), False, name='C')
    D = Node(First(), False, name='D')
    E = Node(First(), True, name='E')
    F = Node(First(), False, name='F')
    A.input_nodes = [B, C, D]
    B.input_nodes = [C, A]
    C.input_nodes = [A, B]
    D.input_nodes = [D]
    E.input_nodes = [B]
    F.input_nodes = [F]
    net = Network([A, B, C, D, E, F])
    for i in range(3):
        print "i: %d" % i
        for node in net.nodes:
            print "%s: %s" % (node, node.state)
        net.activate()
