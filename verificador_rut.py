def verificar_rut(rut):
    
    if not isinstance(rut, str):
        return False

    try:
        numero_rut_str, dv_str = rut.split("-")
    except ValueError:
        return False

    try:
        numero_rut = int(numero_rut_str)
    except ValueError:
        return False

    dv_str = dv_str.lower()

    suma = 0
    multiplicador = 2
    temp_rut = numero_rut

    while temp_rut > 0:
        digito = temp_rut % 10
        suma += digito * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
        temp_rut //= 10

    dv_calculado_num = 11 - (suma % 11)

    if dv_calculado_num == 11:
        dv_calculado = '0'
    elif dv_calculado_num == 10:
        dv_calculado = 'k'
    else:
        dv_calculado = str(dv_calculado_num)

    return dv_str == dv_calculado