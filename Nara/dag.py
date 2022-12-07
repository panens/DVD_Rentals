import networkx as nx 
from matplotlib import pyplot as plt

entire_graph = nx.DiGraph() #creates an empty DiGraph object

entire_graph.add_edges_from([("Connect","Create Dim Tables"),("Create Agg Table","Delete Tables"),("Create Dim Tables","Create Agg Table"),("Create Agg Table","Disconnect"),("Connect","Delete Tables"),("Delete Tables","Disconnect")])

def visualize_dag(nodes_and_edges,name): #function that creates dag visualization
    '''Creates a visualization of a DAG and saves it
    Args:
        nodes_and_edges (list): a list of all edges from which the nodes are inferred
        name (str): name of how the file should be saved
    '''
    plt.figure()
    nx.draw_networkx(nodes_and_edges, arrows = True, with_labels = True)
    plt.savefig(f'DAGs/{name}.png', format="png")
    plt.clf()

visualize_dag(entire_graph, "entire_dag") #creates entire dag
