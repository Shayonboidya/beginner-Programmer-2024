import random
secret_number = random.randint(1,9)
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit:
    guess = int(input('choice any number: '))
    guess_count +=1
    if guess == secret_number:
        print('you win...')
        break
else:
    print("\nyou lost.")    
    
    