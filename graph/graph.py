from collections import defaultdict

class Node():
  def __init__(self, data):
    # self.name = name
    self.city = data

class Graph():
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, src, dest, cost="inf"):
    # Adding dest, src Node to Undirected Graph
    # Adding dest Node to the front of the Adjacency List (LL)
    self.graph[src].append((Node(dest), cost))
    # Adding src Node to the front of the Adjacetnty List (LL)
    self.graph[dest].append((Node(src), cost))

  def printGraph(self):
    for v in self.graph:
      print("Adjacency list of vertex {}\n head".format(v), end="")
      nodes = self.graph[v]
      for node, cost in nodes:
        print(" -> {} ({})".format(node.city, cost), end="")
      print("\n")

  def BreadthFirstSearch(self, city):
    # set all cities to not visited (yet)
    visited = dict()
    for key in self.graph.keys():
      visited[key] = False

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
      for node, _ in self.graph[city]:
        city = node.city
        # if the city has not yet been visited
        if not visited[city]:
          # then add it to the queue and proclaim it visited (more like discovered)
          queue.append(city)
          visited[city] = True
