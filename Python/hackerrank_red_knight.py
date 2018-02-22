#!/bin/python3

import sys

def genLegalMoves(x,y,board):
    newMoves = []
    moveChoices = [(-1,-2), (1,-2), (2,0), (1,2), (-1,2), (-2,0)]
    
    for i in moveChoices:
        newX = x + i[0]
        newY = y + i[1]
        if legalSpot(newX,board) and legalSpot(newY, board):
            newMoves.append((newX,newY))
    # print(newMoves)           
    return newMoves

def legalSpot(pos, board):
    return pos >= 0 and pos < board
    
def printShortestPath(n, x, y, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    # need to keep track of previously explored spaces
    prev_explored = []
    # keep track of all paths to be checked
    paths_to_check[(x,y)]
    
    # while loop to keep going while there are paths to explore
    while paths_to_check:
        path = paths_to_check.pop(0)
        # get last node from path
        node = path[-1]
        # if node hasn't been explored
        if node not in prev_explored:
            spaces = genLegalMoves(path[0],path[1],n)
            # construct a new list of spaces to go over
            for space in spaces:
                new_path = list(path)
                new_path.append(space)
                paths_to_check.append(new_path)
                # return path if space is goal
                if space == (i_end, j_end):
                    return new_path
            # mark space as explored
            prev_explored.append(node)
    # if there's not a legal path
    print('Impossible')

if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)

