from sys import path, stdin
from typing import Optional

class Node:
  nodes: 'list[Node]' = []
  start_node: Optional['Node'] = None
  end_node: Optional['Node'] = None

  def __init__(self, value: str):
      self.value = value
      self.links: list['Node'] = []
      self.visited = False

  def add_link(self, n: 'Node'):
    self.links.append(n)

  def is_big_cave(self):
    return self.value.isupper()

  def visit(self):
    if self.is_big_cave():
      return
    self.visited = True

  def has_node(value):
    for n in Node.nodes:
      if value == n.value:
        return True
    return False

  def get_node(value):
    for n in Node.nodes:
      if value == n.value:
        return n


f = open('testinput.txt')
for line in f:
  line = line.rstrip()
  from_value, to_value = line.split('-')

  if Node.has_node(from_value):
    node_from = Node.get_node(from_value)
  else:
    node_from = Node(from_value)
    if from_value == 'start':
      Node.start_node = node_from
    Node.nodes.append(node_from)


  if Node.has_node(to_value):
    node_to = Node.get_node(to_value)
  else:
    node_to = Node(to_value)
    if to_value == 'end':
      Node.end_node = node_to
    Node.nodes.append(node_to)


  node_from.add_link(node_to)
  node_to.add_link(node_from)

paths = []

def pathfinder(node: Node, path: list):
  if node.visited:
    return
  path.append(node.value)
  node.visit()
  if node.value == 'end':
    return
  for n in node.links:
    pathfinder(n, path)
  return

Node.start_node.visit()

for n in Node.start_node.links:
  path = [Node.start_node.value]
  pathfinder(n, path)
  if len(path) > 0 and path[-1] == 'end':
    paths.append(path)

print(len(paths))
