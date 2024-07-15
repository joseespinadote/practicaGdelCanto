tupla = ("manzana", "banana", "cereza", "manzana", "cereza") #crear tupla
print(tupla)
print(len(tupla)) #longitud de la tupla

type # con el type podemos ver que tipo de clase estamos usando en una variable

tupla1 = ("manzana",) # tupla de solo 1 indice, crear con una coma al final asi python reconoce que es una tupla
print(type(tupla1))

tupla2 = ("manzana", "banana", "cereza") # las tuplas contienen cualquier tipo de datos
tupla3 = (1, 5, 7, 9, 3)
tupla4 = (True, False, False)

tuple5 = ("abc", 34, True, 40, "male") # de igual manera puede contener distintas variables como las listas

tupla = tuple(("manzana", "banana", "cereza")) # podemos crear una tupla definiendola
print(tupla)

tupla = ("manzana", "banana", "cereza") 
print(tupla[1]) # para  ver el indice 1
print(tupla[-1]) # para ver el ultimo indice

tupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(tupla[2:5]) #ver desde el indice 2 hasta el 4 (no se excluye el 5)

tupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(tupla[:4]) # muesta del indice 0 hasta el 3 

tupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(tupla[2:]) #muesta desde el 2 hasta el final

tupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(tupla[-4:-1]) # muestra desde el ultimo (excluyendolo) hasta el 4 

tupla = ("manzana", "banana", "cereza") 
if "manzana" in tupla:
  print("manzana esta prensente")

x = ("manzana", "banana", "cereza") # como no podemos actualizar una tupla ya que son inmutables podemos pasar de tupla a lista cambiar el valor y volver a transformala en tupla
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

tupla = ("manzana", "banana", "cereza") # como las tuplas son inmutables pasamos a lista y despues de agregar un nuevo indice lo pasamos tupla otra vez
y = list(tupla)
y.append("naranja")
tupla = tuple(y)

tupla = ("manzana", "banana", "cereza") # podemos unir tuplas
y = ("naranja",)
tupla += y

print(tupla)

tupla = ("manzana", "banana", "cereza") # pasar de tupla a lista y remover un indice y volver a tupla
y = list(tupla)
y.remove("manzana")
tupla = tuple(y)

del tupla #elimina la tupla

frutas = ("manzana", "banana", "cereza")

(verde, amarillo, rojo) = frutas # desempaquetar una tupla

print(verde)
print(amarillo)
print(rojo)

(verde, amarillo, *rojo) = frutas # si la desempaquetadura tiene menos indices que la tupla con el * con el ultimo indice se le pondra automaticamente todos los indices de la tupla restantes

(verde, *amarillo, rojo) = frutas # en caso de poner el * en medio o al incio la desempaquetadura pondra los datos hasta que los indice coincidan

for m in frutas: #forma de recorrer una tupla con for
  print(m)

for m in range(len(frutas)): #forma de recorrer una tupla con for midiendo el rango y la longitud
  print(m)

i = 0
while i < len(frutas): #forma de recorrer una tupla con while
  print(frutas[i])
  i = i + 1

tupla5 = frutas + tupla #concatenar tuplas (unir)
print(tupla5)

tupla6 = frutas*2 #multiplicar por 2 el contenido de la tupla
print(tupla6)


