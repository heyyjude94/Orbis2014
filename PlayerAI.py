import random
from tronclient.Client import *

class PlayerAI():
    def __init__(self):
        return

    def new_game(self, game_map, player_lightcycle, opponent_lightcycle):
        return

    def get_move(self, game_map, player_lightcycle, opponent_lightcycle, moveNumber):
        my_position = player_lightcycle['position']
        my_x = my_position[0]
        my_y = my_position[1]
        my_direction = player_lightcycle['direction']
        randMove = self.next_move(my_x, my_y, game_map, my_direction)
        if randMove == 3:
            return PlayerActions.MOVE_LEFT
        elif randMove == 1:
            return PlayerActions.MOVE_RIGHT
        elif randMove == 2:
            return PlayerActions.MOVE_DOWN
        else:
            return PlayerActions.MOVE_UP

    def next_move(self, x, y, game_map, direction):
        #checks current direction
        print direction
        if direction == 2:
            down = self.check_down(x, y, game_map)
            if down:
                return 2
            else:
                return self.find_next_step(x, y, game_map, direction)
        elif direction == 3:
            left = self.check_left(x, y, game_map)
            if left:
                return 3
            else:
                return self.find_next_step(x, y, game_map, direction)
        elif direction == 1:
            right = self.check_right(x, y, game_map)
            if right:
                return 1
            else:
                return self.find_next_step(x, y, game_map, direction)
        else:
            up = self.check_up(x,y,game_map)
            if up:
                return 0
            else:
                return self.find_next_step(x, y, game_map, direction)

    def find_next_step(self, x, y, game_board, direction):
        if direction is 3:
            down = self.check_down(x,y, game_board)
            up = self.check_up(x, y, game_board)
            print self.go_up(y, game_board)
            if self.go_up(y, game_board):
                if up:
                    return 0
                else:
                    return 2
            else:
                if down:
                    return 2
                else:
                    return 0

        elif direction is 1:
            print "going right"
            down = self.check_down(x,y, game_board)
            up = self.check_up(x, y, game_board)
            if self.go_up(y, game_board):
                if up:
                    return 0
                else:
                    return 2
            else:
                if down:
                    return 2
                else:
                    return 0

        elif direction is 2:
            right = self.check_right(x, y, game_board)
            left = self.check_left(x, y, game_board)
            if self.go_left(x, game_board):
                if left:
                    return 3
                else:
                    return 1
            else:
                if right:
                    return 1
                else:
                    return 3

        else:
            right = self.check_right(x,y, game_board)
            left = self.check_left(x, y, game_board)
            if self.go_left(x, game_board):
                if left:
                    return 3
                else:
                    return 1
            else:
                if right:
                    return 1
                else:
                    return 3


    def go_up(self, y, game_board):
        result = y*(1.0)/(len(game_board[0]) - 1)
        print result
        if result > 0.5:
            return True
        else:
            return False

    def go_left(self, x, game_board):
        result = (x*1.0)/(len(game_board[0]) - 1)
        if result > 0.5:
            return True
        else:
            return False

    def check_left(self, x, y, game_board):
        if x <= 0:
            return False
        elif game_board[x-1][y] != "empty":
            return False
        else:
            return True

    def check_right(self, x, y, game_board):
        if x >= (len(game_board) - 1):
            return False
        elif game_board[x+1][y] != "empty":
            return False
        else:
            return True

    def check_down(self, x, y, game_board):
        if y>=(len(game_board[0])-1):
            return False
        elif game_board[x][y+1] != "empty":
            return False
        else:
            return True

    def check_up(self, x, y, game_board):
        if y <= 0:
            return False
        elif game_board[x][y-1] != "empty":
            return False
        else:
            return True




'''

8888888 8888888888 8 888888888o.      ,o888888o.     b.             8 
      8 8888       8 8888    `88.  . 8888     `88.   888o.          8 
      8 8888       8 8888     `88 ,8 8888       `8b  Y88888o.       8 
      8 8888       8 8888     ,88 88 8888        `8b .`Y888888o.    8 
      8 8888       8 8888.   ,88' 88 8888         88 8o. `Y888888o. 8 
      8 8888       8 888888888P'  88 8888         88 8`Y8o. `Y88888o8 
      8 8888       8 8888`8b      88 8888        ,8P 8   `Y8o. `Y8888 
      8 8888       8 8888 `8b.    `8 8888       ,8P  8      `Y8o. `Y8 
      8 8888       8 8888   `8b.   ` 8888     ,88'   8         `Y8o.` 
      8 8888       8 8888     `88.    `8888888P'     8            `Yo
      
                                Quick Guide
                --------------------------------------------
                      Feel free to delete this comment.

        1. THIS IS THE ONLY .PY OR .BAT FILE YOU SHOULD EDIT THAT CAME FROM THE ZIPPED STARTER KIT

        2. Any external files should be accessible from this directory

        3. new_game is called once at the start of the game if you wish to initialize any values

        4. get_move is called for each turn the game goes on

        5. game_map is a 2-d array that contains values for every board position.
                example call: game_map[2][3] == POWERUP would evaluate to True if there was a powerup at (2, 3)

        6. player_lightcycle is your lightcycle and is what the turn you respond with will be applied to.
                It is a dictionary with corresponding keys: "position", "direction", "hasPowerup", "isInvincible", "powerupType"
                position is a 2-element int array representing the x, y value
                direction is the direction you are travelling in. can be compared with Direction.DIR where DIR is one of UP, RIGHT, DOWN, or LEFT
                hasPowerup is a boolean representing whether or not you have a powerup
                isInvincible is a boolean representing whether or not you are invincible
                powerupType is what, if any, powerup you have

        7. opponent_lightcycle is your opponent's lightcycle. Same keys and values as player_lightcycle

        8. You ultimately are required to return one of the following:
                                                PlayerAction.SAME_DIRECTION
                                                PlayerAction.MOVE_UP
                                                PlayerAction.MOVE_DOWN
                                                PlayerAction.MOVE_LEFT
                                                PlayerAction.MOVE_RIGHT
                                                PlayerAction.ACTIVATE_POWERUP
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_UP
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_DOWN
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_LEFT
                                                PlayerAction.ACTIVATE_POWERUP_MOVE_RIGHT
                
        9. If you have any questions, contact challenge@orbis.com

        10. Good luck! Submissions are due Sunday, September 21 at noon. You can submit multiple times and your most recent submission will be the one graded.
 
'''
