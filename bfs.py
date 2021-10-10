import random
import time
import copy
import plotly.graph_objects as go

######################################################################################
# The cell create a 3x3 array by using 2D list. Firstly a list of 9 numbers is created
# using range function, shuftle function randomies the position of entries. The nested
# for loop initilizes the array if entry is 0 it is filled with space and than the text
# displayed
######################################################################################
def generateSequence():
 numbers = list(range(0,9))
 random.shuffle(numbers)
 array = []
 for row in range(3):
    col = []
    for column in range(3):
        entry = numbers.pop()
        col.append(entry)   
    array.append(col)
 display(array)
 return array

#####################################################################################
# This function returns the index of 0 in the puzzle
######################################################################################
def spaceIndex(array):
    for row in range(3):
     for column in range(3):
        if array[row][column] == 0:
            return row, column    
#####################################################################################
# This function is used to display the using for loop
######################################################################################
def display(array):
    print("*****************************")
    for row in range(3):
     for column in range(3):
        print(array[row][column], end=' ')    
     print()


#####################################################################################
# These are helper functions to check movement of 0 if it is within board
######################################################################################
def moveUp(row):
    if row > 0:
        return True

def moveDown(row):
    if row < 2:
        return True

def moveRight(column):
    if column < 2:
        return True

def moveLeft(column):
    if column > 0:
        return True

#####################################################################################
# This basic functionality of this function is to create neighbouring stateSets of the
# current state. It takes one argument which is any state and than returns the 4 state
# sets of it.
######################################################################################
def stateSet(state):
    row, column = spaceIndex(state)
    neighbours = []
    
    if (moveUp(row)):
        tmp = state[row-1][column]
        newState = copy.deepcopy(state)
        newState[row][column] = tmp
        newState[row-1][column] = 0
        neighbours.append(newState)
    

    if (moveDown(row)):
        tmp = state[row+1][column]
        newState = copy.deepcopy(state)
        newState[row][column] = tmp
        newState[row+1][column] = 0
        neighbours.append(newState)

    if (moveLeft(column)):
        tmp = state[row][column-1]
        newState = copy.deepcopy(state)
        newState[row][column] = tmp
        newState[row][column-1] = 0
        neighbours.append(newState)

    if (moveRight(column)):
        tmp = state[row][column+1]
        newState = copy.deepcopy(state)
        newState[row][column] = tmp
        newState[row][column+1] = 0
        neighbours.append(newState)
    return neighbours

########################################################################################
# The basic functionality of this function is to implement BFS algorithm on the 8 puzzle
# problem. The function takes two positional arguments one is starting state and the Goal
# state. time.time() starts calculating time when function started it's execution to keep
# record of total time taken by code to execute. VisitedState list keep record of the state
# which has been visited. Queue is initiliazed to implement BFS.
########################################################################################
def bfs(initialState, goalState):
    start = time.time()
    queue = []
    visitedState = []
    path = []
    queue.append(initialState)
    visitedState.append(initialState)
    while queue:
        currentState = queue.pop(0)
        path.append(currentState)
        if currentState == goalState:
            display(currentState)
            break

        for neighbourState in stateSet(currentState):
            if neighbourState not in visitedState:
                visitedState.append(neighbourState)
                queue.append(neighbourState)
    end = time.time()
    timeTaken = end - start
    return timeTaken, path

if __name__=='__main__':
    goalState = [[1,2,3], [4,0,5], [6,7,8]]
    initialState = generateSequence()
    print("------------BFS has started execution------------")
    timeTakenBFS, pathBFS = bfs(initialState, goalState)
    print("Time taken by BFS : " + str(timeTakenBFS/60) + " minutes")
    