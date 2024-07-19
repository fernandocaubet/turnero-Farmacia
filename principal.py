import numeros
from os import system

def preguntar():
    system('cls')
    print('*' * 10 + ' bienvenidos '+ '*' * 10)
    while True:
        print("\nRUBROS!!!\n [P] Perfumeria  \n [C] Cosmetica \n [F] Farmacia")
        try:
            mi_rubro = input('Elija un rubro:').upper()
            ['P','C','F'].index(mi_rubro)
        except ValueError:
            print('no es una opcion valida')
        else:
            break
    numeros.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('quieres sacar otro turno? [S] [N]: ').upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('esa no es una opcion valida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break

inicio()
