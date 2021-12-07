arr = list(map(int,open("input.txt").read().split(',')))

def part1(arr):
    n = len(arr)
    arr.sort();
    median = arr[(n-1)//2] if (n % 2 == 0) else arr[n//2]
    return sum([abs(num-median) for num in arr])

# brute force approach
def part2(arr):
  min_fuel = float("inf")
  for pos in range(min(arr), max(arr)+1):
    fuel = 0
    for num in arr:
      n = abs(pos-num)
      fuel += n*(n+1)/2
    if fuel < min_fuel:
      min_fuel = fuel
  return min_fuel

# discovered that the alignment pos was just the mean
def part2_optimized(arr):
  avg = sum(arr)/len(arr)
  fuel = 0
  for num in arr:
    n = abs(num-avg)
    fuel += n*(n+1)/2
  return int(fuel)

print(part2_optimized(arr))
