entries = open("input.txt").read().strip().split("\n")

def part1(entries):
    count = 0
    for entry in entries:
        output_value = entry.split('|')[1].split()
        for digit in output_value:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                count += 1
    return count

# helper function - decodes output value from single entry
def decode_output_value(entry):
    signal_patterns, output_value = entry.split('|')
    output_value = [set(output_digit) for output_digit in output_value.split()]
    base_patterns = sorted(signal_patterns.split(), key=len)[:3]
    return sum([decode_output_digit(output_value[3-i], base_patterns)*10**i for i in range(3,-1,-1)])

# helper function - decodes single digit output value
def decode_output_digit(digit, base_patterns):
    pattern_length_singletons = { 2:1, 3:7, 4:4, 7:8 }
    if len(digit) in pattern_length_singletons:
        return pattern_length_singletons[len(digit)]
    if len(digit) == 5:
        if digit.union(base_patterns[1]) == digit:
            return 3
        if len(digit.intersection(base_patterns[2])) == 3:
            return 5
        return 2
    if digit.union(base_patterns[2]) == digit:
        return 9
    if digit.union(base_patterns[0]) == digit:
        return 0
    return 6

def part2(entries):
    return sum([decode_output_value(entry) for entry in entries])

print(part1(entries))
print(part2(entries))
