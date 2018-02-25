"""Python Game Text."""
from sys import exit

# --------------------------- VARS ---------------------------

beast_alive = True
dragon_alive = True
sword = False

# ------------------------- ROUTINES -------------------------

# ROOM 1


def room_1():
    print("Estas en un cuarto grande con las paredes cuviertas de sangre.")
    print("Esta demasiado oscuro y lo unico que puedes ver son tres puertas")
    print("Conducen al este, norte y oeste. ¿A donde te diriges?")

    choice = input("> ")

    if "oeste" in choice:
        room_2()
    elif "norte" in choice:
        room_4()
    elif "este" in choice:
        game_over("""Cuidadosamente caminas hacia el pasaje que te dirige al este. Despues de caminar durante tres minutos, ves que
termina con una pared sólida. Te das la vuelta para volver
pero te encuentras frente a otra pared. Algo ha pasado,
estás atrapado. Sin comida ni agua mueres en unos cuantos dias.""")
    else:
        room_1()

# ROOM 2


def room_2():
    print("Esta habitacion tiene un techo muy bajo y debes agacharte para caminar.")
    print("Ves un pasaje que conduce al oeste y un pasaje que conduce al norte.")
    print("Al fondo de la primera, puedes ver una luz brillante.")
    print("De la segunda, un olor horrible emana.")
    print("El pasaje hacia el este conduce a la primera sala.")
    print("¿A dónde te diriges?")

    choice = input("> ")

    if "oeste" in choice:
        game_over("""Sigues el camino brillante. Mientras caminas, la luz
se vuelve mas y mas brillante, hasta que no puede ver nada.
De repente ya no puedes sentir el suelo debajo de tu
pies y, al caer en un pozo de llamas, entiendes
de dónde vino la luz Mueres gritando de dolor.""")
    elif "norte" in choice:
        room_3()
    elif "este" in choice:
        room_1()
    else:
        room_2()

# ROOM 3


def room_3():

    global beast_alive
    global sword

    if beast_alive:
        print("Cuando entras a la habitacion, entiendes de donde viene el olor.")
        print("El piso esta cubierto de cadáveres podridos.")
        print("De repente escuchas un gruñido y una enorme bestia aparece frente a ti.")
        print("Ves un pasaje hacia el este, una antorcha encendida en el suelo,")
        print("un esqueleto sosteniendo una espada y un agujero en el otro extremo de la habitacion.")
        print("El pasaje hacia el sur conduce a la segunda habitacion.")
        print("¿Qué decides hacer?")

        choice = input("> ")

        if "este" in choice:
            game_over("""Mientras corres hacia el este, la bestia salta
frente a ti. No tienes tiempo para hacer nada,
porque la bestia abre sus mandíbulas y rasga tu cabeza.""")
        elif "antorcha" in choice:
            print("""Tomas la antorcha encendida y la agitas frente a la
bestia. Salta hacia atras con miedo, tropieza y cae en el
agujero, desapareciendo de la habitacion.""")
            beast_alive = False
            room_3()
        elif "espada" in choice:
            print("""Tomas la espada. De repente, comienza a emanar una luz y te sientes invencible. Sin saber como, tu
saltas adelante y matas a la bestia.""")
            beast_alive = False
            sword = True
            room_3()
        elif "agujero" in choice:
            game_over("""Saltas en la oscuridad. No fue
una buena idea, sin embargo empiezas a caer en el vacío. Mueres días despues, todavia
que cayendo.""")
        elif "sur" in choice:
            room_2()
        else:
            room_3()

    else:
        print("El piso esta cubierto de cadaveres podridos.")
        print("Ves un pasaje hacia el este, una antorcha encendida en el suelo,")
        print("un esqueleto sosteniendo una espada y un agujero en el otro extremo de la habitacion.")
        print("El pasaje hacia el sur conduce a la segunda habitación.")
        print("¿Que decides hacer?")

        choice = input("> ")

        if "este" in choice:
            room_4()
        elif "antorcha" in choice:
            print("""Tomas la antorcha encendida y la agitas en el aire.
Te sientes estupido y lo dejas.""")
            room_3()
        elif "espada" in choice:
            print("""Tomas la espada.""")
            sword = True
            room_3()
        elif "agujero" in choice:
            game_over("""Saltas en la oscuridad. No fue
una buena idea, sin embargo empiezas a caer en el vacio. Mueres días despues, todavia
que cayendo.""")
        elif "sur" in choice:
            room_2()
        else:
            room_3()

# ROOM 4


def room_4():

    global dragon_alive

    if dragon_alive:

        print("La habitacion es enorme, y por buenas razones. Es el hogar de un dragon.")

        if sword:
            print("""De repente, tu espada comienza a brillar. Una fuerza desconocida te impulsa a saltar hacia adelante e introducir la espada en el corazon del dragones.
Muere con horribles gritos.""")
            dragon_alive = False
            room_4()
        else:
            print("Hay un pasaje hacia el norte, uno hacia el este, uno hacia el")
            print("sur y uno al oeste. ¿Que haces?")

        choice = input("> ")

        game_over("El dragon salta delante de ti y te asa vivo.")

    else:

        print("Hay un pasaje hacia el norte, uno hacia el este, uno hacia el")
        print("sur y uno al oeste. ¿Que haces?")

        choice = input("> ")

        if "este" in choice:
            game_over("""Sigues hacia el este hasta que terminas en una
habitación con escritorio y un PC. Un pequeño tipo está escribiendo
en la PC y de repente nota tu presencia. '¡No deberías haberme encontrado! él dice. 'Ahora
tienes que morir ". Él escribe algo en la PC, y tú mueres.""")
        elif "sur" in choice:
            room_1()
        elif "oeste" in choice:
            room_3()
        elif "norte" in choice:
            game_over("""El pasaje conduce a la superficie. ¡Estas libre! ¡Has ganado el juego!""")
        else:
            room_4()

# START


def start():
    room_1()

# GAME OVER


def game_over(s):

    global beast_alive
    global dragon_alive
    global sword

    beast_alive = True
    dragon_alive = True
    sword = False

    print(s)
    print("¿Deseas jugar de nuevo? (s / n)")

    choice = ""
    while choice != "s" and choice != "n":
        choice = input("> ")
        if choice == "s":

            start()
        elif choice == "n":
            exit(0)


# --------------------------- MAIN ---------------------------

start()
