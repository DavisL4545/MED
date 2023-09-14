cadena = "askakanasindsananadsjsdanana"
palabra_a_buscar = "ana"

# Inicializa una lista para almacenar los índices de coincidencia
indices_coincidencia = []

# Inicializa una variable para realizar la búsqueda en la cadena
inicio_busqueda = 0

# Busca la palabra "ana" en la cadena y almacena los índices de coincidencia
while True:
    indice_coincidencia = cadena.find(palabra_a_buscar, inicio_busqueda)
    if indice_coincidencia == -1:
        break  # Termina el bucle si no se encontraron más coincidencias
    indices_coincidencia.append(indice_coincidencia)
    inicio_busqueda = indice_coincidencia + 1

# Calcula la cantidad de veces que se repite la palabra "ana"
cantidad_repeticiones = len(indices_coincidencia)

# Muestra la cantidad de repeticiones y la lista de índices
print("Cantidad de veces que se repite la palabra 'ana':", cantidad_repeticiones)
print("Lista de índices de coincidencia:", indices_coincidencia)
