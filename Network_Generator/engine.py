"""
    University of Tehran,
    Department of Algorithms and Computation
    Network Science Course
    Coded by: Amir Abbas Bakhshipour

    This is the implementation of the engine of various network generators.

"""


class Node:
    def __init__(self, label, adj_list=[]):
        self.label = label
        self.adj_list = adj_list


class Network:
    def __init__(self, nnodes=0, node_list=[]):
        self.nnodes = nnodes
        if nnodes != 0:
            if len(node_list) == 0:
                tmp = []
                for i in range(1, nnodes+1):
                    tmp.append(Node(i))
                self.node_list = tmp
            else:
                self.node_list = node_list
        else:
            self.node_list = node_list

    def add_node(self, node):
        self.nnodes = self.nnodes + 1
        self.node_list.append(node)

    def add_dir_link(self, node1, node2):
        try:
            for i in range(self.nnodes):
                if self.node_list[i].label == node1:
                    self.node_list[i].adj_list.append(node2)
                else:
                    print("There is no such node with label %s in the network" % str(node1.label))
        except:
            print("There is no such node with label %s or %s in the network" % (str(node1.label), str(node2.label)))

    def add_undir_link(self, node1, node2):
        try:
            for i in range(self.nnodes):
                if self.node_list[i].label == node1:
                    self.node_list[i].adj_list.append(node2)
                else:
                    print("There is no such node with label %s in the network" % str(node1.label))
            for i in range(self.nnodes):
                if self.node_list[i].label == node2:
                    self.node_list[i].adj_list.append(node1)
                else:
                    print("There is no such node with label %s in the network" % str(node2.label))
        except:
            print("there is no such node with label %s or %s in the network" % (str(node1.label), str(node2.label)))


