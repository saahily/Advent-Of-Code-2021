lines = open("input.txt").read().strip().split("\n")

def part1and2(lines, part):
  points = dict()
  for line in lines:
    coords = [tuple(map(int,(coord.split(',')))) for coord in line.replace(' ', '').split('->')]
    x1, y1, x2, y2 = coords[0][0], coords[0][1], coords[1][0], coords[1][1]
    if x1 == x2:
      lo, hi = (y1, y2) if y1 < y2 else (y2, y1)
      for i in range(lo, hi+1):
        points[(x1, i)] = points.get((x1, i), 0)+1
    elif y1 == y2:
      lo, hi = (x1, x2) if x1 < x2 else (x2, x1)
      for i in range(lo, hi+1):
        points[(i, y1)] = points.get((i, y1), 0)+1
    elif part == 'part2':
      ypath = range(y1, y2+1) if y2 > y1 else range(y1, y2-1, -1)
      x, xincr = x1, x2 > x1
      for y in ypath:
        points[(x, y)] = points.get((x, y), 0)+1
        x = x+1 if xincr else x-1
  return len([v for v in points.values() if v >= 2])
print(part1and2(lines, 'part1'))
