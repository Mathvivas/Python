D = {}
Resp = 's'
while Resp == 's':
    Prod = input('Digite o produto: ')
    Loja = input('Digite a loja: ')
    Preço = float(input('Digite o preço: '))
    print('%15s%15s%15s' % ('Prod', 'Loja' , 'Preço'))
    print('%15s%15s%15s' % (Prod, Loja , Preço))
    Resp = input('Deseja digitar outro produto, loja ou preço (s/n)?: ')
    
    
    
    