grid = [list(f.replace("\n", "")) for f in open("input.dat")]

width = len(grid[0])
height = len(grid)


def get_next_index(type: str, x: int, y: int) -> tuple:
    match type:
        case ">":
            return (x + 1) % width, y
        case "v":
            return x, (y+1)%height
        case ".":
            return x, y


finished = False
not_moving_steps = 0
i = 1
while not finished:
    able_to_move = []
    for y in range(height):
        for x in range(width):
            n_x, n_y  = get_next_index(grid[y][x], x, y)
            match (grid[y][x], grid[n_y][n_x], i%2==1):
                case (">", ".", True):
                    able_to_move.append([y,x,"."])
                    able_to_move.append([n_y,n_x,">"])
                case ("v", ".", False):
                    able_to_move.append([y,x,"."])
                    able_to_move.append([n_y,n_x,"v"])

    match (not_moving_steps, len(able_to_move)==0):
        case (0, True):
            not_moving_steps = 1
        case (1, True):
            finished = True
        case _:
            not_moving_steps = 0

       
    for move in able_to_move:
        grid[move[0]][move[1]] = move[2]

    i+=1


print((i+1)//2)