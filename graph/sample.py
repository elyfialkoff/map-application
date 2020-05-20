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

  # graph.printGraph()

  # graph.BreadthFirstSearch("0")
  # print()
  # graph.DepthFirstSearch("0")
  # print()
  # graph.dijkstra("0")

  cities = list()
  for key in graph.graph.keys():
    for city in graph.graph[key].keys():
      cities.append((key, city, graph.graph[key][city]))
  
  sortedCities = sorted(cities, key=lambda city: city[2])

  visited = {city: False for city in graph.graph.keys()}
  spanningTree = {city: defaultdict() for city in graph.graph.keys()}

  allVisited = [visited[city] for city in visited.keys()]

  while not all(allVisited) and sortedCities:
    src, dest, cost = sortedCities.pop(0)
    isCycle = _isCycle(src, dest, spanningTree)
    if not isCycle:
      visited[src] = True
      spanningTree[src][dest] = cost

    allVisited = [visited[city] for city in visited.keys()]

  for city in spanningTree:
    print("{} -> {}".format(city, ', '.join(["{} ({})".format(key, spanningTree[city][key]) for key in spanningTree[city].keys()])))

def _isCycle(src, dest, cities):
  # set all cities to not visited (yet)
  visited = {city: False for city in cities.keys()}

  queue = list()
  queue.append(src)
  visited[src] = True

  # While there are still cities to visit
  while queue:
    # remove the first item from the queue
    city = queue.pop(0)

    # iterate through its neighboring cities
    for neighbor in cities[city].keys():
      if dest == city:
        return True
      
      # if the neighbor has not yet been visited
      if not visited[neighbor]:
        # then add it to the queue and proclaim it visited (more like discovered)
        queue.append(neighbor)
        visited[neighbor] = True
    
  return False
  
  
if __name__ == '__main__':
  main()