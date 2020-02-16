"""ESte metodo te saca las jugadas que puedes hacer a nivel de filas y columnas del Othelo,
La siguiente version sera sacar los movimientos de las diagonales"""

def return_positions(self,contrincante, player, lista, state,parametro):
        tamano = len(state)
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
                            if parametro == 1:
                                lisT.append(j)
                                lisT.append(i)
                            else:
                                lisT.append(i)
                                lisT.append(j)
                            if lisT not in lista:
                                lista.append(lisT)
                                lisT = []
                            verdeEnNegra = 0

                    if state[i][j] == player:
                        estaDentroDeNegras = 1
                        estaDentroDeBlancas = 0

                        if verdeEnBlancas == 1:
                            if parametro == 1:
                                lisT.append(posY)
                                lisT.append(posX)
                            else:
                                lisT.append(posX)
                                lisT.append(posY)

                            if lisT not in lista:
                                lista.append(lisT)
                                lisT = []
                            verdeEnBlancas = 0
        return lista