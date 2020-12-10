#####################################################################
# freight_service.py
#####################################################################


# Node Definition
class Node(object):
    city_label = None

    def __init__(self, city_label):
        self.city_label = city_label
    
    def get_city_label(self):
        return self.city_label


#####################################################################


# Edge Definition
class Edge(object):
    source = None
    target = None
    train_label = None

    def __init__(self, source, target, train_label):
        self.source = source
        self.target = target
        self.train_label = train_label

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_train_label(self):
        return self.train_label


#####################################################################


# Custom Graph Implementation
class Graph(object):
    list_of_distinct_nodes = list()
    list_of_distinct_cities = list()
    set_of_distinct_edges = set()
    set_of_freight_trains = set()
    adjacency_matrix = []

    def __init__(self, number_of_distinct_cities, list_of_trains, list_of_routes, set_of_distinct_cities):
        self.number_of_distinct_cities = number_of_distinct_cities
        self.list_of_trains = list_of_trains
        self.list_of_routes = list_of_routes
        self.set_of_distinct_cities = set_of_distinct_cities
        self.initialize_adjacenct_matrix()

    def initialize_adjacenct_matrix(self):
        self.adjacency_matrix = [[0] * self.number_of_distinct_cities for x in range(self.number_of_distinct_cities)]
        self.adjacency_matrix = self.adjacency_matrix * self.number_of_distinct_cities

    def initializeGraph(self):
        for city in self.set_of_distinct_cities:
            self.list_of_distinct_cities.append(city)
            self.list_of_distinct_nodes.append(self.create_node(city))

        print(self.list_of_distinct_cities)

        for i in range(len(self.list_of_trains)):
            train_label = self.list_of_trains[i]
            # create nodes out of the list of cities
            list_of_cities = self.list_of_routes[i]
            # print(train_label,"<-->", list_of_cities)
            for f in range(len(list_of_cities)):
                for g in range(f, len(list_of_cities)):
                    source_city = list_of_cities[f]
                    target_city = list_of_cities[g]
                    if (source_city != target_city):
                        source_index = self.list_of_distinct_cities.index(source_city)
                        target_index = self.list_of_distinct_cities.index(target_city)
                        source_node = self.list_of_distinct_nodes[source_index]
                        target_node = self.list_of_distinct_nodes[target_index]
                        edge = self.create_edge(source_node, target_node, train_label)
                        self.update_adjacency_matrix(source_index, target_index)
                        self.set_of_distinct_edges.add(edge)
                    else:
                        continue

    def create_node(self, city_label):
        return Node(city_label)
    
    def create_edge(self, source, target, train_label):
        return Edge(source, target, train_label)

    def update_adjacency_matrix(self, index_of_source_city, index_of_target_city):
        # print("indices:", index_of_source_city, index_of_target_city)
        if (index_of_source_city != index_of_target_city):
            self.adjacency_matrix[index_of_source_city][index_of_target_city] = 1
            self.adjacency_matrix[index_of_target_city][index_of_source_city] = 1
        else:
            self.adjacency_matrix[index_of_source_city][index_of_target_city] = 0

    def print_adjacency_matrix(self):
        for i in range(self.number_of_distinct_cities):
            for k in range(self.number_of_distinct_cities):
                print((self.adjacency_matrix[i][k]), end="  ")
            print()
    
    # remove the following function before submitting the assignment
    def print_edge_list(self):
        for edge in self.set_of_distinct_edges:
            print(edge.train_label,":", edge.get_source().get_city_label(),"<--->", edge.get_target().get_city_label())

#####################################################################


# FileUtilities Functions
class FileUtilities(object):
    def __init__(self):
        self.READ_MODE = "r"
        self.list_of_trains = []
        self.list_of_routes = []
        self.set_of_distinct_cities = set()

    def read_input_file(self, inputfile):
        file = open(inputfile, self.READ_MODE)
        for line in file:
            entries = line.split("/")
            stripped_entries = [item.strip() for item in entries]
            self.list_of_trains.append(stripped_entries[0])
            self.list_of_routes.append(stripped_entries[1:])
            self.set_of_distinct_cities.update(set(stripped_entries[1:]))
        file.close()

    def get_number_of_distinct_cities(self):
        return len(self.set_of_distinct_cities)

    def get_set_of_distinct_cities(self):
        return self.set_of_distinct_cities

    def get_list_of_trains(self):
        return self.list_of_trains

    def get_list_of_routes(self):
        return self.list_of_routes


#####################################################################


class FreightService(object):
    def __init__(self):
        self.graph = None
        self.fileUtilities = FileUtilities()

    def readCityTrainfile(self, inputfile):
        # read the input file
        self.fileUtilities.read_input_file(inputfile)
        
        # create the collections of trains and cities
        number_of_distinct_cities = self.fileUtilities.get_number_of_distinct_cities()
        list_of_trains = self.fileUtilities.get_list_of_trains()
        list_of_routes = self.fileUtilities.get_list_of_routes()
        set_of_distinct_cities = self.fileUtilities.get_set_of_distinct_cities()

        # now create the Graph object and then initialize it
        self.graph = Graph(number_of_distinct_cities, list_of_trains, list_of_routes, set_of_distinct_cities)
        self.graph.initializeGraph()
        self.graph.print_adjacency_matrix()  # remove this function call

    def showAll(self):
        pass

    def displayTransportHub(self):
        pass

    def displayConnectedCities(self, train):
        pass

    def displayDirectTrain(self, city_a, city_b):
        pass

    def findServiceAvailable(self, city_a, city_b): 
        pass
    
    def readPromptFile(self, promptfile):
        pass


#####################################################################
if __name__ == "__main__":
    freightService = FreightService()
    freightService.readCityTrainfile("inputPS22.txt")
    # freightService.showAll()


