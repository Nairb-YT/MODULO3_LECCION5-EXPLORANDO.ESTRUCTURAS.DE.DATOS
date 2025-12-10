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

