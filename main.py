from source.Graph import *

def main():

    #we can call the init method using True or False
    #dependig which kind of graph we need
    g = Graph()

    #creating three pairs of vertices
    g.CreateEdge("A", "B", 1)
    g.CreateEdge("C", "D", 3)
    g.CreateEdge("A", "D", 3)

    #The IsEdge method returns True only if an edge is founded
    print ("there is an edge between A and B: ", g.IsEdge("A", "B"))

    #The GetCost method returns the value of the edge
    print ("Cost: (A - ", g.GetCost("A", "B"), " - B)")

    #this method prints the whole graph in the following format:
    #( Origin Vertice , Cost, Destiny Vertice ) 
    g.PrintData()

    #This method returns a dictionary 
    #which represents the vertices that are linked to the origin we send as parameter
    print(g.GetNeighbors("A"))

    #This method verifies if certain vertice exists in the graph
    print(g.Contains("A"))

    #deleting the conection between A and B
    g.EraseEdge("A", "B")

    #checking the data
    g.PrintData()

    #getting an error
    g.EraseEdge("A", "B")


if __name__ == "__main__":
    main()

