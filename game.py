class Game:
    """    
    Clase destinada a operaciones dentro de cada partida.
    Cada instancia de Game es una partida diferente con sus tableros y jugadores distintos.
    """

    def display(self):
        """
        Esta funcion recibe el tablero en forma de lista y crea un string
        con ella para poder visualizar de mejor forma el tablero en la consola.
        """    
        inp = self.tablero
        tablero = "\nTablero: \n\n"
        for i in range(3):
            filaStr = " │ ".join(inp[0 + 3*i:3 + 3*i])
            if(i <2 ):
                tablero = tablero + "   " + filaStr + "\n" + "  ───┼───┼───\n"
            else:
                tablero = tablero + "   " + filaStr + "\n" 

        return tablero

    def comprobar(self):
        """
        Esta funcion recibe el tablero y devuelve un booleano true si la partida ha terminado.
        El segundo parametro que devuelve es el jugador ganador. En el caso de empate devuelve un "-"
        Si la partida todavia no termina devuelve un booleano false.
        """
        #Comprobacion por filas
        for i in range(3):
            if self.__comprTrios(self.tablero[0+i*3:3+i*3]) & (self.tablero[0+i*3:3+i*3][0] != ' '):
                self.ganador = self.tablero[0+i*3:3+i*3][0]
                return True
        
        #Comprobacion por columnas
        for i in range(3):
            if self.__comprTrios([self.tablero[0+i], self.tablero[3+i], self.tablero[6+i]]) & ([self.tablero[0+i], self.tablero[3+i], self.tablero[6+i]][0] != ' '):
                self.ganador = [self.tablero[0+i], self.tablero[3+i], self.tablero[6+i]][0]
                return True

        #Comprobar diagonales
        if self.__comprTrios([self.tablero[0], self.tablero[4], self.tablero[8]]) & ([self.tablero[0], self.tablero[4], self.tablero[8]][0] != ' '): #diag principal
            self.ganador = [self.tablero[0], self.tablero[4], self.tablero[8]][0]
            return True

        if self.__comprTrios([self.tablero[2], self.tablero[4], self.tablero[6]]) & ([self.tablero[2], self.tablero[4], self.tablero[6]][0] != ' '):  #diagonal secundaria
            self.ganador = [self.tablero[2], self.tablero[4], self.tablero[6]][0]
            return True

        #Casillas completas (aka punto muerto)
        if self.tablero.count(' ') == 0:
            self.ganador = "-"
            return True

        #Default state
        return False

    def jugar(self, jugador, pos):
        if self.__validarPosicion(pos):
            self.tablero[pos-1] = jugador
            return True
        else:
            return False

    def __comprTrios(self, trio):
        """
        Funcion de validacion auxiliar para self.comprobar()
        """
        if trio.count(trio[0]) == 3:
            return True
        else:
            return False

    def __validarPosicion(self, pos):
        #revisa si la posicion esta entre 1 y 9
        if [1,2,3,4,5,6,7,8,9].count(pos) != 1:
            return False
        
        #Revisa si la posicion esta vacia
        if self.tablero[pos - 1] != ' ':
            return False
        return True

    def __init__(self):
        self.ganador = "-"
        self.tablero = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' '
        ] 


if __name__ == "__main__":
    print("Este script es un contendor de clases. No se deve ejecutar como archivo principal.")