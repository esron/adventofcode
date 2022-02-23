from sys import stdin

numbers = input()

numbers = numbers.rstrip().split(',')

boards = []
board = []
input()
for line in stdin:
  if line == '\n':
    boards.append(board)
    board = []
    continue
  board.append(list(filter(lambda e: e != '', line.strip().split(' '))))

boards.append(board)

def bingo(board):
  for i in range(0, len(board)):
    colum_count = 0
    line_count = 0
    for j in range(0, len(board[i])):
      if board[i][j] == 'X':
        line_count += 1
      if line_count == 5:
        return True
      if board[j][i] == 'X':
        colum_count += 1
      if colum_count == 5:
        return True
  return False

def score(board):
  score = 0
  for line in board:
    score += sum(map(lambda x: int(x) if x != 'X' else 0, line))
  return score

for number in numbers:
  for b in range(0, len(boards)):
    for i in range(0, len(boards[b])):
      for j in range(0, len(boards[b][i])):
        if boards[b][i][j] == number:
          boards[b][i][j]  = 'X'

          if bingo(boards[b]):
            print(score(boards[b]) * int(number))
            exit(0)
