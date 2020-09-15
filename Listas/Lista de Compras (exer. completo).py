def ExibirTabela(L):
    L.sort()
    s = 0
    print('%8s\t%10s\t%8s' %('Produto', 'Quantidade', 'Preço')) #1º linha da tabela
    for item in L: #item = Produto, Quantidade ou Preço
        print('%8s\t%10.2f\t%8.2f' %tuple(item)) #transforma a sublista em uma tupla, onde o 1° item é uma string....
        s += item[1]*item[2] #Quantidade * Preço
    print('Total = R$ %.2f' %s)


n = int(input('Digite o número de itens: '))
L = []
c = 1

for i in range(n):
    produto = input('Entre com o %i° produto: ' %c).capitalize()
    quant = float(input('Entre com a quantidade: '))
    preço = 0
    L.append([produto, quant, preço])
    c += 1

print(L)

ExibirTabela(L)


answer = 'S'   # Necessário para comecar o looping
while answer == 'S':
    print('\n\n Consulta de Preços')
    produto = input('Digite o produto: ').capitalize()
    for item in L:   #Olha a lista inteira e procura pelo nome do produto
        if item[0] == produto:
            preço = float(input('Valor do produto (unidade), use ponto, não vírgula: '))
            item[2] = preço
    ExibirTabela(L)
    answer = input('Deseja mudar outro preço?(S/N): ').upper()
 