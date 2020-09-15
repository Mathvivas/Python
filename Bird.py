bird_types = "crow, robin, parrot, eagle, sandpiper, hawk, piegon"

have_bird = input("Enter a bird type: ")

print(have_bird, "available is", have_bird.lower() in bird_types)

