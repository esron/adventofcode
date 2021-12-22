from _typeshed import Self
from sys import stdin
from typing import Iterable

class Point:
    def __init__(self, coord: tuple[int, int], value: int, cost_to_move: int, weight: int) -> None:
        self.x = coord[0]
        self.y = coord[1]
        self.value = value
        self.cost_to_move = cost_to_move
        self.weight = weight
        self.father: Point = None

    def distance(self, point: 'Point') -> int:
        """Manhattan distance to point"""
        return (point.x - self.x) + (point.y - self.y)

    def set_father(self, point: 'Point') -> None:
        self.father = point

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __gt__(self, __o: object) -> bool:
        return self.weight > __o.weight

    def __lt__(self, __o: object) -> bool:
        return self.weight < __o.weight



grid = []
f = open('testinput.txt')
for line in f:
    grid.append(list(map(int, line.rstrip())))


def is_in_range(x: int, y: int, grid: Iterable[Iterable[int]]) -> bool:
    return (0 <= x < len(grid)) and (0 <= y < len(grid[x]))

start = (0, 0)
goal = (len(grid), len(grid[0]))

def pathfinder(A: Point, grid: Iterable[Iterable[int]]) -> Iterable[Point]:
    open_list = [A]
    closed_list = []

    while(len(open_list) != 0):
        open_list = sorted(open_list, reverse=True)
        current = open_list.pop()
