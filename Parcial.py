'''
MARIA PAULA RAMOS MARTINEZ - SEBASTIAN ALZATE SIERRA

Clases Padre (Super Clases):
    1. List: Es una clase padre que contiene métodos para manipular listas
    2. SearchAndSort: Es una clase padre que contiene métodos para realizar búsquedas y ordenamientos en listas.

Clases Hijas (Herencia):
    1. RandomList:  Contiene el método generate_list().
    2. ManualList:  Contiene el método insert_list()
    3. ListFromRange: Contiene el método create_list().
    4. Help
    5. Order
    
Clases Hijas con Varios Padres (Herencia Múltiple):
    1. RandomList: Hereda de List y SearchAndSort. Contiene el método generate_list().
    2. ManualList: Hereda de List y SearchAndSort. Contiene el método insert_list().
    3. ListFromRange: Hereda de List y SearchAndSort. Contiene el método create_list().
    
Métodos Mágicos:
    1. __init__(): Constructor de la clase List.
    2. __str__(): Método especial de la clase List para representar el objeto como una cadena de texto.

Métodos de Instancia:
    1. generate_list(): Método de RandomList para generar una lista aleatoria y extender la lista interna.
    2. insert_list(): Método de ManualList para permitir a los usuarios insertar elementos manualmente en la lista interna.
    3. create_list(): Método de ListFromRange para crear una lista a partir de un rango especificado por el usuario.
    4. get_list(): Método de List para obtener la lista almacenada en el objeto.

Métodos Estáticos:
    1. linear_search(): Método estático de SearchAndSort para realizar una búsqueda lineal en una lista.
    2. binary_search(): Método estático de SearchAndSort para realizar una búsqueda binaria en una lista ordenada.
    3. bubble_sort(): Método estático de SearchAndSort para ordenar una lista utilizando el algoritmo de burbuja.
    4. quick_sort(): Método estático de SearchAndSort para ordenar una lista utilizando el algoritmo de quicksort.
    5. show_help(): Método estático de Help para mostrar información de ayuda.
    6. linear_position()
    7. binary_position ()
    8. compare_algorithms()

Métodos de Clase: 
    1. bubble_sort(): Método de clase de Order para ordenar una lista utilizando el algoritmo de burbuja.
    2. quick_sort(): Método de clase de Order para ordenar una lista utilizando el algoritmo de quicksort.
    3. compare_algorithms(): Método de clase de AlgorithmComparison para comparar los tiempos de ejecución de diferentes algoritmos de ordenamiento.
    

'''




import time
import statistics
import random

class List:
    #Metodo constructor (__init__) de la clase List
    def __init__(self, lista=None): #Inicializa la lista interna (self.lista) con la lista propocionada.
        self.lista = lista if lista is not None else [] #o una lista vacía si no se proporciona ninguna.

    def get_list(self): # Método para obtener la lista almacenada en el objeto
        return self.lista

    def __str__(self): # Método especial para representar el objeto como una cadena de texto
        return str(self.lista) # Convierte la lista interna en una cadena y la devuelve

