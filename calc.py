def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multip(a, b):
    return a * b


def divis(a, b):
    division = int(a / b)
    # Devuelve el resto de una división
    resto = a % b
    return division, resto


def calc():
    print('Calculadora Pro 9000')
    # Ingreso de operador
    print('Ingrese la alternativa correspondiente '
          'a la operación a realizar:')
    print('1.-Suma\n2.-Resta\n3.-Multiplicación\n4.-División')
    func = int(input('Ingrese la operación:\n'))

    # Obtención de números
    numero1 = input('Ingrese Primer Número:\n')
    numero1 = int(numero1)
    numero2 = input('Ingrese Segundo Número:\n')
    numero2 = int(numero2)

    # Operadores
    resto = None
    print('El resultado es:')
    if func == 1:  # Suma
        result = suma(numero1, numero2)
    elif func == 2:  # Resta
        result = resta(numero1, numero2)
    elif func == 3:  # Multiplicación
        result = multip(numero1, numero2)
    elif func == 4:  # División
        result, resto = divis(numero1, numero2)
    print(result)
    if resto:
        print('El resto es: {}'.format(resto))


if __name__ == '__main__':
    calc()
