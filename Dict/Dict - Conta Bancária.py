Conta = float(input('Digite o valor de sua conta bancária: '))

D = {}

Resp = 'O'
while Resp == 'O':
    Operação = input('(S)aque, (D)epósito, (P)agamento: ')
    if Operação == 'S':
        D['Saque'] = float(input('Digite o valor do saque (negativo): '))
        valor_restanteS = Conta + D['Saque']
    elif Operação == 'D':
        D['Depósito'] = float(input('Digite o valor do depósito: '))
        valor_restanteD = Conta + D['Depósito']
    else:
        D['Pagamento'] = float(input('Digite o valor do pagamento (negativo): '))
        valor_restanteP = Conta + D['Pagamento']
    
    print(D)
    
    Resp = input('Outra (O)peração ou (F)im: ')
    if Resp == 'F':
        print(valor_restanteS + valor_restanteD + valor_restanteP )
    