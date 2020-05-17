from collections import defaultdict

class Node():
  def __init__(self, data):
    # self.name = name
    self.city = data

class AdjacentNode():
  city = "city"
  cost = "cost"

class Graph():
  def __init__(self):
    self.graph = defaultdict(list)

  def addEdge(self, src, dest, cost="inf"):
    # Adding dest, src Node to Undirected Graph
    # Adding dest Node to the front of the Adjacency List (LL)
    adjacentNode = {
      AdjacentNode.city: Node(dest),
      AdjacentNode.cost: cost 
    }
    self.graph[src].append(adjacentNode)
    # Adding src Node to the front of the Adjacetnty List (LL)
    adjacentNode = {
      AdjacentNode.city: Node(src),
      AdjacentNode.cost: cost 
    }
    self.graph[dest].append(adjacentNode)

  def printGraph(self):
    for v in self.graph:
      print("Adjacency list of vertex {}\n head".format(v), end="")
      nodes = self.graph[v]
      for node in nodes:
        print(" -> {} ({})".format(node[AdjacentNode.city].city, node[AdjacentNode.cost]), end="")
      print("\n")

  def BreadthFirstSearch(self, city):
    # set all cities to not visited (yet)
    visited = dict()
    for city in self.graph:
      visited[city] = False

    queue = list()

    queue.append(city)
    visited[city]

    while queue:
      city = queue.pop(0)
      print(city, end=" ")

      for c in self.graph[city]:
        if not visited[c[AdjacentNode.city].city]:
          queue.append(c[AdjacentNode.city].city)
          visited[c[AdjacentNode.city].city] = True
