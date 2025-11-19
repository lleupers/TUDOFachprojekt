h, w, k = map(int, input().split())
moves = list(map(int, input().split()))

# Board: w Spalten, jede h hoch
board = [[0]*h for _ in range(w)]

winner = None
winmove = None

for p, currentCol in enumerate(moves):
    col = currentCol - 1
    player = 1 if p % 2 == 0 else 2  # A=1, B=2

    # Stein fallen lassen
    row = 0
    while row < h and board[col][row] != 0:
        row += 1
    board[col][row] = player

    # Wincheck: vier Richtungen
    # (dx,dy): rechts, oben, diag-down-right, diag-up-right
    directions = [(1,0), (0,1), (1,1), (1,-1)]

    for dx, dy in directions:
        count = 1

        # nach vorne
        x, y = col + dx, row + dy
        while 0 <= x < w and 0 <= y < h and board[x][y] == player:
            count += 1
            x += dx
            y += dy

        # nach hinten
        x, y = col - dx, row - dy
        while 0 <= x < w and 0 <= y < h and board[x][y] == player:
            count += 1
            x -= dx
            y -= dy

        if count >= k:
            winner = player
            winmove = p + 1
            break

    if winner:
        break

if winner is None:
    print("D")
else:
    print("A" if winner == 1 else "B", winmove)