class SearchAndSort: # Definición de la clase SearchAndSort
    @staticmethod  # Método estático para la búsqueda lineal en una lista
    def linear_search(lista, elemento): # Recorre la lista y compara cada elemento con el elemento buscado
        for i, num in enumerate(lista):
            if num == elemento:
                return i # Devuelve el índice si se encuentra el elemento
        return -1 # Devuelve -1 si el elemento no se encuentra en la lista

    @staticmethod # Método estático para la búsqueda binaria en una lista ordenada
    def binary_search(lista, elemento):
        ordenar_lista = sorted(lista) # Ordena la lista
        izq, der = 0, len(ordenar_lista) - 1 # Se definen dos indices de la lista ordenada
        while izq <= der:
            mitad = (izq + der) // 2 # Calcula el indice de la mitad
            if ordenar_lista[mitad] == elemento: #Compara el elemento en la posición de la mitad del elemento a buscar
                return mitad # Devuelve el índice si se encuentra el elemento
            elif ordenar_lista[mitad] < elemento: # Si el elemento en mitad es menor que el elemento buscado, se ajusta el índice izq para buscar en la mitad derecha de la lista.
                izq = mitad + 1
            else: # Si el elemento en mitad es mayor, se ajusta el índice der para buscar en la mitad izquierda de la lista.
                der = mitad - 1
        return -1

    @staticmethod  # Método estático para ordenar una lista utilizando el algoritmo de bubble sort
    def bubble_sort(lista): # Compara pares de elementos adyacentes en la lista y los intercambia si están en el orden incorrecto.
        m = len(lista) # Obtener la longitud de la lista.
        for i in range(m - 1): # Inicio del primer bucle, que itera a través de todos los elementos de la lista, excepto el último.
            for j in range(m - i - 1):  # Inicio del segundo bucle, que itera a través de los elementos aún no ordenados.
                if lista[j] > lista[j + 1]: # Compara el elemento actual con el siguiente elemento en la lista.
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # Si el elemento actual es mayor que el siguiente, intercambia los elementos.
                    # Este intercambio coloca los elementos en el orden correcto, moviendo los elementos más grandes hacia la derecha.

    @classmethod # Método de clase para ordenar una lista utilizando el algoritmo de quick sort
    def quick_sort(cls, lista): 
        if len(lista) <= 1: # Verifica si la lista tiene 1 elemento o está vacía.
            return lista
        else:
            pivote = lista[0] # Toma el primer elemento como pivote
            menor = [x for x in lista[1:] if x <= pivote] # Elementos menores o iguales al pivote
            mayor = [x for x in lista[1:] if x > pivote] # Elementos mayores al pivote
            # Llama recursivamente al método quick_sort para ordenar las listas "menor" y "mayor".
        # Esto es parte de la estrategia "divide y conquista" del algoritmo quick sort.
        # Cada llamada recursiva intentará ordenar una porción más pequeña de la lista original.
        # Después, se concatenan las tres partes: "menor", el pivote y "mayor".
            return cls.quick_sort(menor) + [pivote] + cls.quick_sort(mayor)  #Se divide la lista en 3, se aplica el algoritmo de manera recursiva a las sublistas menores y mayores hasta que toda la lista esté ordenada. El pivote se coloca en su posición final en la lista ordenada.

class RandomList(List, SearchAndSort):
    def generate_list(self):
        i = int(input("Ingrese el tamaño de la lista: ")) # Solicita al usuario el tamaño de la lista.
        random_elements = [random.randint(0, 10000) for _ in range(i)] # Genera una lista de números enteros aleatorios entre 0 y 10,000.
        self.lista.extend(random_elements) # Extiende la lista interna de la clase con los elementos generados aleatoriamente.
        print("Lista generada (primeros 10 elementos):", self.lista[:10])

# Clase hija para listas manuales
class ManualList(List, SearchAndSort):
    def insert_list(self): # Método para insertar una lista manualmente
        lista = input("Ingrese los elementos separados por comas: ").strip().split(",")
        manual_elements = []
        for elemento in lista: # Itera a través de los elementos ingresados por el usuario.
            try:
                manual_elements.append(int(elemento)) # Intenta convertir cada elemento a un número entero y agregarlo a la lista manual_elements.
            except ValueError:
                print(f"Error: '{elemento}' no es un número válido. Se omitirá este elemento.")
        self.lista.extend(manual_elements) # Extiende la lista interna de la clase con los elementos ingresados manualmente.
        print("Lista generada:", self.lista[:10])

class ListFromRange(List, SearchAndSort):
    def create_list(self):  # Método para crear una lista a partir de un rango especificado por el usuario
        inicio = int(input("Ingrese el valor inicial del rango: "))
        fin = int(input("Ingrese el valor final del rango: "))
        tamano = int(input("Ingrese el tamaño de la lista: "))
        
        # Generar números aleatorios dentro del rango
        range_elements = [random.randint(inicio, fin) for _ in range(tamano)]
        
        self.lista.extend(range_elements) # Extiende la lista interna de la clase con los números generados dentro del rango.
        print("Lista generada (primeros 10 elementos):", self.lista[:10])

