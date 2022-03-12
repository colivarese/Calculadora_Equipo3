def multiplicacion(a,b):
  """
  Función para multiplicar dos números

  Params:
    a: Primer número a multiplicar
    b: Segundo número a multiplicar


  Returns:
    El producto de a y b.

  >>>multiplicacion(5,"6/25")
    1.2
  """

  mult_a = convertir_fracciones(a)
  mult_b = convertir_fracciones(b)
  return mult_a * mult_b
