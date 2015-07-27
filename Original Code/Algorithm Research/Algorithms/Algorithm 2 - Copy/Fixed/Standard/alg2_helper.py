import networkx as nx
import random, sys

class alg2():
    def __init__(self, graph, sd):
        self.graph = graph
        random.seed(sd)
        self.result_graph = nx.Graph()
        self.monitor_set = set()

    def pick_start(self):
        try:
            temp=list(set(self.result_graph.nodes()) - self.monitor_set)
            start_node = random.choice(temp)
        except:
            start_node = random.choice([x for x in self.graph.nodes() if x not in self.monitor_set])
        self.monitor_set.add(start_node)
        self.result_graph.add_node(start_node)
        return start_node

    def add_neighbors(self, node):
        neighbors = self.graph.neighbors(node)
        for neighbor in neighbors:
            self.result_graph.add_edge(node, neighbor)

    def place_next_monitor(self, node):
        neighbors = self.graph.neighbors(node)
        max_degree, neighbor_list = 0, []
        neighbor_set = set(neighbors) - self.monitor_set
        for neighbor in neighbor_set:
            degree = self.graph.degree(neighbor)
            if degree > max_degree:
                neighbor_list = []
                max_degree = degree
                neighbor_list.append(neighbor)
            elif degree == max_degree and len(neighbor_list) >= 1:
                neighbor_list.append(neighbor)
            else:
                continue
        if neighbor_set:
            next_monitor = random.choice(neighbor_list)
            self.monitor_set.add(next_monitor)
        else:
            next_monitor = self.pick_start()
        return next_monitor

    def stop(self, allotment):
        if allotment > self.graph.number_of_nodes():
            print "Error, cannot have more than", self.graph.number_of_nodes(), "monitors!"
            sys.exit(1)
        if len(self.monitor_set) < allotment:
            return False
        else:
            return True