# Clase con método estático
class Help:
    @staticmethod
    def show_help():
        print("Ayuda:")
        print("La búsqueda lineal recorre la lista de principio a fin hasta encontrar el elemento.")
        print("La búsqueda binaria requiere que la lista esté ordenada y encuentra el elemento dividiendo la lista en mitades.")
        print("El ordenamiento por burbuja compara pares de elementos adyacentes y los intercambia si están en orden incorrecto.")
        print("El ordenamiento rápido utiliza un elemento 'pivote' para dividir la lista y ordenar de manera eficiente.")

# Clase Order para realizar operaciones de ordenamiento en listas
class Order:
    @staticmethod
    def bubble_sort(lista):
        m = len(lista)
        for i in range(m - 1): # Itera a través de los elementos de la lista (menos uno) para realizar el ordenamiento.
            for j in range(m - i - 1): # Itera a través de los elementos no ordenados.
                if lista[j] > lista[j + 1]: # Compara el elemento actual con el siguiente elemento.
                    lista[j], lista[j + 1] = lista[j + 1], lista[j] # Si el elemento actual es mayor que el siguiente, los intercambia.

    @classmethod
    def quick_sort(cls, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0] # Toma el primer elemento de la lista como pivote.
            menor = [x for x in lista[1:] if x <= pivote] # Crea una lista de elementos menores o iguales al pivote.
            mayor = [x for x in lista[1:] if x > pivote] # Crea una lista de elementos mayores al pivote.
             # Llama recursivamente al método quick_sort para ordenar las listas "menor" y "mayor".
            # Esto es parte de la estrategia "divide y conquista" del algoritmo quick sort.
            # Cada llamada recursiva intentará ordenar una porción más pequeña de la lista original.
            # Después, se concatenan las tres partes: "menor", el pivote y "mayor".
            return cls.quick_sort(menor) + [pivote] + cls.quick_sort(mayor)

# Clase Stats para métodos estáticos para cálculos estadísticos
class Stats:
    @staticmethod
    def sum(lista):
        return sum(lista)

    @staticmethod
    def mean(lista):
        return statistics.mean(lista) #promedio

    @staticmethod
    def median(lista):
        return statistics.median(lista)

    @staticmethod
    def variance(lista):
        return statistics.variance(lista)

    @staticmethod
    def length(lista):
        return len(lista)

    @staticmethod
    def maximum(lista):
        return max(lista)

    @staticmethod
    def minimum(lista):
        return min(lista)

# Clase para realizar búsqueda lineal en una lista
class LinearSearch:
    @staticmethod
    def linear_search(lista, elemento):
        for i, num in enumerate(lista): # Itera a través de la lista y sus índices.
            if num == elemento:
                return i
        return -1

    @staticmethod
    def linear_position(lista, elemento):
        posicion = LinearSearch.linear_search(lista, elemento) # Realiza una búsqueda lineal utilizando el método anterior.
        if posicion != -1:
            print(f"Elemento {elemento} encontrado en la posición {posicion}.")
        else:
            print(f"Elemento {elemento} no se ha encontrado en la lista.")

# Clase 'BinarySearch' con métodos estáticos para búsqueda binaria.
class BinarySearch:
    @staticmethod
    def binary_search(lista, elemento):
        ordenar_lista = sorted(lista)  # Ordena la lista
        izq, der = 0, len(ordenar_lista) - 1 # Establece los índices izquierdo y derecho para la búsqueda binaria.
        while izq <= der:  # Mientras el índice izquierdo sea menor o igual al derecho:
            mitad = (izq + der) // 2  # Calcula el índice del elemento en la mitad de la lista.
            if ordenar_lista[mitad] == elemento:  # Compara el elemento de la mitad con el elemento buscado.
                return mitad  # Si se encuentra el elemento, devuelve su índice.
            elif ordenar_lista[mitad] < elemento:  # Si el elemento es mayor que el de la mitad:
                izq = mitad + 1  # Ajusta el índice izquierdo para buscar en la mitad derecha.
            else:
                der = mitad - 1  # Si el elemento es menor, ajusta el índice derecho para buscar en la mitad izquierda.
        return -1  # Si no se encuentra el elemento, devuelve -1.

    @staticmethod
    def binary_position(lista, elemento):
        posicion = BinarySearch.binary_search(lista, elemento)
        if posicion != -1:
            print(f"Elemento {elemento} encontrado en la posición {posicion}.")
        else:
            print(f"Elemento {elemento} no se ha encontrado en la lista.")

