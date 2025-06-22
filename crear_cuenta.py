import verificador_rut
def crear_cuenta():

    print('Ingrese los siguientes datos para su cuenta:')

    apellido_1 = input('Ingrese su apellido paterno: ')
    while not apellido_1:
        print('Es obligatorio llenar el campo')
        apellido_1 = input('Ingrese apellido paterno: ')

    apellido_2: input('Ingrese su apellido materno: ')
    while not apellido_2:
        print('Es obligatorio llenar el campo')
        apellido_2 = input('Ingrese su apellido materno: ')

