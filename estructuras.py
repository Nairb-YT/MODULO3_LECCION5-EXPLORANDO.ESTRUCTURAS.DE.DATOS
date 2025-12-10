"""
1.- CREAR ESTRUCTURAS
"""
#Lista con 3 elementos. Las listas Si pueden modificarse.
lista_fruta = ["manzanas", "pera", "platano"]
#Tupla con 3 elementos. Las tuplas NO se pueden modificar.
tupla_numeros = (5, 10, 15)
#Conjuntos con 3 elementos. No tiene orden y no permite elementos repetidos.
conjunto_colores = {"rojo", "verde", "azul"}
#Diccionario con 3 pares clave:valor.
diccionario_persona = {"nombre": "carlos", "edad": 25, "ciudad": "santiago"}

#Mostrar cada estructura por pantalla
print ("lista:", lista_fruta)
print ("tupla:", tupla_numeros)
print ("conjunto:", conjunto_colores)
print ("diccionario:", diccionario_persona)
#Explicacion simple de su diferencia principal
print("\nDiferencia principal: La lista se puede modificar, la tupla no."
      "El conjunto no tiene orden y el diccionario usa claves para identificar valores.")


"""
2.- ACCEDER A ELEMENTOS
"""
#Mostrar cantidad de elementos en cada estructura con len()
print("\nSegundo elemento de la lista:", lista_fruta[1])
#Imprimir una clave y sus valores desde el diccionario
print("Nombre dentro del diccionario:", diccionario_persona["nombre"])
#Explicacion sobre los set
#No se puede acceder por indice a un set porque NO tiene orden fijo.
#Si intentas conjunto_colores[0], dara error.


"""
3.- CONTAR E ITERAR
"""
#Mostrar cantidad de elementos en cada estructura con len()
print("\nCantidad en la lista:", len(lista_fruta))
print("Cantidad en la tupla:", len(tupla_numeros))
print("Cantidad en el conjunto:", len(conjunto_colores))
print("Cantidad en el diccionario:", len(diccionario_persona))
#iterar lista
print("\nElementos en la lista:")
for fruta in lista_fruta:
    print(fruta)

#Iterar tupla
print("\nElementos en la tupla:")
for numero in tupla_numeros:
    print(numero)

#Iterar Conjunto
print("\nElemntos en el conjunto(El orden puede cambiar):")
for color in conjunto_colores:
    print(color)

#Iterar Diccionario
print("\nElementos en el Diccionario:")
for clave in diccionario_persona:
    print(clave, "->", diccionario_persona[clave])


"""
MODIFICAR ESTRUCTURAS
"""
#Agrega nuevo elemento a la lista
lista_fruta.append("kiwi")
print("\nLista despues de agregar elemento:", lista_fruta)
#Agregar nuevo elemento al conjunto
conjunto_colores.add("amarillo")
print("Conjunto despues de agregar un elemento:", conjunto_colores)
#Borrar un elemento de la lista
lista_fruta.remove("pera")
print("Lista despues de borrar 'pera':", lista_fruta)
#Agregar una nueva clave al diccionario
diccionario_persona["profesion"] = "ingeniero"
print("Diccionario despues de agregar una nueva clave:", diccionario_persona)
#Intentar modificar la tupla
print("\nIntentando modificar la tupla...")

try:
    tupla_numeros[0] = 99
except TypeError:
    print("No se puede modificar una tupla. Las tuplas son inmutables y no cambian.")
    