diag = [[char for char in line] for line in open("input.txt").read().strip().split("\n")]

def part1(diag):
  diag_t = [list(x) for x in zip(*diag)]
  gamma = ''.join(['1' if pos.count('1') > len(pos)/2 else '0' for pos in diag_t])
  epsilon = ''.join(['0' if bit == '1' else '1' for bit in gamma])
  return int(gamma, 2) * int(epsilon, 2)

def part2(diag):
  ogr = csr = diag
  for i in range(len(ogr[0])):
    pos = [num[i] for num in ogr]
    mcv = '1' if pos.count('1') >= len(pos)/2 else '0'
    ogr = list(filter(lambda num: num[i] == mcv, ogr))
    if len(ogr) == 1:
      break
  for i in range(len(csr[0])):
    pos = [num[i] for num in csr]
    lcv = '0' if pos.count('0') <= len(pos)/2 else '1'
    csr = list(filter(lambda num: num[i] == lcv, csr))
    if len(csr) == 1:
      break
  return int(''.join(ogr[0]), 2) * int(''.join(csr[0]), 2)

print(part2(diag))
