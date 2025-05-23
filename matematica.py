# matematica.py

def soma(a, b):
  """Retorna a soma de dois números."""
  return a + b

def subtrai(a, b):
  """Retorna a subtração de dois números."""
  return a - b

def modulo(n):
  """Retorna o módulo (valor absoluto) de um número inteiro positivo."""
  if isinstance(n, int) and n >= 0:
    return n
  elif isinstance(n, int) and n < 0:
    return -n # Ou abs(n)
  else:
    return "Por favor, insira um número inteiro."