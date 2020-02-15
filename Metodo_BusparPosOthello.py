state = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

lista = []


player = 2
tamano = len(state)

#Para mirar si una tupla esta en una lista
#(1,2) in lis

"""for i in range(len(state)):
    for j in range(len(state[i])):
        if state[i][j] == player:
            lis.append((i,j))"""

contrincante = 0
if player == 2:
    contrincante = 1
elif player == 1:
    contrincante = 2



for i in range(len(state)):
    if state[i].count(player) != 0 and (tamano - state[i].count(0)) != 1:
        estaDentroDeBlancas = 0
        estaDentroDeNegras = 0
        verdeEnNegra = 0
        verdeEnBlancas = 0
        posX = 0
        posY = 0
        lisT = []
        for j in range(len(state[i])):
            
            if state[i][j] == contrincante:
                if estaDentroDeNegras == 1:
                    verdeEnNegra = 1
                if estaDentroDeBlancas == 1:
                    verdeEnBlancas = 1

            if state[i][j] == 0:
                posX = i
                posY = j
                estaDentroDeBlancas = 1
                estaDentroDeNegras = 0

                if verdeEnNegra == 1:
                    lisT.append(i)
                    lisT.append(j)
                    lista.append(lisT)
                    lisT = []
                    verdeEnNegra = 0

            if state[i][j] == player:
                estaDentroDeNegras = 1
                estaDentroDeBlancas = 0

                if verdeEnBlancas == 1:
                    lisT.append(posX)
                    lisT.append(posY)
                    lista.append(lisT)
                    lisT = []
                    verdeEnBlancas = 0
                



print(lista)