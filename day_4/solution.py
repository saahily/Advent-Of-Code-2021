class Board:
    def __init__(self, board):
        self.board = [list(map(int,(row.split()))) for row in board]
    def mark(self, num):
        self.board = [['x' if n == num else n for n in row] for row in self.board]
    def check(self):
        bingo = ['x','x','x','x','x']
        for row in self.board:
            if row == bingo:
                return True
        for c in range(5):
            if [row[c] for row in self.board] == bingo:
                return True
        return False
    def score(self, num):
        sum = 0
        for r in range(5):
            for c in range(5):
                curr = self.board[r][c]
                if type(curr) == int:
                    sum += curr
        return sum * num

lines = open("input.txt").read().strip().split("\n")
nums, board_lines = list(map(int,(lines[0].split(',')))), lines[2:]
boards = [Board(board_lines[i*6:i*6+5]) for i in range(int((len(board_lines)+1)/6))]

def part1(nums, boards):
    for num in nums:
        for board in boards:
            board.mark(num)
            if board.check():
                return board.score(num)

def part2(nums, boards):
  for num in nums:
      for board in list(boards):
          board.mark(num)
          if board.check() and len(boards) > 1:
              boards.remove(board)
          elif board.check() and len(boards) == 1:
              return board.score(num)

print(part1(nums, boards))
print(part2(nums, boards))
