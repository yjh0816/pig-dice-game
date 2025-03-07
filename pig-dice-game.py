from random import randint, choice
import random


def select_level():
    print("1: EASY\n2: NORMAL\n3: HARD")
    level = int(input("Input the level:"))
    if level == 1:
        easy_mode()
    elif level == 2:
        normal_mode()
    elif level == 3:
        print("Not yet, wait plz")
    else:
        print("You can input only 1,2,3")

def normal_mode():
    u_score = 0
    c_score = 0
    while u_score < 100 and c_score < 100:

        print(f"user score:{u_score}\ncomputer score:{c_score}")
        u_score += user_play()

        print(f"user score:{u_score}\ncomputer score:{c_score}")
        c_score += n_computer_play()
    
    if u_score > c_score:
        print("Player Win")
    else:
        print("Computer is winner")

def easy_mode():
    u_score = 0
    c_score = 0
    while u_score < 100 and c_score < 100:

        print(f"user score:{u_score}\ncomputer score:{c_score}")
        u_score += user_play()

        print(f"user score:{u_score}\ncomputer score:{c_score}")
        c_score += e_computer_play()
    
    if u_score > c_score:
        print("Player Win")
    else:
        print("Computer is winner")

def roll_dice():
    roll_dice = randint(1,6)
    return roll_dice

def e_computer_play():
  cpu = 1
  cpu_prob = [1]
  final_value = 0
  turn_value = 0
  dice_value = 0

  while cpu <3:
    print("CPU's turn")
    dice_value = roll_dice()
    turn_value += dice_value
    print("CPU rolled", dice_value)
    cpu += 1
    if dice_value == 1:
      print("Turn score reset to 0")
      print(turn_value)
      print("***********************")
      print("Player's turn")
      return turn_value
      break
    else:
      cpu_prob.append (2)
      choice = random.choice(cpu_prob)
      if choice == 1:
        print("CPU chose to roll again")
        dice_value = roll_dice()
        turn_value += dice_value
        print("CPU rolled", dice_value)
        print("CPU's final value is ", turn_value)
        print("***********************")
        print("Player's turn")
        break
      else:
        print("CPU chose to hold")
        print("CPU's final value is ", turn_value)
        print("***********************")
        print("Player's turn")
        break
  return turn_value

def n_computer_play()-> int:
    is_play = True
    point_box = 0
    dice_value = 0
    br = 'r'
    while is_play == True:
        print(f"computer point box: {point_box}")
        dice_value, point_box, is_play = do_br(br, point_box)
        br = 'b'
    print(f"computer point box: {point_box}")
    # in the end, return value is point
    return point_box

def do_br(rb: str,point_box: int):
    is_play = True
    dice_value = roll_dice()

    if rb == 'b':
        # if select bank, get out of while
        is_play = False
    elif rb == 'r':
    # if first dice is one, game end 
        if dice_value == 1:
            print("dice value: 1")
            # user get lose point
            point_box = 0
            is_play = False
        else: 
            print(f"dice value: {dice_value}")
            point_box += dice_value

    return dice_value, point_box, is_play

def user_play()->int:
    is_play = True
    point_box = 0
    dice_value = 0

    while is_play == True:
        
        print(f"point box: {point_box}")
        rb = input("R or B: ")
        dice_value, point_box, is_play = do_br(rb, point_box)
    print(f"point box: {point_box}")
    # in the end, return value is point
    return point_box

if __name__ == '__main__':
    print("start")
    select_level()






