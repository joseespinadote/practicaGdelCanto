import modulo #importar otros archivos .py
import random

"""
comentario totalmente grande
"""
print('hola mundo') #este es un comentario

#TEXTOS
libro = "El Programador prágmatico" #variable String

a = b = c = "Naranja"
print(a)
print(b)
print(c)

g = "hola "
h = "como "
i = "estas"

print(g + h + i) # concatenacion de variables tipo STR

txt = "HOLA BUENAS TARDES" #comprueba si esta la palabra TARDES en el texto
print("TARDES" in txt)
if "TARDES" in txt:
    print("si esta presente")

txt = "las mejores cosas de la vida" # verificacion si existe la platabla jueves en el texto txt
print("hola" not in txt)

txt = "mañana es viernes"

if "jueves" not in txt: # verificacion si existe la platabla jueves en el texto txt con condicion
  print("No, 'jueves' no esta presente")


a = "Hola Mundo" #muestra la logitud del texto
print(len(a))

t = "hola mundo" #muestra solo los caracteres dentro de 2 a 5 no incluidos
print(t[2:5])

b = "hola mundo"
print(b[:5]) # muestra los primeros caracteres hasta 5 no incluido
print(b[5:]) # muestra los caracteres hasta 5 incluido
print(b[-5:-2]) #el 5 muestra solo un caracter en especifico y el 2 solo 1 y 2 caracter desde le final

a = "hola mundo" # todo mayusculas
print(a.upper())
a = "HOLA MUNDO"
print(a.lower()) # todo minuscula
a = " hola mundo "
print(a.strip()) # elimina los saltos incesetarios del texto
a = "Hola mundo"
print(a.replace("H", "J")) #cambia la H por La J
a = "hola mundo"
print(a.split(",")) # entrega el hola mundo en 2 textos separados

age = 21 
txt = f"mi nombre es gabrel, y tengo {age} años de edad" # muestra de por medio una variable int 
print(txt)
precio = 59
txt = f"el precio es {precio:.2f} en clp" # el precio:.2f muestra el resultado con 2 decimales
print(txt)
txt = f"el precio es {20 * 59} en clp" #muestra el resultado de una operacion
print(txt)
txt = "We are the so-called \"Vikings\" from the north" # muetra una varibale de por medio sin error de syntaxis
#NUMERICO
entero = 200 #Variable numerica
decimal = 29.423 #variable Decimal

x = str(3)    # x = 3 pero en texto
y = int(3)    # y = 3 pero en numerico
z = float(3)  # z = 3 pero en decimal
#Entero
x = int(1)   # x =  1
y = int(2.8) # y =  2 # lo toma como 2 ya que el primer numero
z = int("3") # z =  3 # lo toma como entero apesar estar escrito como string
#Float
x = float(1)     # x = 1.0
y = float(2.8)   # y = 2.8
z = float("3")   # z = 3.0
w = float("4.2") # w = 4.2
#String
x = str("s1") # x = 's1'
y = str(2)    # y = '2'
z = str(3.0)  # z = '3.0'

#BOLEANOS
autoriazado = True # variable verdadera
denegado = False # variable false

#MAPAS
jugadores = { #NUMERICO A TEXTO
    10: 'Messi',
    7: 'Cristiano Ronaldo'
}
print(jugadores[7])

países = {  #TEXTO A TEXTO
    'EC': 'Ecuador',
    'MX': 'México',
    'AR': 'Argentina'
}

emails = { #TEXTO A LISTAS
    'Juan': ['juan@gmail.com'],
    'Ricardo': ['ricardo@gmail.com', 'ricardo@hotmail.com']
}
print(emails['Juan'])
#CONSTANTES
PI = 3.14159265359

#OPERADORES
print(1 + 1) #sumar
print(1 - 1) #restar
print(10 * 2) #multiplicar
print(10 / 2) #dividir
print(10 ** 2) #exponente
print(10 % 2) #Resto
print(10 // 2) #division a piso
#OPERADORES COMPARATIVOS
print(4 == 4) #iguales
print(4 == '4') #igual de numerico a texto
print(4 != 5) #es diferente a
print(4 < 5) #menor que
print(4 >= 5) # mayor o igual

animales = ['perro', 'gato', 'raton'] #array String

numeros = [23, 45, 16, 37, 3, 99, 22] #array numerica

entero = 100 #memoria
print(entero is entero) #una variable es exactamente igual en la memoria

#Si es Verdadero o False con and
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

#Si es Verdadero o False con or
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

#CONDICIONALES
if autoriazado: #if and else 
    print('puede ingresar')
else:
    print('no puede ingresar')

if entero == 99: #if and elif 
    print('es 99') #comparar el mismo dato con otro valor
elif entero == 100:
    print('es 100')
else:
    print('no es 99 ni 100')

color = 'amarillo'
match color: #compara los distintos casos de una variable
    case 'verde':
        print('exito')
    case 'amarillo':
        print('advertencia')
    case _:
        print('error')

# las variables globales las pueden usar cualquier funcion
x = "increible"

def myfunc():
  print("Python es " + x)

myfunc()
#en este caso se crea la variable x dentro de la funcion osea que de forma local y no global
def myfunc():
  x = "fantastico"
  print("Python es " + x)

myfunc()

print("Python es " + x)

x = 5
print(type(x))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convertir de int a float:
a = float(x)

#convertir de float a int:
b = int(y)

#convertir de int a complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print(random.randrange(1, 10)) #muestra un numero aleatorio

def sumar(primero,segundo): #realizando suma con retorno mediente una funcion
    return primero + segundo

resultado = sumar(3,4)
print(resultado)

def multiplicar(primero, segundo):  #multiplicacion sin retorno meidente una funcion
    print(primero * segundo)

multiplicar(entero, 2)
    
def imprimirPrimerElemento(lista): #imprimiendo una lista con funcion
    print(lista[0])

imprimirPrimerElemento(animales)

def quicksort(lista1): 
    if len(lista1) <= 1:
        return lista1
    pivote = lista1[0]
    izquierda = []
    derecha = []

    for i in range(1, len(lista1)):
        izquierda.append(lista1[i]) if lista1[i] < pivote else derecha.append(lista1[i])

    return quicksort(izquierda) + [pivote] + quicksort(derecha)

listaOrdenada = quicksort(numeros) #la funcion quicksort ordena automaticamente
print(listaOrdenada)

for animal in animales: #el bucle for muestra todas las variables de un array 
    print(animal)

for numero in numeros:
    multiplicar(numeros, 2) #en este caso multiplica toda la array por 2

emergencia = 201

while entero < emergencia:  #bucle hasta llegar al numero indicado
        print(entero)
        entero += 1

javascript = {
    'nombre': 'JavaScript',
    'año': '1995'
}

def descrpción():
    print('%s fue creado en %s' % (javascript['nombre'], javascript['año'])) #mostrar los datos de un mapa o diccionario en el orden que se ponen

class Lenguaje:
    def __init__(self,nombre, año):
        self.nombre = nombre
        self.año = año
    def descrpción1(self): #metodo
        print('%s fue creado en %s' % (self.nombre, self.año))

javascript1 = Lenguaje('JavaScript', 1995)
javascript1.descrpción1()
html = Lenguaje ('HTML', 1993)
html.descrpción1()
css = Lenguaje ('CSS', 1996)
css.descrpción1()

modulo.restar(10, 2) # mostrar datos de la importacion