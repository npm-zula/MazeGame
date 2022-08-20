import curses

import queue
import time


maze = [
    ["#", "#", "#", "#", "O", "#", "#", "#", "#", ],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", ],
    ["#", " ", " ", " ", " ", "#", "#", " ", "#", ],
    ["#", " ", " ", "#", " ", " ", "#", " ", "#", ],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", ],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", ],
    ["#", " ", " ", "#", " ", " ", " ", " ", "#", ],
    ["#", "#", "#", "#", "#", "#", "X", "#", "#", ]
]

def print_maze(maze, stdscr, path =[]):
    cyan = curses.color_pair(1)
    magenta = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if(i,j) in path:
                stdscr.addstr(i,j*4,"X",cyan)
            else:
                stdscr.addstr(i,j*4, value, magenta)

def find_path(maze, stdscr):
    start = "O"
    end  =  "X"

    start_pos = getStartPos(maze, start)

    qu = queue.Queue() # Queue creation for shortest distant algorithm
    qu.put((start_pos, [start_pos]))

    visited  = set() # set to put the nodes when they are visited by the loop

    while not qu.empty():
        curr_pos, path = qu.get()

        row,col = curr_pos # temp variables for further understanding

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.4)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbours = findNeighbour(maze, row, col)

        for neighbour in neighbours:
            if neighbour in visited:
                continue

            r,c = neighbour
            if(maze[r][c] == "#"):
                continue

            new_path = path + [neighbour] # path for the neighbour (new node) will be old path + this node
            qu.put((neighbour, new_path)) # add to queue 
            visited.add(neighbour)        # add to visited so that doesnot check again


def findNeighbour(maze,row,col):
    neighbours = []

    #UP
    if(row > 0):
        neighbours.append((row-1,col))

    #DOWN
    if row + 1 < len(maze):
        neighbours.append((row+1,col)) 

    # LEFT
    if(col > 0):
        neighbours.append((row,col-1))

    # RIGHT
    if(col + 1 < len(maze[0])):
        neighbours.append((row,col+1))

    
    return neighbours

def getStartPos(maze,startSymbol):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == startSymbol:
                return i,j

def main(stdscr):
    
    curses.init_pair(1,curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    find_path(maze, stdscr)

    # # black_cyan = curses.color_pair(1)
    # stdscr.clear()
    # print_maze(maze, stdscr)
    # # stdscr.addstr(5, 5, "hello jee", black_cyan)
    # stdscr.refresh()
    # stdscr.getch()
    stdscr.getch()

curses.wrapper(main)
