# Algoritmos

Recreacion de los algoritmos mas populares y utilizados, hechos y explicados en python!

## Algoritmos de busqueda

**_Linear Search(Busqueda lineal):_** Es un metodo para encontrar un valor dentro de una lista (vector), en este metodo comprobamos secuencialmente cada elemento para ver si coincide con el que estamos buscando o hasta que todos los elementos hayan sido comparados. Su complejidad es O(n).

**_Binary Search(Busqueda binaria):_** Sirve tambien para encontrar un valor dentro de una lista pero esta **debe estar ordenada**, lo que hace es ir comparando con el emento en el medio del array, si no son iguales la mitad en el cual el valor no puede estar es eliminada y la busqueda continua en la mitad hasta que el valor se encuentre o se termine de recorrer el array. Su complejidad es O(log n).

**Recomendacion:** Aqui te dejo un link donde podras visualizar como se realiza tanto una busqueda binaria como una lineal. [Search visualization](https://www.cs.usfca.edu/~galles/visualization/Search.html)

**_Depth First Search(Busqueda en profundidad):_** Es un algoritmo para recorrer todos los nodos de un grafo o arbol de manera ordenada pero no uniforme, va expandiendo y visitando todos los nodos de forma recurrente de un camino, cuando este se queda sin nodos regresa y repite el proceso con los hermanos del nodo ya procesado. Este metodo se puede pensar como una **pila**. Su complejidad es O(V + E) siendo V el numero de vertices y E el numero de aristas(edge).
Su procedimiento seria el siguiente:

1. Apilo el vertice inicial.
2. Lo marco como vistado y lo quito de la pila.
3. Añado a la pila a sus vecinos y visito alguno de ellos.
4. Repito desde el punto 2, en caso de no tener ningun vecino ya que este es el ultimo puedo seguir con alguno de la pila.

**Recomendacion:** [BFS visualization](https://www.cs.usfca.edu/~galles/visualization/DFS.html)

**_Breadth First Search(Busqueda en anchura):_** Este metodo es parecido al anterior solo que en este caso vamos a pensarlo como una **cola**. Complejidad O(V + E)
Su procedimiento seria el siguiente:

1. Encolo el vertice inicial.
2. Lo marco como visitado y lo quito de la cola.
3. Añado a la cola a sus vecino y visito alguno de ellos.
4. Reptio desde el punto 2, en caso de no tener ningun vecino puedo seguir con los de la cola.

**Recomendacion:** [DFS visualization](https://www.cs.usfca.edu/~galles/visualization/BFS.html)

## Notas

La utilización de modulos de terceros networkX y matplotlib no son necesarios para el funcionamiento del codigo por lo tanto estos pueden ser removidos sin embargo estos sirven para darnos una ayuda visual sobre el grafo.
