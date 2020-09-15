def bissexto(ano):
    # 2000 é divisível por 4 e 100, mas tbm é por 400, portanto é bissexto
    return ano % 400 == 0 or ano % 4 == 0 and not(ano % 100 == 0)


ano = int(input('Digite o ano: '))
x = print(bissexto(ano))

if ano % 400 == 0 or ano % 4 == 0 and not(ano % 100 == 0):
    print(str(ano) + ' é bissexto')

else:
    print(str(ano) + ' não é bissexto')
        
