mesExtenso = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

dia = input("Digite o dia: ")
mes = int(input("Digite o mês: "))
ano = input("Digite o ano: ")

data = [dia, mesExtenso[mes-1], ano]

dataExtenso = ' de '.join(data)

print(dataExtenso)