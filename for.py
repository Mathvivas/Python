t = 'Banana'
print(t[0:6])


total_de_bananas = 0

s = "bananabananabananabananabananabananabanana"

for letras in range(len(s)):
    if(s[letras: letras+1] == "a"):
        total_de_bananas += 1

print(total_de_bananas)



total_de_bananas = 0

s = "bananabananabananabananabananabananabanana"

for letras in range(len(s)):
    if(s[letras: letras+6] == "banana"):
        total_de_bananas += 1

print(total_de_bananas)