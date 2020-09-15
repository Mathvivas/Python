i = 1
s = 0
while (1/i) > 10E-4:
    s = s + (1/i) 
    i += 1
print('%.4f' % s)
