class Lanternfish:
  def __init__(self, timer):
    self.timer = timer
  def age(self):
    if self.timer == 0:
      self.timer = 6
      return True
    else:
      self.timer -= 1
      return False

initial_timers = list(map(int,open("input.txt").read().split(',')))
population = [Lanternfish(timer) for timer in initial_timers]

def part1(population):
  for _ in range(80):
    new_gen = []
    for fish in population:
      if fish.age():
        new_gen.append(Lanternfish(8))
    population.extend(new_gen)
  return len(population)

# rewrite to reduce time complexity
def part2(initial_timers):
  curr_state = {segment:initial_timers.count(segment) for segment in range(6)}
  for _ in range(256):
    next_state = dict()
    for segment in curr_state:
      if segment == 0:
        next_state[6] = next_state.get(6,0)+curr_state[segment]
        next_state[8] = curr_state[segment]
      else:
        next_state[segment-1] = next_state.get(segment-1,0)+curr_state[segment]
    curr_state = next_state
  return sum(curr_state.values())

print(part2(initial_timers))
