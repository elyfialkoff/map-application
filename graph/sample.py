from graph import Graph
from collections import defaultdict

def main():
  graph = Graph()
  # graph.addEdge("Salt Lake City", "Seattle", 800) 
  # graph.addEdge("Salt Lake City", "Houston", 1450) 
  # graph.addEdge("Seattle", "San Diego", 1255) 
  # graph.addEdge("Seattle", "Phoenix", 1415) 
  # graph.addEdge("Seattle", "Houston", 2300) 
  # graph.addEdge("San Diego", "Phoenix", 350) 
  # graph.addEdge("Phoenix", "Houston", 1175) 

  graph.addEdge("0", "1", 4)
  graph.addEdge("0", "7", 8)
  graph.addEdge("1", "2", 8)
  graph.addEdge("1", "7", 11)
  graph.addEdge("2", "3", 7)
  graph.addEdge("2", "5", 4)
  graph.addEdge("2", "8", 2)
  graph.addEdge("3", "4", 9)
  graph.addEdge("3", "5", 14)
  graph.addEdge("4", "5", 10) 
  graph.addEdge("5", "6", 2) 
  graph.addEdge("6", "7", 1)
  graph.addEdge("6", "8", 6)
  graph.addEdge("7", "8", 7)

  graph.printGraph()

  graph.BreadthFirstSearch("0")
  print()
  graph.DepthFirstSearch("0")
  print()
  graph.dijkstra("0")
  print()
  graph.kruskalsMinimumSpanningTree()
  

if __name__ == '__main__':
  main()