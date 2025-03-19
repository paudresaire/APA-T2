"""
PAU DRESAIRE

>>> esPrimo(5)
True

>>> esPrimo(2)
True

>>> esPrimo(74211)
False

>>> print(primos(10))
(2, 3, 5, 7)

>>> print(descompon(28))
(2, 2, 7)

>>> print(mcd(28, 35))
7

>>> print(mcm(28, 35))
140


Tests unitarios:

1. esPrimo(numero): Al ejecutar [ numero for numero in range(2, 50) if esPrimo(numero) ], la salida debe ser [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].
   
2. primos(numero): Al ejecutar primos(50), la salida debe ser (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47).

3. descompon(numero): Al ejecutar descompon(36 * 175 * 143), la salida debe ser (2, 2, 3, 3, 5, 5, 7, 11, 13).

4. mcm(num1, num2): Al ejecutar mcm(90, 14), la salida debe ser 630.

5. mcd(num1, num2): Al ejecutar mcd(924, 780), la salida debe ser 12.

6. mcmN(numeros): Al ejecutar mcmN(42, 60, 70, 63), la salida debe ser 1260.

7. mcdN(numeros): Al ejecutar mcdN(840, 630, 1050, 1470), la salida debe ser 210.
"""


def esPrimo(numero):
    """
    La función devuelve True si el número es primo, False si no lo es

    >>> for numero in range(2,50):
    ...     if esPrimo(numero):
    ...         print(numero)
    2
    3
    5
    7
    11
    13
    17
    19
    23
    29
    31
    37
    41
    43
    47
    """
    for prueba in range(2, numero):
        if numero % prueba == 0:
            return False
    return True


def primos(numero):
    """
    La función devuelve una tupla con todos los numeros primos menores que su argumento
    
    >>> print(primos(50))
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    primos= []
    for prueba in range (2, numero):
        if esPrimo(prueba):
            primos.append(prueba)
    return tuple(primos)


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    
    >>> print(descompon(36 * 175 * 143))
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> print(mcd(924, 780))
    12
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    comunes = []
    for factor in factores1:
        if factor in factores2:
            comunes.append(factor)
            factores2 = list(factores2)  # Convertir en lista para modificar
            factores2.remove(factor)
    producto = 1
    for factor in comunes:
        producto *= factor
    return producto


def mcm(numero1, numero2):
    """
    Devuelve el mínimo comun multiplo de sus argumentos

    >>> print(mcm(90, 14))
    630
    
    """
    factores1 = list(descompon(numero1))
    factores2 = list(descompon(numero2))
    resultado = factores1[:]
    for factor in factores2:
        if factor in factores1:
            factores1.remove(factor)
        else:
            resultado.append(factor)
    producto = 1
    for factor in resultado:
        producto *= factor
    return producto


def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de varios números usando su descomposición en factores primos.
    
    >>> print(mcmN(42, 60, 70, 63))
    1260
    """
    # Diccionario para almacenar la máxima cantidad de veces que aparece cada factor primo
    mcm_resultado = {}
    
    # Descomponemos todos los números y agregamos los factores primos
    for numero in numeros:
        factores = descompon(numero)
        for factor in factores:
            if factor in mcm_resultado:
                # Guardamos el máximo recuento del factor
                mcm_resultado[factor] = max(mcm_resultado[factor], factores.count(factor))
            else:
                # Si el factor no ha sido agregado, lo añadimos
                mcm_resultado[factor] = factores.count(factor)
    
    # Multiplicamos todos los factores con sus máximos recuentos
    resultado = 1
    for factor, count in mcm_resultado.items():
        resultado *= factor ** count
    
    return resultado


def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de varios números usando su descomposición en factores primos.
    
    >>> print(mcdN(840, 630, 1050, 1470))
    840
    """
    resultado = 1
    # Descomponemos todos los números y buscamos los factores comunes
    for factor in descompon(numeros[0]):
        if all(factor in descompon(num) for num in numeros):
            min_count = min([descompon(num).count(factor) for num in numeros])
            resultado *= factor ** min_count
    return resultado




if __name__  == '__main__':
    import doctest
    doctest.testmod()



