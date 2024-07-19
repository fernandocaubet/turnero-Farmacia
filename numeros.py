def turno_perfumeria():
    num = 0
    while num < 100:
        num += 1
        yield f'>>>   {num} P'


def turno_farmacia():
    num = 0
    while num < 100:
        num += 1
        yield f'>>>   {num} F'


def turno_cosmetica():
    num = 0
    while num < 100:
        num += 1
        yield f'>>>   {num} C'


p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmetica()


def decorador(rubro):
    print('\n*******FARMACIA PUBLICA*******')
    print('>>>   Su Turno es el Nro   <<<')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else:
        print(next(c))
    print('Gracias por su Visita!!!')