# Clase para comparar algoritmos de ordenamiento
class AlgorithmComparison:
    @staticmethod
    def compare_algorithms(lista):
        lista_bubble = lista[:]  # Clona la lista original.
        lista_quick = lista[:]   # Clona la lista original.
        lista_sorted = lista[:]  # Clona la lista original.

        tiempo_inicio = time.time()  # Registra el tiempo actual.
        SearchAndSort.bubble_sort(lista_bubble)  # Aplica el algoritmo de ordenamiento de burbuja a la lista clonada.
        tiempo_bubble = time.time() - tiempo_inicio  # Calcula el tiempo transcurrido.

        tiempo_inicio = time.time()  # Reinicia el contador de tiempo.
        SearchAndSort.quick_sort(lista_quick)  # Aplica el algoritmo de ordenamiento rápido a la lista clonada.
        tiempo_quick = time.time() - tiempo_inicio  # Calcula el tiempo transcurrido.

        tiempo_inicio = time.time()  # Reinicia el contador de tiempo.
        sorted(lista_sorted)  # Aplica el método de Python 'sorted()' a la lista clonada para obtener una lista ordenada.
        tiempo_sorted = time.time() - tiempo_inicio  # Calcula el tiempo transcurrido.

        return tiempo_bubble, tiempo_quick, tiempo_sorted  # Devuelve los tiempos de ejecución de los tres algoritmos.


