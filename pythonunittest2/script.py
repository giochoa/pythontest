from random import randint


def guess_game(guess, answer):

    if guess > 0 and int(guess) < 11:
        if guess == answer:
            print('your a genius')
            return True
    else:
        print('number i said')  
        return False
        
answer = randint(1, 10)

if __name__ == '__main__':  

    while True:
            try:
                guess = int(input('guess a number from 1 ~ 10  '))
                if (guess_game(guess, answer)):
                    break    
            except ValueError:
                print('a number please')
                continue    