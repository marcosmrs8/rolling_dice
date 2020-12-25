import random


def main():
    while True:
        resp = input('do you want to roll the dice? (y/n)\n')
        if resp.lower() == 'y':
            dice()
        elif resp.lower() == 'n':
            print('See ya! :D')
            return False
        else:
            print('wrong choice!try again')


def dice():
    rolling_dice = random.randint(1, 6)
    print(rolling_dice)
    return

main()