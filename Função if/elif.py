weather = input('Enter a weather(sunny, snowy, rainy): ')
if weather.lower() == 'sunny':
    print('wear a shirt')
elif weather.lower() == 'rainy':
    print('Get an umbrella')
elif weather.lower() == 'snowy':
    print('wear a warm coat')
else:
    print('Sorry, not sure of what to suggest for', weather)
    