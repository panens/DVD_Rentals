import networkx as nx 
from matplotlib import pyplot as plt

creation_graph = nx.DiGraph() #creates an empty DiGraph object
deletion_graph = nx.DiGraph() #creates an empty DiGraph object
entire_graph = nx.DiGraph() #creates an empty DiGraph object

#By adding edges, the nodes are added as well. 
#There are 2 different activities - creating tables or deleting tables that one can do with the project. 

creation_graph.add_edges_from([("Connect","Create Dim Tables"),("Create Dim Tables","Create Agg Table"),("Create Agg Table","Disconnect")]) 
deletion_graph.add_edges_from([("Connect","Delete Tables"),("Delete Tables","Disconnect")])
entire_graph.add_edges_from([("Connect","Create Dim Tables"),("Create Agg Table","Delete Tables"),("Create Dim Tables","Create Agg Table"),("Create Agg Table","Disconnect"),("Connect","Delete Tables"),("Delete Tables","Disconnect")])

def visualize_dag1(): #function that creates dag visualization
    plt.figure()
    nx.draw_networkx(creation_graph, arrows = True, with_labels = True)
    plt.savefig('DAGs/creation_dag.png', format="png")
    plt.clf()

def visualize_dag2():
    plt.figure()
    nx.draw_networkx(deletion_graph, arrows = True, with_labels = True)
    plt.savefig('DAGs/deletion_dag.png', format="png")
    plt.clf()

def visualize_dag3():
    plt.figure()
    nx.draw_networkx(entire_graph, arrows = True, with_labels = True)
    plt.savefig('DAGs/entire_dag.png', format="png")
    plt.clf()