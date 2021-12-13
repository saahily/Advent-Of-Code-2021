map = [[point for point in row] for row in open("input.txt").read().strip().split("\n")]

def neighbors(point, dim):
    r, c, rlen, clen = point[0], point[1], dim[0], dim[1]
    neighbors = set()
    if r > 0:
        neighbors.add((r-1,c))
    if r < rlen-1:
        neighbors.add((r+1,c))
    if c > 0:
        neighbors.add((r,c-1))
    if c < clen-1:
        neighbors.add((r,c+1))
    return neighbors

def low_points(map):
    low_points = set()
    rlen, clen = len(map), len(map[0])
    for r in range(rlen):
        for c in range(clen):
            if all([int(map[r][c]) < int(map[p[0]][p[1]]) for p in neighbors((r,c), (rlen,clen))]):
                low_points.add((r,c))
    return low_points

def basin_size(low_point, map):
    visited = set([low_point])
    queue = [low_point]
    while queue:
        r,c = queue.pop(0)
        for p in neighbors((r,c), (len(map), len(map[0]))):
            h = int(map[p[0]][p[1]])
            if p not in visited and int(map[r][c]) < h < 9:
                visited.add(p)
                queue.append(p)
    return len(visited)

def part1(map):
    return sum([int(map[r][c])+1 for r,c in low_points(map)])

from operator import mul
def part2(map):
    return reduce(mul, sorted([basin_size(point, map) for point in low_points(map)])[-3:], 1)

print(part1(map))
print(part2(map))
