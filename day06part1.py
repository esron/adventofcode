from sys import stdin

fishes = input()

fishes = list(map(int, fishes.rstrip().split(',')))

new_fishes = []
for _ in range(80):
    for i in range(len(fishes)):
        if fishes[i] == 0:
            new_fishes.append(8)
            fishes[i] = 6
            continue
        fishes[i] -= 1
    fishes.extend(new_fishes)
    new_fishes = []

print(len(fishes))
