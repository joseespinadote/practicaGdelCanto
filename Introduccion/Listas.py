numeros = [23, 45, 16, 37, 3, 99, 22] #array numerica
print(numeros[0]) #seleccionar y mostrar la array

animales = ['perro', 'gato', 'raton'] #array String

datosmixtos = ['texto', 23, True, ['lista dentro de otra lista']] # array con  datos mixtos

frutas = ["manzana", "pera", "platano"] 
d, e, f = frutas
print(d)
print(e)
print(f)

lista12 = ["manzana", "planano", "higo"]
lista12.append("naranja")   #agregenga un indice con valor designado
print(lista12)

lista12.insert(1, "naranja") #agrega un indice con valor designado en el indice 1
print(lista12)

tuple = ("kiwi", "naranja") #puede agregar tipo de objetos
lista12.extend(tuple)
print(lista12) 

lista12 = ["manzana", "planano", "higo"] #elimina el indice con el nombre desginado en la varibale remove en caso de haber 2 variable iguales elimina solo la primera aparicion
lista12.remove("banana")
print(lista12)

lista12 = ["manzana", "planano", "higo"] #elimina el indice 1, si no se especifica el pop elimina el ultimo indice
lista12.pop(1)
print(lista12)

lista12 = ["manzana", "planano", "higo"] # con la palabra clave del tambien elimina el indice 0 en el caso de poner del sin especificar el indice la elimina por completo
del lista12[0]
print(lista12)

lista12 = ["manzana", "planano", "higo"] # limpia los indices de la array dejandola completamente vacia pero no la elimina
lista12.clear()
print(lista12)

lista12 = ["manzana", "planano", "higo"] # #muestra todos los indices con el bucle for
for i in range(len(lista12)):
  print(lista12[i])

lista12 = ["manzana", "planano", "higo"] # muestra todos los indices por el bucle while 
i = 0
while i < len(lista12):
  print(lista12[i])
  i = i + 1

lista12 = ["manzana", "planano", "higo"] # muestra todos los indices 2 forma con for
for x in lista12:
  print(x)

frutas = ["manzana", "platano", "cherry", "kiwi", "mango"] #crea y copia los datos de una lista ya existente solo que en este caso solo con la letra A
nuevalista = []

for x in frutas:
  if "a" in x:
    nuevalista.append(x)

print(nuevalista)

nuevalista = []
frutas = ["manzana", "platano", "cherry", "kiwi", "mango"] #crea y copia los datos de una lista ya existente con letra A en su nombre pero en solo 1 linea de codigo
nuevalista = [] = [x for x in frutas if "a" in x]
print(nuevalista = [])

nuevalista = []
nuevalista = [x for x in frutas if x != "manzana"] # le podemos poner condiciones en este caso solo para que acepte los que no son manzana

nuevosnumeros = [x for x in range(10)] #crea una iterable hasta un limite 10 (0 al 9)
print(nuevosnumeros)

nuevosnumeros1 = [x for x in range(10) if x < 5] # #crea una iterable hasta un limite 10 (0 al 9) con la condicion de solo sacar numeros menores a 5
print(nuevosnumeros)

nuevalista = [x.upper() for x in frutas] # duplica una lista pero en MAYUSCULAS
nuevalista = ['hola' for x in frutas] # reemplaza todos los datos de la lista como hola

nuevalista = ["manzana", "platano", "cherry", "kiwi", "mango"]
nuevalista = [x if x != "platano" else "naranja" for x in frutas]

nuevalista.sort() # ordena la lista de forma ASCENDENTE
print(nuevalista)
nuevalista.sort(reverse = True) # ordena la lista de forma DESCENDENTE
print(nuevalista)

def mifuncion(n):
  return abs(n - 50)
nuevosnumeros1 = [100, 50, 65, 82, 23] #podemos agregarle una condicion con key y los ordena del mas cercano al 50
nuevosnumeros1.sort(key = mifuncion)
print(nuevosnumeros1)

lista12 = ["platano", "Naranja", "Kiwi", "cherry"] # no distingue entre mayusculas y minusculas palabra clave key
lista12.sort(key = str.lower)
print(lista12)

lista12 = ["platano", "Naranja", "Kiwi", "cherry"] #invierte el orden de los indices
lista12.reverse()
print(lista12)

lista12 = ["platano", "Naranja", "Kiwi", "cherry"] # copia la lista a otra
nuevalista2 = lista12.copy()
print(nuevalista2)

nuevalista2 = list(lista12) #otra forma de copia de una lista a otra
print(nuevalista2)

lista1 = ["a", "b", "c"]    #se puede unir mediante el operador +
lista2 = [1, 2, 3]

lista3 = lista1 + lista2
print(lista3)

for x in lista2: # se puede unir 1 por 1
  lista1.append(x)

print(lista1)

lista1.extend(lista2) # user extend puede unir 2 listas
print(lista1)