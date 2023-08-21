
print("Ingresa los juegos ganados por el jugador A")
jugador_a = int(input())
print("Ingresa los juegos ganados por el jugador B")
jugador_b = int(input())

# Cuando gana el jugador A o el jugador B
if jugador_a>=7 and (jugador_b+2) < jugador_a:
    print("Juego inválido")
elif jugador_b>=7 and (jugador_a+2) < jugador_b:
    print("Juego inválido")
elif jugador_a>=6 and jugador_b+2 <= jugador_a:
    print("Jugador A ha ganado")
elif jugador_b>=6 and (jugador_a+2) <= jugador_b:
    print("Jugador B ha ganado")
elif jugador_a<6 and jugador_b<6:
    print("El juego aún no termina")
elif jugador_a>=5 and jugador_b>=6 and (jugador_b+2>jugador_a or jugador_b<jugador_a+2):
    print("El juego aún no termina")

