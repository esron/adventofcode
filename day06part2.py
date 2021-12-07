from collections import deque

input = input()
input = list(map(int, input.rstrip().split(',')))

fishes = [0] * 9

for i in input:
    fishes[int(i)] += 1

def count_fish(l, days):
    q = deque(l)

    for _ in range(days):
        spawn = q.popleft()
        q[-2] += spawn
        q.append(spawn)
    return sum(q)

print(count_fish(fishes, 256))
