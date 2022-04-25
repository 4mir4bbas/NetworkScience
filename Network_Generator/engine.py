"""
    University of Tehran,
    Department of Algorithms and Computation
    Network Science Course
    Coded by: Amir Abbas Bakhshipour

    This is the implementation of the engine of various network generators.

"""

# %matplotlib inline
import math
import matplotlib.pyplot as plt


class Node:
    def __init__(self, label, deg=0, max_link=math.inf, adj_list=None):
        if adj_list is None:
            adj_list = list()
        self.label = label
        self.deg = deg
        self.max_link = max_link
        self.adj_list = adj_list

    def __repr__(self):
        return "Node #%s" % str(self.label)


class Network:
    def __init__(self, nnodes=0, node_dict=None, deg_counter=None, links=None, node_chance=None):
        if node_dict is None:
            node_dict = dict()
        if deg_counter is None:
            deg_counter = {0: nnodes}
        if links is None:
            links = []
        if node_chance is None:
            node_chance = []
        self.nnodes = nnodes
        self.node_dict = node_dict
        self.deg_counter = deg_counter
        self.links = links
        self.node_chance = node_chance
        if nnodes != 0:
            if len(node_dict) == 0:
                for i in range(1, nnodes+1):
                    self.node_dict[i] = Node(label=i)
        if len(self.links) != 0:
            for i in self.node_dict.keys():
                for j in range(self.node_dict[i].deg):
                    self.node_chance.append(i)
        self.max_deg_node = -1

    def add_node(self, node):
        self.nnodes = self.nnodes + 1
        self.node_dict[node.label] = node
        if 0 not in self.deg_counter.keys():
            self.deg_counter[0] = 1
        else:
            self.deg_counter[0] += 1

    def add_dir_link(self, node1, node2):
        # to be implemented
        pass

    def add_undir_link(self, node1, node2):
        self.node_chance.append(node1)
        self.node_chance.append(node2)
        if node2 not in self.node_dict[node1].adj_list:
            self.node_dict[node1].adj_list.append(node2)
            self.node_dict[node1].deg += 1
            self.links.append((node1, node2))
            if self.node_dict[node1].deg not in self.deg_counter.keys():
                self.deg_counter[self.node_dict[node1].deg] = 1
            else:
                self.deg_counter[self.node_dict[node1].deg] += 1
            self.deg_counter[self.node_dict[node1].deg-1] -= 1
        if node1 not in self.node_dict[node2].adj_list:
            self.node_dict[node2].adj_list.append(node1)
            self.node_dict[node2].deg += 1
            if self.node_dict[node2].deg not in self.deg_counter.keys():
                self.deg_counter[self.node_dict[node2].deg] = 1
            else:
                self.deg_counter[self.node_dict[node2].deg] += 1
            self.deg_counter[self.node_dict[node2].deg - 1] -= 1

    def plot(self, all_types=True, plt_type="two"):
        if all_types:
            fig, ax = plt.subplots(2, 2, figsize=(17,13))
            k = []
            pk = []
            sm = 0
            for i in self.deg_counter.keys():
                sm += self.deg_counter[i]
            for i in self.deg_counter.keys():
                if i != 0:
                    k.append(i)
                    pk.append(self.deg_counter[i]/sm)
            kpk = []
            for i in range(len(k)):
                kpk.append((k[i], pk[i]))
            kpk.sort()
            ax[0, 0].scatter(k, pk)
            ax[0, 0].set_title('Linear Scale')
            ax[0, 0].set_xlabel('k')
            ax[0, 0].set_ylabel('$p_{k}$')
            ax[0, 1].set_title('Log Scale (linear binning)')
            ax[0, 1].set_xlabel('k')
            ax[0, 1].set_ylabel('$p_{k}$')
            ax[1, 0].set_title('Log Scale (log binning)')
            ax[1, 0].set_xlabel('k')
            ax[1, 0].set_ylabel('$p_{k}$')
            ax[1, 1].set_title('Cumulative')
            ax[1, 1].set_xlabel('k')
            ax[1, 1].set_ylabel('$p_{k}$')
            ax[0, 1].set_xscale('log')
            ax[0, 1].set_yscale('log')
            ax[1, 1].set_xscale('log')
            ax[1, 1].set_yscale('log')
            ax[1, 0].set_xscale('log')
            ax[1, 0].set_yscale('log')
            ax[0, 1].scatter(k, pk)
            maxk = max(k)
            newk = []
            newpk = []
            for m in range(0, int(math.sqrt(maxk))+1):
                newk.append((2**m+2**(m+1))/2)
                newpk.append(0)
                for l in range(len(kpk)):
                    if kpk[l][0] >= 2**m and kpk[l][0] <= 2**(m+1):
                        newpk[-1] += kpk[l][1]
                    elif kpk[l][0] > 2**(m+1):
                        break
            ax[1, 0].scatter(newk, newpk)
            cumpk = []
            for i in range(len(kpk)):
                cumpk.append(0)
                for j in range(i,len(kpk)):
                    cumpk[-1] += kpk[j][1]
            ax[1, 1].scatter(k, cumpk)
            return

        else:
            fig, ax = plt.subplots(figsize=(10, 7))
            k = []
            pk = []
            sm = 0
            for i in self.deg_counter.keys():
                sm += self.deg_counter[i]
            for i in self.deg_counter.keys():
                if i != 0:
                    k.append(i)
                    pk.append(self.deg_counter[i]/sm)
            kpk = []
            for i in range(len(k)):
                kpk.append((k[i], pk[i]))
            kpk.sort()
            if plt_type == "one":
                pass
            elif plt_type == "two":
                ax.set_xscale('log')
                ax.set_yscale('log')
            elif plt_type == "three":
                ax.set_xscale('log')
                ax.set_yscale('log')
                maxk = max(k)
                newk = []
                newpk = []
                for m in range(0, int(math.sqrt(maxk))+1):
                    newk.append((2**m+2**(m+1))/2)
                    newpk.append(0)
                    for l in range(len(kpk)):
                        if kpk[l][0] >= 2**m and kpk[l][0] <= 2**(m+1):
                            newpk[-1] += kpk[l][1]
                        elif kpk[l][0] > 2**(m+1):
                            break
            elif plt_type == "four":
                ax.set_xscale('log')
                ax.set_yscale('log')
                cumpk = []
                for i in range(len(kpk)):
                    cumpk.append(0)
                    for j in range(i,len(kpk)):
                        cumpk[-1] += kpk[j][1]

            if plt_type == "one" or plt_type == "two":
                ax.scatter(k, pk)
            if plt_type == "three":
                ax.scatter(newk, newpk)
            if plt_type == "four":
                ax.scatter(k, cumpk)
            return
