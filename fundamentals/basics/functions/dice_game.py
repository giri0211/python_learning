import random

def main():
    
    def roll_dice():
        dice_total = random.randint(1,6) + random.randint(1,6)
        return dice_total

    player1 = input('enter player 1 name\n')
    player2 = input('enter player 2 name\n')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1,'rolled', roll1)
    print(player2,'rolled', roll2)

    if roll1 > roll2:
        print(player1, 'won')
    elif roll1 < roll2:
        print(player2, 'won')
    else:
        print('its a tie')
main()