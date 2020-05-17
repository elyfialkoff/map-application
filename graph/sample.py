from graph import Graph

def main():
  graph = Graph()
  graph.addEdge("Salt Lake City", "Seattle", 800) 
  graph.addEdge("Salt Lake City", "Houston", 1450) 
  graph.addEdge("Seattle", "San Diego", 1255) 
  graph.addEdge("Seattle", "Phoenix", 1415) 
  graph.addEdge("Seattle", "Houston", 2300) 
  graph.addEdge("San Diego", "Phoenix", 350) 
  graph.addEdge("Phoenix", "Houston", 1175) 

  graph.printGraph()

  graph.BreadthFirstSearch("Houston")


if __name__ == '__main__':
  main()