from game import Game

#Main loop
while True:
    partida = Game()

    print(partida.display())

    #loop de partida
    while partida.comprobar() == False:

        pos = int(input("Juega el jugador X: "))
        while partida.jugar("X", pos) == False:
            print("Posicion invalida. Las posiciones van del 1 al 9.")
            pos = int(input("Juega el jugador X: "))

        print(partida.display())

        if partida.comprobar():
            break

        pos = int(input("Juega el jugador O: "))
        while partida.jugar("O", pos) == False:
            print("Posicion invalida. Las posiciones van del 1 al 9.")
            pos = int(input("Juega el jugador O: "))

        print(partida.display())

    if partida.ganador == "-":
        print("=============================\n   Es un empate!!\n=============================")        
    else:
        print("=============================\n   El ganador es " + partida.ganador + "\n=============================")

    continuar = input("\nJugar otra vez?(si/no)")
    if continuar.upper() == "NO":
        break


input("\nGracias por jugar!! (Pesiona ENTER para salir)")
