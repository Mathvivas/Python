L = []

while True:
    Resp = input('Deseja digitar um item? (Sim/Não): ').capitalize()
    if Resp == 'Sim':
         item = input('Digite algo para colocar na lista: ')
         L.append(item)
    elif Resp == 'Não':
        print(L)
        break     
    else:
        print('Resposta Inválida!')
        
            
                