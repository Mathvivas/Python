secret_number = "5"
while True:
    number_guess = input('Guess a number 1 to 5: ')
    if number_guess == secret_number:
        print('Yes!', number_guess, 'is correct!')
        break
    else:
        print(number_guess, 'is incorrect')
        