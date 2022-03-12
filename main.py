<<<<<<< HEAD
def resta(a,b):
    """
    Calcula la resta entre dos números

    :param a: el valor del minuendo
    :param b: el valor del sustraendo
    :return: la resta entre el parámetro a y b.

    >>> resta(2,1)
    1
    >>> resta(1,2)
    -1
    """
    minuendo = convertir_fracciones(a)
    sustraendo = convertir_fracciones(b)
    return minuendo - sustraendo
=======























def division(a,b):
  numerador = convertir_fracciones(a)
  denominador = convertir_fracciones(b)
  if(denominador == 0):
    raise Exception("Error: el denominador no puede ser 0")
  else:
    return numerador / denominador
>>>>>>> div
