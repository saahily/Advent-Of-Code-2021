lines = open("input.txt").read().strip().split("\n")

def scan(line):
    pairs = {'(':')','[':']','{':'}','<':'>'}
    error_pts = {')':3,']':57,'}':1197,'>':25137}
    completion_pts = {')':1,']':2,'}':3,'>':4}
    stack = []
    for char in line:
        if char in pairs:
            stack.append(char)
        else:
            left = stack.pop()
            if char != pairs[left]:
                return 'corrupted', error_pts[char]
    if len(stack) == 0:
        return 'complete', 0
    completion, completion_score = [], 0
    while stack:
        left = stack.pop()
        completion.append(pairs[left])
    for right in completion:
        completion_score *= 5
        completion_score += completion_pts[right]
    return 'incomplete', completion_score

def part1(lines):
    error_score = 0
    for line in lines:
        result = scan(line)
        if result[0] == 'corrupted':
            error_score += result[1]
    return error_score

def part2(lines):
    completion_scores = []
    for line in lines:
        result = scan(line)
        if result[0] == 'incomplete':
            completion_scores.append(result[1])
    return sorted(completion_scores)[len(completion_scores)//2]

print(part1(lines))
print(part2(lines))
