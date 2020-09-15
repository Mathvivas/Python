import numpy as np

# Função para ler as coordenadas de um ponto
def LerPonto(nomePonto):

    p = []
    eixos = ["x", "y", "z"]
    for d in range(len(eixos)):

        c = float(input("Digite a coordenada %s do ponto %s: " % (eixos[d], nomePonto)))
        p.append(c)

    ponto = np.array(p)
    print()
    return ponto

 

# programa principal
# Leitura dos pontos
# parâmetro nomePonto deve ser um caractere com o nome do ponto, por exemplo "A", com as aspas
O = LerPonto('O')
A = LerPonto('A')
B = LerPonto('B')

# calcular os vetores OA e OB
OA = A-O

OB = B-O

# calcular o vetor perpendicular aos vetores OA e OB
n = np.cross(OA,OB)

# converter o vetor para versor
n = n/(np.linalg.norm(n))

# equação geral do plano ax+by+cz+d=0
# no caso, a, b, e c são as componentes do vetor n
# foi escolhido arbitrariamente o ponto O como ponto pertencente ao plano para calcular d
d = - (n[0]*O[0] + n[1]*O[1] + n[2]*O[2])
print("%.3f·x + %.3f·y + %.3f·z + %.3f = 0" % (n[0], n[1], n[2], d))