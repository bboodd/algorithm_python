n,m = map(int,input().split())
bw = ["B","W"]
board = []
count = []
for _ in range(n):
    board.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        b_count = 0
        c_board = [item[:] for item in board]
        last = ''
        for x in range(8):
            if c_board[i+x][j] != last:
                c_board[i+x][j] = last
            for y in range(7):
                if c_board[i+x][j+y] == c_board[i+x][j+y+1]:
                    if c_board[i+x][j+y] == "W":
                        b_count+=1
                        c_board[i+x][j+y+1] = "B"
                    else:
                        b_count+=1
                        c_board[i+x][j+y+1] = "W"
            last = c_board[i+x][j+7]
        count.append(b_count)
count.sort()
print(count[0])