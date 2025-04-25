# 1. Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens according to the following constraints. 
# a. Each row should have exactly only one queen. 
# b. Each column should have exactly only one queen. 
# c. No queens are attacking each other. 


n = 8
board = [[0 for _ in range(n)] for _ in range(n)]

row = 0
col = 0
stack = []

while row < n:
    while col < n:
        # Check if position is safe
        safe = True
        for r, c in stack:
            if c == col or abs(r - row) == abs(c - col):
                safe = False
                break
        
        if safe:
            # Place the queen
            board[row][col] = 1
            stack.append((row, col))
            row += 1
            col = 0
            break
        else:
            col += 1
    
    if col == n:
        # Backtrack
        row, col = stack.pop()
        board[row][col] = 0
        col += 1

for i in range(n):
    for j in range(n):
        print("Q" if board[i][j] == 1 else ".", end=" ")
    print()