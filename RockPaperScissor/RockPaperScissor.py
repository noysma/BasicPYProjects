import random
import RPS as hands

human_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors '))
computer_choice = random.randint(0,2)
possibilities = [hands.rock, hands.paper, hands.scissors]

if human_choice < 0 or human_choice > 2:
    print('Choose a valid option')
else:
    if human_choice == computer_choice:
        print('/IT\'S A DRAW')
    elif human_choice == 0 and computer_choice == 2:
        print('You choose\n', possibilities[human_choice], '\nComputer choose\n', possibilities[computer_choice])
        print('/YOU WIN')
    elif human_choice == 1 and computer_choice == 0:
        print('You choose\n', possibilities[human_choice], '\nComputer choose\n', possibilities[computer_choice])
        print('/YOU WIN')
    elif human_choice == 2 and computer_choice == 1:
        print('You choose\n', possibilities[human_choice], '\nComputer choose\n', possibilities[computer_choice])
        print('/YOU WIN')
    else:
        print('You choose\n', possibilities[human_choice], '\nComputer choose\n', possibilities[computer_choice])
        print('/YOU LOSE')