lines = open("input.txt").read().strip().split("\n")

def part1(lines):
	count = 0
	prev = int(lines[0])
	for line in lines:
		curr = int(line)
		if curr > prev:
			count += 1
		prev = curr
	return count

def part2(lines):
	count = 0
	prev_sum = int(lines[0]) + int(lines[1]) + int(lines[2])
	for i in range(1, len(lines) - 2):
		curr_sum = prev_sum - int(lines[i - 1]) + int(lines[i + 2])
		if curr_sum > prev_sum:
			count += 1
		prev_sum = curr_sum
	return count

print(part1(lines))
print(part2(lines))
