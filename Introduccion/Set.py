set = {"manzana", "banana", "cereza"} #crear set
print(set) #imprimir set
set = {"manzana", "banana", "cereza", "manzana"} #los set no permiten duplicados
print(set)
set = {"manzana", "banana", "cereza", True, 1} #true y 1 se concideran lo mismo
print(set)
set = {"manzana", "banana", "cereza", False, 0} #False y 0 se concideran lo mismo
print(len(set))

set1 = {"manzana", "banana", "cereza"} #set texto
set2 = {1, 5, 7, 9, 3} # set enteros
set3 = {True, False, False} # set booleanos

set3 = {"abc", 34, True, 40, "hombre"} #puede contener distintas variables
print(type(set3)) # ver tipo de clase

set4 = set(("manzana", "banana", "cereza")) # podemos crear un set con el constructor set()
print(set4)

for x in set4: # son los set no podemos ver un indice en especifica como las listas pero podemos recorrer el set bucles
  print(x)

print("banana" in set4) #ver si esta en el set
print("banana" not in set4) #ver si no esta en el set

set4.add("naranja") # agregar un nuevo dato al set
print(set4)

tropical = {"piña", "mango", "papaya"} # podemos juntar 2 set's
set4.update(tropical)
print(set4)

lista = ["kiwi", "naranja"] #podemos juntar listas a set de igual manera con diccionarios y tuplas
set4.update(lista)
print(set4)
set4.remove("banana") #podemos remover un elementos del set
print(set4)
set4.discard("manzana") # tambien podemos eliminar con discard
print(set4)

x = set4.pop() # con esto podemos eliminar un dato random dentro del set
print(x)
print(set4)
set4.clear() # limpia el set
print(set4)
del set4 #elimina el set
print(set4)

set3 = set1.union(set2) # podemos unir sets
print(set3)
set3 = set1 | set2 # #podemos unir sets con el operador | en ves de union()
print(set3)

set5 = set1.union(set2, set3, set4) # asi podemos unir muchos sets
print(set5)
set5 = set1 | set2 | set3 |set4 # unir con el operador
print(set5)

x = {"a", "b", "c"} # con union no solo podemos unir sets entre si tambien set a tupla y listas
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"manzan", "banana", "cereza"}
set2 = {"google", "microsoft", "manzana"}

set3 = set1.intersection(set2) # intersection solo contendra los elementos identicos en ambas tablas
print(set3)

set3 = set1 & set2 # podemos user el operador & para usar intersection
print(set3)
set1.intersection_update(set2) # solo actualiza el set1 y mostrara los duplicados 
print(set1)

set1 = {"manzana", 1,  "banana", 0, "cereza"}
set2 = {False, "google", 1, "manzana", 2, True}

set3 = set1.intersection(set2) # como true y 1 son iguales y false y 0 son iguales solo muestra los duplicados
print(set3)

set1 = {"manzana", "banana", "cereza"}
set2 = {"google", "microsoft", "manzana"}

set3 = set1.difference(set2) # mostrara solo los datos que no esten presente en el otro set
print(set3)
set3 = set1 - set2 # con operador - podemos realizar lo mismo
print(set3)

set1.difference_update(set2) # se crea un nuevo set con los datos no presente de ambos set
print(set1)

set3 = set1.symmetric_difference(set2) # se crea un nuevo set con los datos que no esten presentes en ambos set
print(set3)

set3 = set1 ^ set2 # realizamos los mismo de arriba unir los dos set con los datos no presente
print(set3)

set1.symmetric_difference_update(set2) # actualiza un set pero mantiene los no duplicados de ambas tablas
print(set1)