num = input("Enter a number: ")
if num.isdigit():
    print(num, "is a valid number")
else:
    print(num, "is not a valid number")
#Another if
if num.isalpha():
    print(num, "is more like a word")
else:
    pass
