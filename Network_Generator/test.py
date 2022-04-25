from engine import *
from random import random, choice
# import seaborn as sns

nnodes = 10000
sat = 50
initial_nodes = {
    1: Node(1, 2, adj_list=[2,4]),
    2: Node(2, 2, adj_list=[1,3]),
    3: Node(3, 2, adj_list=[2,4]),
    4: Node(4, 2, adj_list=[1,3])
}
initial_deg = {
    2: 4
}
initial_links = [(1,2), (2,3), (3,4), (1,4)]
p = 0.1
net = Network(nnodes=4,node_dict=initial_nodes,deg_counter=initial_deg,links=initial_links)

# for i in range(5, nnodes+1):
#     net.add_node(Node(i))
#     rnd = random()
#     if rnd < p:
#         chosen_node = choice([j for j in range(1,net.nnodes+1)])
#         net.add_undir_link(chosen_node, i)
#     else:
#         chosen_link = choice(net.links)
#         net.add_undir_link(chosen_link[0], i)

for i in range(5, nnodes+1):
    net.add_node(Node(i))
    chosen = choice(net.node_chance)
    # saturation model
#     while net.node_dict[chosen].deg > sat:
#         chosen = choice(net.node_chance)
    net.add_undir_link(chosen, i)


net.plot()
# net.plot(False, plt_type="one")
# net.plot(False, plt_type="two")
# net.plot(False, plt_type="three")
# net.plot(False, plt_type="four")

