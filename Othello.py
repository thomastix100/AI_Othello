

from Game import Game
import copy


class Othello(Game):
        
    def caso1(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        flanquea = 0
        entroVacio = 0
        lis = []
        while tamano != 0:
            if y == 8:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            y += 1
        return lista

    def caso2(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        entroVacio = 0
        flanquea = 0
        lis = []
        while tamano != 0:
            if x == 8 or y == 8:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            x += 1
            y += 1
            
        return lista

    def caso3(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        entroVacio = 0
        flanquea = 0
        lis = []
        while tamano != 0:
            if x == 8:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            x += 1
        return lista

    def caso4(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        entroVacio = 0
        flanquea = 0
        lis = []
        while tamano != 0:
            if x == 8 or y == -1:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            x += 1
            y -= 1
        return lista

    def caso5(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        entroVacio = 0
        flanquea = 0
        lis = []
        while tamano != 0:
            if y == -1:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            y -= 1
            
        return lista

    def caso6(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        entroVacio = 0
        flanquea = 0
        lis = []
        while tamano != 0:
            if x == -1 or y == -1:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            x -= 1
            y -= 1
        return lista

    def caso7(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        entroVacio = 0
        flanquea = 0
        lis = []
        while tamano != 0:
            if x == -1:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            x -= 1
        return lista

    def caso8(self,posx,posy,contrincante,lista,state,parametro,jugador):
        tamano = 8
        x = posx
        y = posy
        player = jugador
        copiaLis = lista.copy()
        contrincante = self.return_contricante(player)
        flanquea = 0
        lis = []
        entroVacio = 0
        while tamano != 0:
            if x == -1 or y == 8:
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                break
            if parametro == 0 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 1 and state[x][y] == player:
                break
            if parametro == 1 and flanquea == 0 and state[x][y] == player:
                return copiaLis
            if parametro == 1 and state[x][y] == 0 and entroVacio == 1:
                return copiaLis
            if state[x][y] == 0:
                entroVacio = 1
                if parametro == 1 and flanquea == 1:
                    return copiaLis
                if flanquea == 1 and parametro == 0:
                    lis.append(x)
                    lis.append(y)
                    if lis not in lista:
                        lista.append(lis)
                if parametro == 0:break
            if state[x][y] == contrincante:
                flanquea = 1
                if parametro == 1:
                    lista.append([x,y])
            tamano -=1
            x -= 1
            y += 1
        return lista

    def return_positions(self,contrincante, player, lista, state):
        tamano = len(state)
        for i in range(len(state)):
            if state[i].count(player) != 0:
                for j in range(len(state[i])):
                    posx = i
                    posy = j
                    if state[posx][posy] == player:
                        lista = self.caso1(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso2(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso3(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso4(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso5(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso6(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso7(posx,posy,contrincante,lista,state,0,player)
                        lista = self.caso8(posx,posy,contrincante,lista,state,0,player)
        return lista

    

    def return_contricante(self,player):
        contrincante = 0
        if player == 2:
            contrincante = 1
        elif player == 1:
            contrincante = 2
        return contrincante

    def actions(self,state):
        """Devemos retornar todas las posiciones donde podemos colocar una ficha"""
        lista = []
        player = self.to_move(state)
        contrincante = self.return_contricante(player)
        lista = self.return_positions(contrincante, player, lista, state)
        return lista

    def result(self,state, move):
        #Toma el tablero y la jugada, y retorna el tablero con la jugada.... osea el estado
        lista = []
        posx = move[0]
        posy = move[1]
        player = self.to_move(state)
        contrincante = self.return_contricante(player)
        lista = self.caso1(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso2(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso3(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso4(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso5(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso6(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso7(posx,posy,contrincante,lista,state,1,player)
        lista = self.caso8(posx,posy,contrincante,lista,state,1,player)
        tamanoLista = len(lista)
        i = 0
        auxList = copy.deepcopy(state)
        while tamanoLista != 0:
            auxLista = lista[i]
            posx = auxLista[0]
            posy = auxLista[1]
            auxList[posx][posy] = self.to_move(state)
            i += 1
            tamanoLista -= 1    
            
        auxList[move[0]][move[1]] = self.to_move(state)
        return auxList

    def utility(self, state, player):
        """Return the value of this final state to player."""
        """Devuelve el valor de este estado final al jugador"""
        finalista = 0
        countPlayer1 = 0
        countPLayer2 = 0

        for i in range(len(state)):
            countPlayer1 += state[i].count(1)
            countPLayer2 += state[i].count(2)
        
        if countPlayer1 > countPLayer2:
            finalista = 1
        if countPLayer2 > countPlayer1:
            finalista = -1
        return finalista

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        num = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != 0:
                    num += 1
       
        if num%2 == 0:
            return 2
        else:
            return 1

    def display(self, state):
        """Print or otherwise display the state."""
        """Imprime o muestra el estado"""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self):
        """Play an n-person, move-alternating game."""
        raise NotImplementedError
    