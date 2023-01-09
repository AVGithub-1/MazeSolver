import maze_generation as magen
import random
from time import sleep

class Bot():
    def __init__(self):

        self.char = '⬛'
        self.pos = [1, 1]

        self.total_moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.available_moves = []
        self.preferred_moves = [[0, 1], [1, 0]]
        self.other_moves = [[0, -1], [-1, 0]]


    def reg_traversal(self):
        magen.grid[self.pos[0]][self.pos[1]] = '⬜'
        move = random.choice(self.preferred_moves)
        self.pos[0] += move[0]
        self.pos[1] += move[1] #move this and line above to object traversal function
        magen.grid[self.pos[0]][self.pos[1]] = self.char
        magen.print_grid()

    def obstacle_traversal(self):
        lower_square = magen.grid[self.pos[0] + 1][self.pos[1]]
        right_square = magen.grid[self.pos[0]][self.pos[1] + 1]

        white_x_squares = {}
        white_y_squares = {}
        x_distance = []
        y_distance = []

        #if obstacle is below bot, find opening and minimum distance to it
        def lower_row_obstacle():
            lower_row = self.pos[0] + 1
            square_x_index = 0

            for square in magen.grid[lower_row]:
                if square == '⬜':

                    x_distance = abs(self.pos[1] - square_x_index)
                    white_x_squares.update({square_x_index: x_distance})
                square_x_index += 1

        # if obstacle is to the right of the bot, find opening and minimum distance to it
        def right_row_obstacle():
            right_row = self.pos[1] + 1
            square_y_index = 0
            for row in magen.grid:
                if row[right_row] == '⬜':

                    y_distance = abs(self.pos[0] - square_y_index) #fix this, distance shouldn't be a list
                    white_y_squares.update({square_y_index : y_distance})
                square_y_index += 1

        def min_distance_function(white_squares_list):
            square_removal_list = []
            for square1 in white_squares_list:
                for square2 in white_squares_list:
                    #print(white_squares_list)
                    #print(square1, white_squares_list[square1], square2, white_squares_list[square2])

                    if square1 < square2 and white_squares_list[square1] == white_squares_list[square2]:
                        square_removal_list.append(square1) #this causes the error
                        # because it shortens the dictionary during iteration
            for square in square_removal_list:
                white_squares_list.pop(square)

            distance_list = white_squares_list.values()
            index_list = list(white_squares_list.keys())
            min_distance = min(distance_list)
            global min_distance_index
            min_distance_index = index_list[list(distance_list).index(min_distance)]
            # print(min_distance_index)


        # moves bot to the opening, whether it's for a vertical wall or horizontal wall
        if lower_square == '🟦' and right_square == '🟦':
            lower_row_obstacle()
            right_row_obstacle()
            distance_list = []
            index_list = []

            # the following checks which wall the opening is in, then finds the nearest opening in the wall
            #that it can access

            # if at a corner, it checks the horizontal wall first for openings,
            # then if there are none it checks the vertical wall
            for number in range(0, self.pos[0]):
                if number in white_x_squares.keys():
                    distance_list.append(white_x_squares.get(number))
                    index_list.append(number)

            if len(distance_list) != 0:
                min_distance = min(distance_list)
                min_distance_index_s = index_list[list(distance_list).index(min_distance)]
                magen.grid[self.pos[0]][self.pos[1]] = '⬜'
                self.pos[0] += 0
                self.pos[1] += -1
                magen.grid[self.pos[0]][self.pos[1]] = self.char
                magen.print_grid()


            elif len(distance_list) == 0:
                for number in range(0, self.pos[1]):
                    if number in white_y_squares.keys():
                        distance_list.append(white_y_squares.get(number))
                        index_list.append(number)

                min_distance = min(distance_list)
                min_distance_index_s = index_list[list(distance_list).index(min_distance)]
                magen.grid[self.pos[0]][self.pos[1]] = '⬜'
                self.pos[0] += -1
                self.pos[1] += 0
                magen.grid[self.pos[0]][self.pos[1]] = self.char
                magen.print_grid()


        #if bot isn't at a corner and instead is at a horizontal wall, it finds the nearest opening in it
        #and moves the bot one square closer to that opening
        elif lower_square == '🟦':
            lower_row_obstacle()
            min_distance_function(white_x_squares)
            if min_distance_index > self.pos[1]:
                magen.grid[self.pos[0]][self.pos[1]] = '⬜'
                self.pos[0] += 0
                self.pos[1] += 1
                magen.grid[self.pos[0]][self.pos[1]] = self.char
                magen.print_grid()
            if min_distance_index < self.pos[1]:
                magen.grid[self.pos[0]][self.pos[1]] = '⬜'
                self.pos[0] += 0
                self.pos[1] += -1
                magen.grid[self.pos[0]][self.pos[1]] = self.char
                magen.print_grid()

        # if bot isn't at a corner or horizontal wall and is at a vertical wall, it finds the nearest
        #opening in it and moves the bot one square closer to that opening
        elif right_square == '🟦':
            right_row_obstacle()
            min_distance_function(white_y_squares)
            # while self.pos[1] != min_distance_index: # maybe take this line out completely
            if min_distance_index > self.pos[0]:
                magen.grid[self.pos[0]][self.pos[1]] = '⬜'
                self.pos[0] += 1
                self.pos[1] += 0
                magen.grid[self.pos[0]][self.pos[1]] = self.char
                magen.print_grid()
            if min_distance_index < self.pos[0]:
                magen.grid[self.pos[0]][self.pos[1]] = '⬜'
                self.pos[0] += -1
                self.pos[1] += 0
                magen.grid[self.pos[0]][self.pos[1]] = self.char
                magen.print_grid()









    #for m in self.total_moves:
        #if magen.grid[self.pos[0] + m[0]][self.pos[1] + m[1]] == '🟦':
           # if m in self.preferred_moves:
            #    self.preferred_moves.remove(m)
           # if m in self.other_moves:
            #    self.other_moves.remove(m)
            #else:
            #    self.available_moves.append(m)




def traversal():

    bot = Bot()

    while bot.pos != [9, 9]:

        if bot.pos == [9, 8]:
            magen.grid[9][8] = '⬜'
            bot.pos[1] += 1
            magen.grid[bot.pos[0]][bot.pos[1]] = bot.char
            magen.print_grid()

        for m in bot.preferred_moves:

            if magen.grid[bot.pos[0] + m[0]][bot.pos[1] + m[1]] == '🟦': #maybe change to while loop
                bot.obstacle_traversal()
                #sleep(1)  #maybe add this here





        bot.reg_traversal()

    print('Solved!')

#for traversal:
# while loop to keep the bot moving until it hits the end goal
# if the bot is next to a vertical or horizontal wall, then it must activate obstacle traversal