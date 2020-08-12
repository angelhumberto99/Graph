class Graph:
    def __init__(self, directed = False):
        self.__directed = directed
        self.__graph = {}


    def IsEdge(self, origin, destiny):
        if self.__graph.get(origin, False):
            if self.__graph[origin].get(destiny, False):
                return True
            return False
        return False


    def CreateEdge(self, origin, destiny, cost):
        destinies = {}

        if self.__directed:
            if self.__graph.get(origin, False):
                destinies = self.__graph[origin]
            destinies[destiny] = cost
            self.__graph[origin] = destinies

        else:
            o_d = {}
            d_o = {}

            if self.__graph.get(origin, False):
                o_d = self.__graph[origin]
            
            o_d[destiny] = cost

            if self.__graph.get(destiny):
                d_o = self.__graph[destiny]
            
            d_o[origin] = cost

            self.__graph[origin] = o_d
            self.__graph[destiny] = d_o


    def PrintData(self):
        #print(self.__graph)
        size = len(self.__graph)
        i = 0
        keys = list(self.__graph.keys())

        for i in range(0, size):
            auxDict = dict(self.__graph[keys[i]])
            subKeys = list(auxDict.keys()) 
            subSize = len(auxDict)
            for j in range(0, subSize):
                print("(", keys[i], ",", auxDict[subKeys[j]],
                      ",", subKeys[j], ")")


    def GetCost(self, origin, destiny):
        if self.IsEdge(origin, destiny) == False:
            print("The edge does not exist")
            return
        return self.__graph[origin][destiny]

        
    def GetNeighbors(self, origin):
        if self.__graph.get(origin, False) == False:
            print("The origin doesn't exist")
            return
        return self.__graph[origin]


    def Contains(self, origin):
        if self.__graph.get(origin, False):
            return True
        return False