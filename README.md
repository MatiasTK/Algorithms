# Algoritmos

Recreacion de los algoritmos mas populares y utilizados, hechos y explicados en python!

## Algoritmos de busqueda

_Linear Search(Busqueda lineal):_ Es un metodo para encontrar un valor dentro de una lista (vector), en este metodo comprobamos secuencialmente cada elemento para ver si coincide con el que estamos buscando o hasta que todos los elementos hayan sido comparados. Su complejidad es O(n).

_Binary Search(Busqueda binaria):_ Sirve tambien para encontrar un valor dentro de una lista pero esta **debe estar ordenada**, lo que hace es ir comparando con el emento en el medio del array, si no son iguales la mitad en el cual el valor no puede estar es eliminada y la busqueda continua en la mitad hasta que el valor se encuentre o se termine de recorrer el array. Su complejidad es O(log n).

**Recomendacion:** Aqui te dejo un link donde podras visualizar como se realiza tanto una busqueda binaria como una lineal. [Search visualization](https://www.cs.usfca.edu/~galles/visualization/Search.html)

_Depth First Search(Busqueda en profundidad):_ Es un algoritmo para recorrer todos los nodos de un grafo o arbol de manera ordenada pero no uniforme, va expandiendo y visitando todos los nodos de forma recurrente de un camino, cuando este se queda sin nodos regresa y repite el proceso con los hermanos del nodo ya procesado. En forma resumida y mas entendible: vos tenes un grafo con dos elementos sus aristas(flechas que los une) y sus vertices, al recorrerlo en profundidad vas a tener un vertice inicial y una lista de visitados, vas a visitar al inicial lo añadis a la lista de deseados y luego haces lo mismo con sus vecinos, los visitas los marcas como visitados y luego visitas al vecino del vecino si es que no esta visitado, este termina una vez que no pueda seguir visitando a otros vecinos. Su complejidad es O(V + E) siendo V el numero de vertices y E el numero de aristas(edge).
**Recomendacion:** [BFS visualization](https://www.cs.usfca.edu/~galles/visualization/DFS.html)
