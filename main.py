import solver_algorithm as solvalg
import maze_generation as magen

def maze_runner():
    # not sure what to do, but basically this should combine all the parts together
    magen.create_maze() #create maze first, this creates the grid we use
    magen.print_grid()
    solvalg.traversal()



maze_runner()
