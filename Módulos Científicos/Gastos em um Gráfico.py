import matplotlib.pyplot as plt

categ = ['Casa', 'Alimentação', 'Saúde', 'Transporte', 'Educação', 'Lazer']

gastos = {
        'Casa' : 0.00,
        'Alimentação' : 0.00,
        'Saúde' : 0.00,
        'Transporte' : 0.00,
        'Educação' : 0.00,
        'Lazer' : 0.00,
        'Outros' : 0.00
}

op = ' '
while op != '':
    c = input('Categoria: ')
    g = float(input('Gasto: '))
    if c in categ:
        gastos[c] += g
    else:
        gastos['Outros'] += g
    op = input('Digite ENTER para encerrar...')
print(gastos)

categ = list(gastos.keys())
valores = list(gastos.values())
plt.title('Gastos')
plt.pie(valores, labels=categ, autopct='%1.4f%%')
plt.axis('equal')
plt.tight_layout()
plt.show()
