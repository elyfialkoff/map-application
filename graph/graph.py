from collections import defaultdict

class Node():
  def __init__(self, data):
    self.city = data

class Graph():
  def __init__(self):
    self.graph = defaultdict(defaultdict)

  def addEdge(self, src, dest, cost="inf"):
    # Adding dest, src Node to Undirected Graph
    self.graph[src][dest] = cost
    self.graph[dest][src] = cost

  def printGraph(self):
    for v in self.graph:
      print("Adjacency list of vertex {}\n head".format(v), end="")
      neighbors = self.graph[v]
      for neighbor in neighbors:
        print(" -> {} ({})".format(neighbor, neighbors[neighbor]), end="")
      print("\n")

  def _validateSrc(self, src):
    if src not in self.graph.keys():
      raise Exception('{} not in graph.'.format(src)) 

  def BreadthFirstSearch(self, city):
    self._validateSrc(city)

    # set all cities to not visited (yet)
    visited = {key: False for key in self.graph.keys()}

    # Queue to keep track of cities that have been found, but not yet visited
    queue = list()

    # Add the first city to the queue, proclaim it visited
    queue.append(city)
    visited[city] = True

    # While there are still cities to visit
    while queue:
      # remove the first item from the queue
      city = queue.pop(0)
      print(city, end=" ")

      # iterate through its neighboring cities
      for neighbor in self.graph[city].keys():
        # if the neighbor has not yet been visited
        if not visited[neighbor]:
          # then add it to the queue and proclaim it visited (more like discovered)
          queue.append(neighbor)
          visited[neighbor] = True

  def DepthFirstSearch(self, city):
    self._validateSrc(city)

    # set all cities to not visited (yet)
    visited = {key: False for key in self.graph.keys()}

    self._helperDFS(city, visited)

  def _helperDFS(self, city, visited):
    visited[city] = True
    print(city, end=" ")

    for neighbor in self.graph[city]:
      if not visited[neighbor]:
        self._helperDFS(neighbor, visited)

  def dijkstra(self, src):
    self._validateSrc(src)

    # Initialize a dict for each city with the following default values
    costAndDirectionsDict = defaultdict()
    visited = defaultdict()
    for city in self.graph.keys():
      costAndDirectionsDict[city] = {
        "cost": float("inf"),
        "directions": list()
      }
      visited[city] = {
        "visited": False
      }

    # Set the cost to travel to the source as 0
    costAndDirectionsDict[src]["cost"] = 0

    for _ in self.graph.keys():

      # go through the non-visited, cheaper nodes to visit next and find the cheapest node
      minNextNode = float("inf")
      nextNode = None
      for key in self.graph.keys():
        if costAndDirectionsDict[key]["cost"] < minNextNode and not visited[key]["visited"]:
          minNextNode = costAndDirectionsDict[key]["cost"]
          nextNode = key

      # set the cheapest node to visited
      visited[nextNode]["visited"] = True

      for city in self.graph.keys():
        # Check that the cost from current to next city is not 0
        existsAndValidCost = city in self.graph[nextNode] and self.graph[nextNode][city] > 0
        # Check that the city has been visited
        visitedYet = visited[city]["visited"]
        # Check to see if the cost to the next best city + the cost from the next best city to the current city is cheaper
        isCheaper = city in self.graph[nextNode] and costAndDirectionsDict[city]["cost"] > costAndDirectionsDict[nextNode]["cost"] + self.graph[nextNode][city]
        if existsAndValidCost and not visitedYet and isCheaper:
          costAndDirectionsDict[city]["cost"] = costAndDirectionsDict[nextNode]["cost"] + self.graph[nextNode][city]
          # If a better route was found, start over
          if costAndDirectionsDict[city]["directions"]:
            costAndDirectionsDict[city]["directions"] = list()
          # Append the nextNodes route to the current city for backtracking
          [costAndDirectionsDict[city]["directions"].append(c) for c in costAndDirectionsDict[nextNode]["directions"]]
          costAndDirectionsDict[city]["directions"].append(nextNode)

    # Simply append the final city to the directions for backtracking
    for city in self.graph.keys():
      costAndDirectionsDict[city]["directions"].append(city)

    for city in self.graph.keys():
      print("{}\t{}\t{}".format(city, costAndDirectionsDict[city]["cost"], ', '.join(costAndDirectionsDict[city]["directions"])))

    return costAndDirectionsDict

  def kruskalsMinimumSpanningTree(self):
    cities = list()
    for key in self.graph.keys():
      for city in self.graph[key].keys():
        cities.append((key, city, self.graph[key][city]))
    
    sortedCities = sorted(cities, key=lambda city: city[2])

    visited = {city: False for city in self.graph.keys()}
    spanningTree = {city: defaultdict() for city in self.graph.keys()}

    allVisited = [visited[city] for city in visited.keys()]

    while not all(allVisited) and sortedCities:
      src, dest, cost = sortedCities.pop(0)
      isCycle = self._isCycle(src, dest, spanningTree)
      if not isCycle:
        visited[src] = True
        spanningTree[src][dest] = cost

      allVisited = [visited[city] for city in visited.keys()]

    for city in spanningTree:
      print("{} -> {}".format(city, ', '.join(["{} ({})".format(key, spanningTree[city][key]) for key in spanningTree[city].keys()])))

    return spanningTree

  def _isCycle(self, src, dest, cities):
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
