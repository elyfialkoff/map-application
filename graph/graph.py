from collections import defaultdict

class Graph():

  COST = 'cost'
  VISITED = 'visited'
  DIRECTIONS = 'directions'

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

    # Keep track of the order in which the cities are visited (for returning/printing)
    orderOfCities = list()

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
      orderOfCities.append(city)

      # iterate through its neighboring cities
      for neighbor in self.graph[city].keys():
        # if the neighbor has not yet been visited
        if not visited[neighbor]:
          # then add it to the queue and proclaim it visited (more like discovered)
          queue.append(neighbor)
          visited[neighbor] = True

    print(orderOfCities)

  def DepthFirstSearch(self, city):
    self._validateSrc(city)

    # Keep track of the order in which the cities are visited (for returning/printing)
    orderOfCities = list()

    # set all cities to not visited (yet)
    visited = {key: False for key in self.graph.keys()}

    orderOfCities = self._helperDFS(city, visited, orderOfCities)
    print(orderOfCities)

  def _helperDFS(self, city, visited, orderOfCities):
    # Proclaim the current city as visited and add it the city ordering
    visited[city] = True
    orderOfCities.append(city)

    # recursively look at each neighbor that has not yet been visited and traverse its neighbors
    for neighbor in self.graph[city]:
      if not visited[neighbor]:
        self._helperDFS(neighbor, visited, orderOfCities)

    return orderOfCities

  def dijkstra(self, src):
    self._validateSrc(src)

    # Initialize a dict for each city with the following default values
    costAndDirectionsDict = defaultdict()
    visited = defaultdict()
    for city in self.graph.keys():
      costAndDirectionsDict[city] = {
        Graph.COST: float("inf"),
        Graph.DIRECTIONS: list()
      }
      visited[city] = {
        Graph.VISITED: False
      }

    # Set the cost to travel to the source as 0
    costAndDirectionsDict[src][Graph.COST] = 0

    for _ in self.graph.keys():

      # go through the non-visited, cheaper nodes to visit next and find the cheapest node
      minNextNode = float("inf")
      nextNode = None
      for key in self.graph.keys():
        if costAndDirectionsDict[key][Graph.COST] < minNextNode and not visited[key][Graph.VISITED]:
          minNextNode = costAndDirectionsDict[key][Graph.COST]
          nextNode = key

      # set the cheapest node to visited
      visited[nextNode][Graph.VISITED] = True

      for city in self.graph.keys():
        # Check that the cost from current to next city is not 0
        existsAndValidCost = city in self.graph[nextNode] and self.graph[nextNode][city] > 0
        # Check that the city has been visited
        visitedYet = visited[city][Graph.VISITED]
        # Check to see if the cost to the next best city + the cost from the next best city to the current city is cheaper
        isCheaper = city in self.graph[nextNode] and costAndDirectionsDict[city][Graph.COST] > costAndDirectionsDict[nextNode][Graph.COST] + self.graph[nextNode][city]
        if existsAndValidCost and not visitedYet and isCheaper:
          costAndDirectionsDict[city][Graph.COST] = costAndDirectionsDict[nextNode][Graph.COST] + self.graph[nextNode][city]
          # If a better route was found, start over
          if costAndDirectionsDict[city][Graph.DIRECTIONS]:
            costAndDirectionsDict[city][Graph.DIRECTIONS] = list()
          # Append the nextNodes route to the current city for backtracking
          [costAndDirectionsDict[city][Graph.DIRECTIONS].append(c) for c in costAndDirectionsDict[nextNode][Graph.DIRECTIONS]]
          costAndDirectionsDict[city][Graph.DIRECTIONS].append(nextNode)

    # Simply append the final city to the directions for backtracking
    for city in self.graph.keys():
      costAndDirectionsDict[city][Graph.DIRECTIONS].append(city)

    for city in self.graph.keys():
      print("{}\t{}\t{}".format(city, costAndDirectionsDict[city][Graph.COST], ', '.join(costAndDirectionsDict[city][Graph.DIRECTIONS])))

    return costAndDirectionsDict

  def kruskalsMinimumSpanningTree(self):
    # Create a tuple of (src, dest, cost) and sort based on cost
    cities = list()
    for key in self.graph.keys():
      for city in self.graph[key].keys():
        cities.append((key, city, self.graph[key][city]))
    
    sortedCities = sorted(cities, key=lambda city: city[2])

    # Initialize a visitedDict to help determine when all cities have been added to the MinimumSpanningTree
    visited = {city: False for city in self.graph.keys()}
    # Initialize a minimumSpanningTree structure
    spanningTree = {city: defaultdict() for city in self.graph.keys()}

    # Check to see if all cities have already been visited (here this will always return False)
    allVisited = [visited[city] for city in visited.keys()]

    # Coninue as long as not all cities have been visited and there are still more cities to compute
    while not all(allVisited) and sortedCities:
      # pop off the cheapest city and add it to the minimumSpanningTree
      src, dest, cost = sortedCities.pop(0)
      # check to see if the src <--> dest creates a cycle in the minimumSpanningTree (we don't want cycles)
      isCycle = self._isCycle(src, dest, spanningTree)
      if not isCycle:
        # mark this city as visited (True)
        visited[src] = True
        # Set the cost of the minimumSpanningTree at src <--> dest
        spanningTree[src][dest] = cost

      # Check if all cities have been visited
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
