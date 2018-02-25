loop = 'y'

while loop == 'y':
    numero1 = float(input('Ingresa el primer numero\n'))
    numero2 = float(input('Ingresa el segundo numero\n'))
    opcion = int(input(""" Ingresa la opción deseada
            1.- Sumar
            2.- Restar
            3.- Multiplicar
            4.- Dividir 1ro ebtre 2do
            5.- Modulo 1ro ebtre 2do
        """))
    if opcion == 1:
        print('{} + {} = {}'.format(
            numero1, 
            numero2, 
            numero1 + numero2,)
        )
        loop = input('¿Deseas hacer otra operacion? y/n')
    elif opcion == 2:
        print('{} - {} = {}'.format(
            numero1, 
            numero2, 
            numero1 - numero2,)
        )
        loop = input('¿Deseas hacer otra operacion? y/n')
    elif opcion == 3:
        print('{} * {} = {}'.format(
            numero1, 
            numero2, 
            numero1 * numero2,)
        )
        loop = input('¿Deseas hacer otra operacion? y/n')
    elif opcion == 4:
        print('{} / {} = {}'.format(
            numero1, 
            numero2, 
            numero1 / numero2,)
        )
        repetir = raw_input('¿Deseas hacer otra operacion? y/n')
    elif opcion == 5:
        print('{} % {} = {}'.format(
            numero1, 
            numero2, 
            numero1 % numero2,)
        )
        repetir = input('¿Deseas hacer otra operacion? y/n')
    else:
        print("Opcion no valida")
        loop = input('¿Deseas hacer otra operacion? y/n')
