numbers = list(map(int,input().split(" ")))
height = numbers[0]
width = numbers[1]
length = numbers[2]

matrix = [[0]*height for _ in range(width)]

placed = list(map(int,input().split(" ")))
# A equals 1, B equals 2



for p, currentCol in enumerate(placed):
    col = currentCol - 1
    if p % 2 == 0:
        player = 1
    else:
        player = 2

    for row in range(height):
        if matrix[col][row] == 0:
            matrix[col][row] = player
            break
    
    