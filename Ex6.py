##from sense_hat import SenseHat
##sense = SenseHat()
import time
import random

b=(0,0,0)
r=(255,0,0)
g=(0,255,0)
w=(255,255,255)
pitch = sense.get_orientation()['pitch']
roll = sense.get_orientation()['roll']
board = [[b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b], 
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],
         [b,b,b,b,b,b,b,b],]

def Ex6A():
    while True:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        print("pitch{0} roll{1}".format(round(pitch,0),round(roll,0)))
        time.sleep(0.05)

def Ex6B():## Display a Marble.
    board = [[b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b],
             [b,b,b,b,b,b,b,b] ]
    y = 2
    x = 2
    board[y][x] = w
    board_1D = sum(board,[])
    print(board_1D)
    sense.set_pixels(board_1D)

def moveMarble(pitch,roll,x,y):
    newx = x
    newy = y
    if 1<pitch<179 and x != 0:
        newx -= 1 #Move left
    elif 359>pitch>179 and x != 7:
        newx += 1 #Move right
    if 1<roll<179 and y != 0:
        newy += 1
    elif 359>roll>179 and y != 7:
        newy -= 1
    newx,newy = checkWall(x,y,newx,newy)
    return newx,newy

def Ex6C():
    while True:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        x,y = moveMarble(pitch,roll,x,y)
        board[y][x] = w
        sense.set_pixels(sum(board,[]))
        time.sleep(0.5)
        board[y][x] = b


def checkWall(x,y,newx,newy):
    if board[newy][newx] != r:
        return newx,newy
    elif board[newy][x] != r:
        return x,newy
    elif board[y][newx] != r:
        return newx,y
    else:
        return x,y

def Ex6D():
    board = [[r,r,r,r,r,r,r,r],
             [r,b,b,b,b,b,b,r], 
             [r,b,b,b,b,b,b,r], 
             [r,b,b,b,b,b,b,r], 
             [r,b,b,b,b,b,b,r], 
             [r,b,b,b,b,b,b,r], 
             [r,b,b,b,b,b,b,r], 
             [r,r,r,r,r,r,r,r]]
    #board = [[r,r,r,b,b,b,b,r], 
    #         [r,b,b,b,b,b,b,r],
    #         [b,b,b,b,b,r,b,r],
    #         [b,r,r,b,r,r,b,r],
    #         [b,b,b,b,b,b,b,b],
    #         [b,r,b,r,r,b,b,b],
    #         [b,b,b,r,b,b,b,r], 
    #         [r,r,b,b,b,r,r,r] ]
    y = 1
    x = 1
    while True:
        x,y = moveMarble(pitch,roll,x,y)
        board[y][x] = w
        sense.set_pixels(sum(board,[]))
        time.sleep(0.5)
        board[y][x] = b

def Ex6E():
    board = [[r,r,r,b,b,b,b,r], 
             [r,b,b,b,b,b,b,r],
             [b,b,b,b,g,r,b,r],
             [b,r,r,b,r,r,b,r],
             [b,b,b,b,b,b,b,b],
             [b,r,b,r,r,b,b,b],
             [b,b,b,r,b,b,b,r], 
             [r,r,b,b,b,r,r,r] ]
    game_over = False
    while not game_over:
        pitch = sense.get_orientation()['pitch']
        roll = sense.get_orientation()['roll']
        x,y = moveMarble(pitch,roll,x,y)
        board[y][x] = w
        sense.set_pixels(sum(board,[]))
        time.sleep(0.5)
        board[y][x] = b
        if g not in board:
            game_over = True
    else:
        sense.clear()
        sense.show_message('Yay!!')

def Optional():
    targX = random.randint(1,7)
    targY = random.randint(1,7)
    while board[targY][targX] != 'r':
        board[targY][targX] = g
        time.sleep(10)
        board[targY][targX] = b
    else:
        targX = random.randint(1,7)
        targY = random.randint(1,7)
