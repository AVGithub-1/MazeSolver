#could make a class for wall pieces
import random

class Obstacle():

    def __init__(self, start):
        self.character = '🟦'
        self.start = start
        self.segments = random.randint(2, 7)
        self.direction = ''
        self.positions = [self.start]

        if self.start[0] == 0:
            self.direction = 'down'
        if self.start[0] == 9:
            self.direction = 'up'
        if self.start[1] == 0:
            self.direction = 'right'
        if self.start[1] == 9:
            self.direction = 'left'

    #def create_branch(self):


grid = [] #the maze grid
obstacle_list = [] #liist of all obstacles/wall segments that branch from the border
def create_maze():
    """
    This will create a random 10x10 square maze
    """
    #this part makes the basic grid to put the wall pieces on

    for i in range(10):
        grid.append([])
        for m in range(10):
            grid[i].append('⬜')
        #print(grid[i])

    #this will make the border and leave one space as the finish
    border = []   #🟦

    for i in range(10):

        if i == 0 or i == 9:
            for n in range(10):
                grid[i][n] = '🟦'
                border.append([i, n])

        else:
            for n in range(10):
                if n == 0 or n == 9:
                    grid[i][n] = '🟦'
                    border.append([i, n])


    grid[9][8] = '⬜'
    grid[9][9] = '🏁'
    border.remove([9, 8])
    border.remove([9, 9])

    border_tuple = tuple(border)
    #this creates a list of possible starting positions for the Obstacles
    obstacle_start_options = border
    corner_positions = ([0,0], [0,1], [1,0], [8,0], [9, 0], [9,1], [0,8], [0,9], [1,9], [8,9])
    for i in corner_positions:
        obstacle_start_options.remove(i)

    #this fills the list of obstacles with a random number of obstacle instances
    #with different start positions
    for i in range(random.randint(7,10)):
        obstacle_list.append(Obstacle(random.choice(obstacle_start_options)))
        obstacle_start_options.remove(obstacle_list[-1].start)


    #check they have acceptable start positions and directions
    #for i in obstacle_list:
        #print(i.start, i.direction)

    #actually create the obstacles on the maze board
    for i in obstacle_list:

        if i.direction == 'up' or i.direction == 'down':
            x = i.start[0]

            for l in range(i.segments):

                grid[x][i.start[1]] = '🟦'

                if i.direction == 'up':
                    x -= 1
                    if grid[x][i.start[1]] == '🟦' or grid[x - 1][i.start[1]] == '🟦':
                        break

                    if grid[x][i.start[1] + 1] == '🟦' or grid[x][i.start[1] - 1] == '🟦':
                        grid[x + 1][i.start[1]] = '⬜'
                        continue

                if i.direction == 'down':
                    x += 1
                    if grid[x][i.start[1]] == '🟦' or grid[x + 1][i.start[1]] == '🟦':
                        break

                    if grid[x][i.start[1] + 1] == '🟦' or grid[x][i.start[1] - 1] == '🟦':
                        grid[x - 1][i.start[1]] = '⬜'
                        continue

        if i.direction == 'left' or i.direction == 'right':
            x = i.start[1]

            for l in range(i.segments):
                #issue is very next if statement below; for first iteration, the condition is triggered
                #and x doesn't change
                if l == 0:
                    pass
                elif grid[i.start[0] + 1][x] == '🟦' or grid[i.start[0] - 1][x - 1] == '🟦':
                    continue

                grid[i.start[0]][x] = '🟦'


                if i.direction == 'left':
                    x -= 1

                    #if next two spaces are blue squares
                    if grid[i.start[0]][x] == '🟦' or grid[i.start[0]][x - 1] == '🟦':
                        break #maybe change to continue

                    #if spaces above and below next space are blue squares
                    if grid[i.start[0] + 1][x] == '🟦' or grid[i.start[0] - 1][x] == '🟦':
                        grid[i.start[0]][x + 1] = '⬜'
                        continue

                if i.direction == 'right':
                    x += 1
                    if grid[i.start[0]][x] == '🟦' or grid[i.start[0]][x + 1] == '🟦':
                        break

                    if grid[i.start[0] + 1][x] == '🟦' or grid[i.start[0] - 1][x] == '🟦':
                        grid[i.start[0]][x - 1] = '⬜'
                        continue

    #print(border)
    for i in border_tuple:
        if grid[i[0]][i[1]] == '⬜':
            grid[i[0]][i[1]] = '🟦'


def print_grid():
    for i in range(10):
        print(''.join(' '.join(grid[i])))
    print(' ')

    #for i in obstacle_list:
        #print(i.start, i.segments)
#create_maze()
