#Observacion -> no se devera usar metodos como sum(),min(),max().
# se podra usar for, while, insert, split,join,append -> solo los metodos que se vio en clase

# 1. la funcion recibe como parametro un array y devera devolver el numero mayor del array
def numero_mayor(arr):
  mayor = arr[0]
  for num in arr:
        if num >= mayor:
            mayor = num
  return mayor

# 2. la funcion recibe un string la funcion devera devolver el string ivertido ejem:entrada=hola, devuleve=aloh
def inverso(txt):
  invertido = ""
  for i in range(len(txt)-1, -1, -1):
        invertido += txt[i]
  return invertido

# 3. la funcion recibe un string y devuelve si la plabara es un palindromo True si no devuelve False: palindromo que se lee igual de derecha a izquierda y viceversa ejm: entrada=reconocer es palindromo se le igual de izquierda a derecha y viciversa
def palindromo(txt):
  txt = txt.lower()
  longitud = len(txt)
  for i in range(longitud // 2):
        if txt[i] != txt[longitud - i - 1]:
            return False
  return True

# 4. la funcion recibe como parametro una letra y devuelve si la letra ingresada es vocal o consonante el mensaje devera ser si es vocal = 'es vocal' si es consonante 'es consonante'
def es_vocal(letra):
  vocales = ['a', 'e', 'i', 'o', 'u']
  if letra.lower() in vocales:
        return 'es vocal'
  else:
        return 'es consonante'