# Clase principal
class Menu:
    def __init__(self):
        self.lista = []

    def main_menu(self):

        try:
            while True:
                print("\nMenu:")
                print("1. Generar lista aleatoria.")
                print("2. Ingresar lista manualmente.")
                print("3. Usar lista previamente cargada.")
                print("4. Crear lista desde rango.")
                print("5. Ayuda.")
                print("6. Salir.")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    random_list = RandomList(self.lista)  # Crea una instancia de la clase RandomList y pasa la lista actual como argumento.
                    random_list.generate_list()  # Llama al método generate_list() para generar una lista aleatoria.
                    self.lista = random_list.lista  # Actualiza la lista actual con la lista generada aleatoriamente.
                elif opcion == "2":
                    manual_list = ManualList(self.lista)  # Crea una instancia de la clase ManualList y pasa la lista actual como argumento.
                    manual_list.insert_list()  # Llama al método insert_list() para permitir al usuario insertar elementos manualmente.
                    self.lista = manual_list.lista  # Actualiza la lista actual con la lista que el usuario ha ingresado manualmente.
                elif opcion == "3":
                    if self.lista:
                        print("Lista previamente generada:", self.lista[:10])
                    else:
                        print("No hay lista previamente cargada.")
                elif opcion == "4":
                    lista_range = ListFromRange(self.lista)
                    lista_range.create_list()
                    self.lista = lista_range.lista
                elif opcion == "5":
                    Help.show_help()
                elif opcion == "6":
                    print("Salió del programa.")
                    break
                else:
                    print("Seleccione una opción válida.")
                if opcion in ["1", "2", "3", "4"]:
                    self.submenu()

        except KeyboardInterrupt:
            print("""\n
            Adiós.
            Ocurrió interrupción del usuario.""")

    def submenu(self):
        try:
            original_lista = self.lista[:]
            while True:
                print("\nSubmenú:")
                print("a. Imprimir lista.")
                print("b. Ordenar con burbuja.")
                print("c. Ordenar con rápido.")
                print("d. Comparar con sorted().")
                print("e. Buscar elemento (búsqueda lineal).")
                print("f. Buscar elemento (búsqueda binaria).")
                print("g. Sumar elementos.")
                print("h. Calcular promedio.")
                print("i. Calcular mediana.")
                print("j. Calcular varianza.")
                print("k. Encontrar el mínimo.")
                print("l. Encontrar el máximo.")
                print("m. Mostrar longitud de la lista.")
                print("n. Comparar con otra lista.")
                print("o. Volver al menú principal.")
                opcion = input("Seleccione una opción: ")

                if opcion == "a":
                    if original_lista:
                        print("Lista original:", original_lista[:10])
                    else:
                        print("No hay lista original generada.")
                elif opcion == "b":
                    if original_lista:
                        tiempo_inicio = time.time()
                        SearchAndSort.bubble_sort(self.lista)
                        tiempo_final = time.time()
                        print("Lista ordenada con burbuja:", self.lista[:10])
                        print("Tiempo de ejecución:", tiempo_final - tiempo_inicio, "segundos")
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "c":
                    if original_lista:
                        tiempo_inicio = time.time()
                        self.lista = SearchAndSort.quick_sort(self.lista)
                        tiempo_final = time.time()
                        print("Lista ordenada con rápido:", self.lista[:10])
                        print("Tiempo de ejecución:", tiempo_final - tiempo_inicio, "segundos")
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "d":
                    if original_lista:
                        algo_comparison = AlgorithmComparison()
                        tiempo_bubble, tiempo_quick, tiempo_sorted = algo_comparison.compare_algorithms(original_lista)
                        print("Tiempo de ejecución (burbuja):", tiempo_bubble, "segundos")
                        print("Tiempo de ejecución (rápido):", tiempo_quick, "segundos")
                        print("Tiempo de ejecución (sorted()):", tiempo_sorted, "segundos")
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "e":
                    if original_lista:
                        try:
                            elemento = int(input("Ingrese el elemento que desea buscar: "))
                            tiempo_inicio = time.time()
                            LinearSearch.linear_position(original_lista, elemento)
                            tiempo_final = time.time()
                            print("Tiempo de ejecución:", tiempo_final - tiempo_inicio, "segundos")
                        except ValueError:
                            print("Error: Por favor, ingrese solo números.")
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "f":
                    if original_lista:
                        try:
                            elemento = int(input("Ingrese el elemento que desea buscar: "))
                            tiempo_inicio = time.time()
                            BinarySearch.binary_position(original_lista, elemento)
                            tiempo_final = time.time()
                            print("Tiempo de ejecución:", tiempo_final - tiempo_inicio, "segundos")
                        except ValueError:
                            print("Error: Por favor, ingrese solo números.")
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "g":
                    if original_lista:
                        suma = Stats.sum(original_lista)
                        print("La suma de los elementos en la lista es:", suma)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "h":
                    if original_lista:
                        promedio = Stats.mean(original_lista)
                        print("El promedio de los elementos en la lista es:", promedio)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "i":
                    if original_lista:
                        mediana = Stats.median(original_lista)
                        print("La mediana de la lista es:", mediana)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "j":
                    if original_lista:
                        varianza = Stats.variance(original_lista)
                        print("La varianza de la lista es:", varianza)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "k":
                    if original_lista:
                        minimo = Stats.minimum(original_lista)
                        print("El mínimo en la lista es:", minimo)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "l":
                    if original_lista:
                        maximo = Stats.maximum(original_lista)
                        print("El máximo en la lista es:", maximo)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "m":
                    if original_lista:
                        longitud = Stats.length(original_lista)
                        print("La longitud de la lista es:", longitud)
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "n":
                    if original_lista:
                        try:
                            segunda_lista = input("Ingrese los elementos de la segunda lista separados por comas: ").strip().split(",")
                            segunda_lista = [int(elementos) for elementos in segunda_lista]
                            if original_lista == segunda_lista:
                                print("Las listas son iguales.")
                            else:
                                print("Las listas son diferentes.")
                        except ValueError:
                            print("Error: Por favor, ingrese solo números y sepárelos con comas.")
                    else:
                        print("No hay lista original generada en este momento.")
                elif opcion == "o":
                    break
                else:
                    print("Seleccione una opción válida.")

        except KeyboardInterrupt:
            print("""\n
            Adiós.
            Ocurrió interrupción del usuario.""")

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
