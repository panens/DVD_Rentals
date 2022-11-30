import networkx as nx 
from matplotlib import pyplot as plt

creation_graph = nx.DiGraph()
deletion_graph = nx.DiGraph()
creation_graph_numbers = nx.DiGraph()

creation_graph.add_edges_from([("Connect","Create Dim Tables"),("Create Dim Tables","Create Agg Table"),("Create Agg Table","Disconnect")])
deletion_graph.add_edges_from([("Connect","Delete Tables"),("Delete Tables","Disconnect")])

def visualize_dag1():
    plt.figure()
    nx.draw_networkx(creation_graph, arrows = True, with_labels = True)
    plt.savefig('DAGs/creation_dag.png', format="png")
    plt.clf()

def visualize_dag2():
    plt.figure()
    nx.draw_networkx(deletion_graph, arrows = True, with_labels = True)
    plt.savefig('DAGs/deletion_dag.png', format="png")
    plt.clf()

