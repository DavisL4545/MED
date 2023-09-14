#solicitar la palabra al usuario

palabra_base = input("ingrese la palabra base:")

#solicitud de la longitud de la lista al usuario


longitud_lista = int(input("ingrese la longitud de la lista:"))

#crearemos una lista vacioa para almacenar las palabras

list_palabras = []

#llenaremos la lista vacia con palabras ingresadas por el usuario

for i in range(longitud_lista):
    palabra = input(f"ingresee la palabra{i+1}:")

    list_palabras.append(palabra)

 #Evaluar si las palabras son acronimas de la palabra acrinimos

acronimos = []
for palabra in list_palabras:
    #verificaremos si la longitud de las palabras es igual a la de la palabra base

    if len(palabra) ==len(palabra_base):
        #verificaremos si las letras de la palabra forman un acronimo de la palabra base

        es_acronimo = all(l1== l2 for l1, l2 in zip (palabra, palabra_base))

#mostraremos las palabras que son acronimas a la palabra base

if acronimos:
    print("las siguientes palabras son acronimas de la palabra base:")
    for acronimos in acronimos:
        print(acronimos)
    else:
        print("no se encontraron acronimos en las listas:")
