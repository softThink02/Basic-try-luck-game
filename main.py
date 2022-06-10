import random

# R = ROCK 
# S = SCISSORS
# P = PAPER

choices = ['S', 'R', 'P']
CPU = random.choice(choices)
Player = None
print('Welcome on board!!!')
while Player not in choices:
    print('I hope you know the rules?')
    Player = input('S, R or P >>> :  ').upper()
    if CPU == Player:
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('TIE!')
        Player = input('PLAY AGAIN >>> ').upper()
        CPU = random.choice(choices)
        if CPU == Player:
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('TIE!')
            Player = input('PLAY AGAIN >>> ').upper()
        elif Player == 'P' and CPU == 'S':
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('YOU LOST! ')
        elif CPU == 'P' and Player == 'R':
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('YOU LOST!')
        elif CPU == 'R' and Player == 'P':
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('YOU WON!!!')
        elif CPU == 'S' and Player == 'R':
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('YOU WON!!!')
        elif CPU == 'R' and Player == 'S':
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('YOU LOST!')
        elif CPU == 'P' and Player == 'S':
            print('Computer : ', CPU)
            print('you picked : ', Player)
            print('YOU WON!!!')
    elif Player == 'P' and CPU == 'S':
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('YOU LOST! ')
    elif CPU == 'P' and Player == 'R':
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('YOU LOST!')
    elif CPU == 'R' and Player == 'P':
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('YOU WON!!!')
    elif CPU == 'S' and Player == 'R':
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('YOU WON!!!')
    elif CPU == 'R' and Player == 'S':
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('YOU LOST!')
    elif CPU == 'P' and Player == 'S':
        print('Computer : ', CPU)
        print('you picked : ', Player)
        print('YOU WON!!!')
    