seat_av = 10
while True:
    print(seat_av, 'available')
    seat_av -=1
    
    if seat_av == 0:
        print('No seats available')
        break
