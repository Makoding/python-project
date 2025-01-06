class Node():
    def __init__(self, descr):
        self.descr = descr
        self.neighbors = []


class Graph():
    def __init__(self,node_list=[]):
        self.node_list = node_list
        if len(node_list) == 0:
            self.descr_list = []
        else:
            for object in len(node_list):
                self.descr_list[object].append(self.node_list[object].descr)
        
    def add_vertex(self, descr ):
        new_node = Node(descr)
        self.node_list.append(new_node)
        self.descr_list.append(descr)

    def add_edge(self, node1_descr, node2_descr):
        if node1_descr in self.descr_list and node2_descr in self.descr_list:
            for object in range(len(self.node_list)):
                if self.node_list[object].descr == node1_descr:
                    self.node_list[object].neighbors.append(node2_descr)
            for object in range(len(self.node_list)):
                if self.node_list[object].descr == node2_descr:
                    self.node_list[object].neighbors.append(node1_descr)
    
    def __get_index(self, descr):
        for object_index in range(len(self.node_list)):
            if self.node_list[object_index].descr == descr:
                return object_index
    

    def breadth_first_search(self, start_descr, end_descr, already_searched=[],st=""):
        if st == "":
            st += f"{start_descr} is friends with"
        else:
            st += f" {start_descr} who is friends with"
        start_descr_friends = self.node_list[self.__get_index(start_descr)].neighbors
        if end_descr in start_descr_friends:
            st += f" {end_descr}"
            print(st)
        else:
            already_searched.append(start_descr)
            for object in range(len(start_descr_friends)):
                if start_descr_friends[object] not in already_searched:
                    return self.breadth_first_search(start_descr_friends[object], end_descr, already_searched, st)

        
        


facebook = Graph()
facebook.add_vertex("Anne")
facebook.add_vertex("Elisa")
facebook.add_vertex("Bob")
facebook.add_vertex("Carl")
facebook.add_vertex("Diana")

facebook.add_edge("Anne", "Bob")
facebook.add_edge("Anne", "Elisa")
facebook.add_edge("Anne", "Diana")
facebook.add_edge("Bob", "Carl")
facebook.add_edge("Bob", "Diana")
facebook.add_edge("Carl", "Diana")
#facebook.add_edge("Carl", "Elisa")
facebook.breadth_first_search("Elisa", "Carl")

#for object in facebook.node_list:
    #print({f"{object.descr} has {object.neighbors} as friends"})
