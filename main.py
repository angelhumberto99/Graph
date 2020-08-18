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
    print ("\nThere is an edge between A and B: ", g.IsEdge("A", "B"))

    #The GetCost method returns the value of the edge
    print ("\nThe cost between A and B is: ", g.GetCost("A", "B"))

    #this method prints the whole graph in the following format:
    #( Origin Vertice , Cost, Destiny Vertice ) 
    print ("\nPrinting the graph")
    g.PrintData()

    #This method returns a dictionary 
    #which represents the vertices that are linked to the origin we send as parameter
    print("\nThe neighbors of 'A' are: ", g.GetNeighbors("A"))

    #This method verifies if certain vertice exists in the graph
    print("\nThe graph contains 'A': ",g.Contains("A"))

    #deleting the conection between A and B
    g.EraseConnection("A", "B")

    #checking the data
    print("\nPrinting the graph after deleting the connection between A and B")
    g.PrintData()

    #getting an error
    print("\nTrying to delete a connection that is already done")
    g.EraseConnection("A", "B")


if __name__ == "__main__":
    main()

