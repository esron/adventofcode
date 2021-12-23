from decimal import Decimal
from sys import stdin
from typing import Iterable

class Point:
    def __init__(self, coord: 'tuple[int, int]', value: int) -> None:
        self.x = coord[0]
        self.y = coord[1]
        self.value = value
        self.f = Decimal('Infinity')
        self.g = Decimal('Infinity')
        self.father: Point = None

    def distance(self, point: 'Point') -> int:
        """Manhattan distance to point"""
        return (point.x - self.x) + (point.y - self.y)

    def set_father(self, point: 'Point') -> None:
        self.father = point

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __gt__(self, __o: object) -> bool:
        return self.f > __o.f

    def __lt__(self, __o: object) -> bool:
        return self.f < __o.f

    def __str__(self) -> str:
        return f'{{ x: {str(self.x)}, y: {str(self.y)}, weight: {self.weight} \
value: {self.value} cost_to_move: {self.cost_to_move} }}'

grid = []
f = open('testinput.txt')
for line in f:
    grid.append(list(map(int, line.rstrip())))


def is_in_range(x: int, y: int, grid: Iterable[Iterable[int]]) -> bool:
    return (0 <= x < len(grid)) and (0 <= y < len(grid[x]))

def append_if_in_range(grid, n, direction):
    if is_in_range(*direction, grid):
        n.append(Point(direction, grid[direction[0]][direction[1]]))

def get_neighbors(point: Point, grid: Iterable[Iterable[int]]) -> Iterable[Point]:
    n = []

    append_if_in_range(grid, n, (point.x - 1, point.y))
    append_if_in_range(grid, n, (point.x, point.y - 1))
    append_if_in_range(grid, n, (point.x + 1, point.y))
    append_if_in_range(grid, n, (point.x, point.y + 1))

    return n

def reconstruct_path(p: Point) -> Iterable[Point]:
    path = []
    while p.father != None:
        path.append(p)
        p = p.father
    return path

def pathfinder(A: Point, goal: Point,
               grid: Iterable[Iterable[int]]) -> Iterable[Point]:
    open_list = [A]
    closed_list = []

    while(len(open_list) != 0):
        open_list = sorted(open_list, reverse=True)
        current = open_list.pop()

        closed_list.append(current)
        if current == goal:
            return reconstruct_path(current)

        neighbors = get_neighbors(current, grid)

        for n in neighbors:
            if n in closed_list:
                continue

            new_g = current.g + n.value

            if new_g < n.g:
                n.father = current
                n.g = new_g
                n.f = new_g + n.distance(goal)

                if n not in open_list:
                    open_list.append(n)


start = Point((0, 0), grid[0][0])
start.g = 0
start.f = 0
goal  = Point((len(grid), len(grid[0])), grid[len(grid) - 1][len(grid[0]) - 1])

path = pathfinder(start, goal, grid)
print(path)
