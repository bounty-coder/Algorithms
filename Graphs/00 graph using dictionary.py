class graph:
    def __init__(self,edge):
        self.edge = edge
        #initialising dic
        self.graph_dict = {}
        for start,end in self.edge:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print(self.graph_dict)

    def get_path(self,start,end,path=[]):
        path = path + [start]
        
        if start==end:
            return path
        
        elif start not in self.graph_dict:
            return []
        
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_path=self.get_path(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start==end:
            return path

        elif start not in self.graph_dict:
            return None
        
        shortest_path=None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
                
        return shortest_path
    
if __name__ == '__main__':
    route=[
        ('mumbai','delhi'),
        ('mumbai','nagpur'),
        ('delhi','nagpur'),
        ('nagpur','jaipur'),
        ('nagpur','bengaluru'),
        ('bengaluru','nagpur'),
        ('bengaluru','hyderabad'),
        ('delhi','hyderabad')
        ]
    routegraph=graph(route)
    print(routegraph.get_path('nagpur','nagpur'))
    print(routegraph.get_path('nagpur','hyderabad'))
    print(routegraph.get_shortest_path('mumbai','hyderabad'))