import numpy as np

initial = np.array([[int(num) for num in row] for row in open("input.txt").read().strip().split("\n")])

def step(map):
    energy = np.array([[1,1,1],[1,0,1],[1,1,1]])
    map += 1
    flashers = np.argwhere(map > 9)
    while len(flashers) > 0:
        for r,c in flashers:
            map[r-1:r+2,c-1:c+2] = map[r-1:r+2,c-1:c+2]+energy
            map[r,c] = np.Inf
            flashers = np.argwhere(np.logical_and(map > 9,map!=np.Inf))
    count = np.count_nonzero(map == np.Inf)
    map[map == np.Inf] = 0
    return count

def part1(initial):
    rlen, clen = initial.shape
    flashes = 0
    map = np.full((rlen+2, clen+2), np.NINF)
    map[1:rlen+1, 1:clen+1] = initial
    for _ in range(100):
        flashes += step(map)
    return flashes

def part2(initial):
    rlen, clen = initial.shape
    k = 0
    map = np.full((rlen+2, clen+2), np.NINF)
    map[1:rlen+1, 1:clen+1] = initial
    while True:
        k += 1
        if step(map) == initial.size:
            return k

print(part1(initial))
print(part2(initial))
