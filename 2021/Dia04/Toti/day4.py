l = [line.split("\n")[0] for line in open("input4.txt", "r")]

drawn_numbers = l[0].split(',')

boards = []
board = []
c = 0
for i in l[1:]:
    if i == '':
        c = 0
    else:
        c += 1
    if c >= 1:
        board.append(i.split(' '))   
    if c >=5:
        c = 0
        boards.append(board)
        board = []
    
boards_clean=[]
for b in boards:
    x = []
    for line in b:
        x.append([i for i in line if i != ''])
    boards_clean.append(x)

def check_if_won(board):
    for i in range(5):
        if board[i][i] == 'X':
            if board[i] == ['X', 'X', 'X', 'X', 'X'] or ([board[0][i],board[1][i],board[2][i],board[3][i],board[4][i]] == ['X', 'X', 'X', 'X', 'X']):
                return True
    return False

def draw(drawn_numbers):
    for num in drawn_numbers:
        for i in range(len(boards_clean)):
            for j in range(5):
                for k in range(5):
                    if boards_clean[i][j][k] == num:
                        boards_clean[i][j][k] = 'X'
            if check_if_won(boards_clean[i]):
                c = 0
                for line in range(5):
                    for col in range(5):
                        if boards_clean[i][line][col] != 'X':
                            c += int(boards_clean[i][line][col])
                return(c*int(num))


def draw2(drawn_numbers):
    won = []
    last_num = 0
    for num in drawn_numbers:
        for i in range(len(boards_clean)):
            for j in range(5):
                for k in range(5):
                    if boards_clean[i][j][k] == num:
                        boards_clean[i][j][k] = 'X'

            for line in boards_clean[i]:
            #print(line)
            #print('----------------------')
            #print('checking...')
                if i not in won:
                    if check_if_won(boards_clean[i]):
                        print(i,'won with',int(num))
                        last_num = int(num)
                        won.append(i)
                        #c = 0
                        #for line in range(5):
                            #for col in range(5):
                                #if boards_clean[i][line][col] != 'X':
                                    #c += int(boards_clean[i][line][col])
                        #return(c*int(num))
        if len(won) == len(boards_clean):
            break
    return(won,last_num)



t = draw2(drawn_numbers)
print('results')
print(t[0][-1],t[1])
last = t[0][-1]

for line in boards_clean[last]:
    print(line)
print('----------------------')
c = 0
for line in range(5):
    for col in range(5):
        if boards_clean[last][line][col] != 'X':
            c += int(boards_clean[last][line][col])
print(c*t[1])
