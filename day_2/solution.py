lines = open("input.txt").read().strip().split("\n")

def part1(lines):
	hor_pos = 0
	depth = 0
	for line in lines:
		direction, magnitude = line.split(" ")
		magnitude = int(magnitude)
		if direction == "up":
			depth -= magnitude
		elif direction == "down":
			depth += magnitude
		elif direction == "forward":
			hor_pos += magnitude
	return hor_pos * depth

def part2(lines):
	hor_pos = 0
	depth = 0
	aim = 0
	for line in lines:
		direction, magnitude = line.split(" ")
		magnitude = int(magnitude)
		if direction == "up":
			aim -= magnitude
		elif direction == "down":
			aim += magnitude
		elif direction == "forward":
			hor_pos += magnitude
			depth += aim * magnitude
	return hor_pos * depth

print(part1(lines))
print(part2(lines))
