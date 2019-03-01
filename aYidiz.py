import math
from simpleai.search import SearchProblem, astar
import cv2
import numpy as np


class MazeSolver(SearchProblem):
    def __init__(self, board):
        self.board = board
        self.goal = (0, 0)
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x].lower() == "o":
                    self.initial = (x, y)
                elif self.board[y][x].lower() == "x":
                    self.goal = (x, y)

        super(MazeSolver, self).__init__(initial_state=self.initial)

    def actions(self, state):
        actions = []
        for action in COSTS.keys():
            newx, newy = self.result(state, action)
            if self.board[newy][newx] != "0":
                actions.append(action)
        return actions

    def result(self, state, action):
        x, y = state

        if action.count("up"):
            y -= 1
        if action.count("down"):
            y += 1
        if action.count("left"):
            x -= 1
        if action.count("right"):
            x += 1

        new_state = (x, y)

        return new_state

    def is_goal(self, state):
        return state == self.goal

    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal
        return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)


if __name__ == "__main__":

    img = cv2.imread('/home/avesta/Desktop/CalismaDizini/maze3.jpeg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thin = cv2.ximgproc.thinning(gray, None, cv2.ximgproc.THINNING_ZHANGSUEN)

    print(thin[100,100])
    for y in range(len(thin)):
        for x in range(len(thin[y])):

            if thin[y][x] == 255:
                thin[y][x] = 1


    [qq,tt]=thin.shape


    table = [[0 for i in range(tt)] for j in range(qq)]

    qq = qq
    tt = tt
    print('qqqqqqqq', qq, tt)
    #print(table[0][469])
    #print(thin.shape)

    for y in range(469):
        #print('y====',y)
        for x in range(476):
            #print('x===',x)
            table[y][x] = thin[y][x]
    """
    y=0
    while y < 469:
        x=0
        #print('y====', y)
        while x<476:
            #print('x===', x)
            table[y][x] = thin[y][x]
            x+=1
        y+=1
    """
    table[440][0] = 'o'
    table[457][475] = 'x'
    #print(table[0][:])
    b = """"""
    for y in range(qq):
        for x in range(tt):
            b += str(table[y][x])
        b += '\n'

    b = [list(x) for x in b.split("\n") if x]

    cost_regular = 1.0
    cost_diagonal = 1.7

    COSTS = {
        "up": cost_regular,
        "down": cost_regular,
        "left": cost_regular,
        "right": cost_regular,
    }


    print(b)
    problem = MazeSolver(b)


    result = astar(problem, graph_search=True)

    print(result,type(result))

    path = [x[1] for x in result.path()]

    print()

    for y in range(len(thin)):
        for x in range(len(thin[y])):
            if (x, y) == problem.initial:
                #print('o', end='')
                img[y][x][2] = 255
                img[y][x][1] = 0
                img[y][x][0] = 0
            elif (x, y) == problem.goal:
                #print('x', end='')
                img[y][x][2] = 255
                img[y][x][1] = 0
                img[y][x][0] = 0
            elif (x, y) in path:
                #print('.', end='')
                img[y][x][2] = 255
                img[y][x][1] = 0
                img[y][x][0] = 0




    # resmin boyutlandırmak için ekledik
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()