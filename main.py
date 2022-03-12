






















def division(a,b):
  numerador = convertir_fracciones(a)
  denominador = convertir_fracciones(b)
  if(denominador == 0):
    raise Exception("Error: el denominador no puede ser 0")
  else:
    return numerador / denominador