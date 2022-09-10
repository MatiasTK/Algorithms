# Algoritmos

Recreación de los algoritmos mas populares y utilizados, hechos y explicados en python!

## Algoritmos de búsqueda

### _Linear Search(Búsqueda lineal)_

Es un método para encontrar un valor dentro de una lista (vector), en este método comprobamos de manera secuencial cada elemento para ver si coincide con el que estamos buscando o hasta que todos los elementos hayan sido comparados. Su complejidad es O(n).

![Animación búsqueda lineal](https://www.doabledanny.com/static/9ba362fd1cb889120f307638e2ecb8f4/gif.gif)

### _Binary Search(Búsqueda binaria)_

Sirve también para encontrar un valor dentro de una lista pero esta **debe estar ordenada**, lo que hace es ir comparando con el elemento en el medio del array, si no son iguales la mitad en el cual el valor no puede estar es eliminada y la búsqueda continua en la mitad hasta que el valor se encuentre o se termine de recorrer el array. Su complejidad es O(log n).

**Recomendación:** Aquí te dejo un link donde podrás visualizar como se realiza tanto una búsqueda binaria como una lineal: [Search visualization](https://www.cs.usfca.edu/~galles/visualization/Search.html)

![Animación búsquedas comparadas](https://c.tenor.com/Jl0YrqxnHmAAAAAd/binary-search-sequence-search.gif)

### _Depth First Search(Búsqueda en profundidad)_

Es un algoritmo para recorrer todos los nodos de un grafo o árbol de manera ordenada pero no uniforme, va expandiendo y visitando todos los nodos de forma recurrente de un camino, cuando este se queda sin nodos regresa y repite el proceso con los hermanos del nodo ya procesado. Este método se puede pensar como una **pila**. Su complejidad es O(V + E) siendo V el numero de vertices y E el numero de aristas(edge).
Su procedimiento seria el siguiente:

1. Apilo el vértice inicial.
2. Lo marco como visitado y lo quito de la pila.
3. Añado a la pila a sus vecinos y visito alguno de ellos.
4. Repito desde el punto 2, en caso de no tener ningún vecino ya que este es el ultimo puedo seguir con alguno de la pila.

**Recomendación:** [DFS visualization](https://www.cs.usfca.edu/~galles/visualization/DFS.html)

![Animación DFS](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

### _Breadth First Search(Búsqueda en anchura)_

Este método es parecido al anterior solo que en este caso vamos a pensarlo como una **cola**. Complejidad O(V + E).
Su procedimiento seria el siguiente:

1. Encolo el vértice inicial.
2. Lo marco como visitado y lo quito de la cola.
3. Añado a la cola a sus vecino y visito alguno de ellos.
4. Repetir desde el punto 2, en caso de no tener ningún vecino puedo seguir con los de la cola.

**Recomendación:** [BFS visualization](https://www.cs.usfca.edu/~galles/visualization/BFS.html)

![Animación BFS](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif?20100504223639)

**Comparación entre DFS y BFS**
![Comparación DFS/BFS](https://miro.medium.com/max/1280/1*GT9oSo0agIeIj6nTg3jFEA.gif)

## Algoritmos de ordenamiento

### Clasificación de algoritmos de ordenamiento

- In-place/Out-place -> Normalmente cuando nos referimos a algoritmos in place quiere decir algoritmos que su complejidad en el espacio es muy baja, en resumen: Algoritmos que usan poco almacenamiento.
- Recursion -> Algunos algoritmos pueden ser recursivos o no recursivos, hay algunos que incluso son los dos (merge sort).
- Estabilidad -> Un algoritmo estable es aquel que cuando hay elementos con claves iguales después de ordenarlos estos mantienen su orden relativo.

![Algoritmos estables](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Sorting_stability_playing_cards.svg/220px-Sorting_stability_playing_cards.svg.png)

### _Bubble Sort(Ordenamiento de burbuja)_

Es un método sencillo de ordenamiento, este compara cada elemento de la lista con el siguiente, si esta en el orden equivocado lo cambia de posición hasta que finalmente este en la posición correcta y luego repite el proceso con los demás números de la lista, es un algoritmo **estable** y también es **in-place**, se suele utilizar para aprender algoritmos de ordenamiento debido a su simpleza. Su complejidad es O(n^2)

![Animación bubble sort](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

### _Insertion Sort(Ordenamiento por inserción)_

Método sencillo de ordenamiento, es mas parecido a como ordenaría un humano por ejemplo un mazo de cartas. Lo que hace este método es ir comparando cada elemento de la lista con los métodos ya ordenados, de esta manera si encuentra un elemento menor o ya no encuentra elementos se tiene y pasa a repetir el proceso con el siguiente elemento, es un algoritmo **estable** y **in-place**, se suele utilizar en listas pequeñas o listas grandes que ya estén casi ordenadas. Su complejidad es O(n^2)

![Animación insertion sort](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

### _Selection Sort(Ordenamiento por selección)_

Ultimo método sencillo de ordenamiento, este ordena la lista comparando cada elemento para encontrar siempre el mínimo de los elementos no ordenados y asi finalmente lograr ordenar la lista, es un algoritmo **no estable** aunque hay implementaciones que lo hacen ser estable, es **in-place**, es util para cuando el vector esta casi ordenado. Su complejidad es O(n^2)

![Animación selection sort](https://i.makeagif.com/media/1-24-2016/VrJ-Br.gif)

### _Merge Sort(Ordenamiento por mezcla)_

Este método de ordenamiento basado en la técnica [divide and conquer(divide y vencerás)](https://es.wikipedia.org/wiki/Divide_y_vencer%C3%A1s).Es un algoritmo **estable** y y también **out-place** aunque hay una version in-place, suele ser recursivo, este algoritmo es util para ordenar **listas enlazadas** o cuando necesitas hacer **external sorting** osea ordenar grandes cantidades de datos.Su complejidad es de O(n log n).
Su funcionamiento es el siguiente:

1. Dividir la lista en dos subsistas "dividiéndola a la mitad"
2. Ordenas cada subsista de manera recursiva aplicando merge sort
3. Mezclas las dos subsistas en una lista ordenada

![Animación merge sort](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/220px-Merge-sort-example-300px.gif)

### _Quick Sort(Ordenamiento rápido)_

Es uno de los métodos de ordenamientos mas rápidos, a veces puede ser mas rápido que merge sort y dos o tres veces mas rápido que heapsort. Es un organismo de [divide and conquer(divide y vencerás)](https://es.wikipedia.org/wiki/Divide_y_vencer%C3%A1s). Hay dos tipos de manera de tomar la partición en este quicksort, esta la partición de Hoare y la de Lomuto, sus diferencias son que la de Hoare es mas compleja y utiliza y por lo tanto mas eficiente. En el algoritmo de Hoare se suele tomar como pivote inicial el primero mientras que en el de Lomuto se suele tomar el ultimo. Este algoritmo suele ser **no estable** aunque hay implementaciones para hacerlo estable, es **in-place**, normalmente se suele utilizar para **ordenar arrays** a diferencia del mergesort que se usa para listas enlazadas. Su complejidad en el peor de los casos es O(n^2) que esto va a ser cuando el array ya esta ordenado o prácticamente ordenado, sin embargo en promedio suele tomar O(n log n).
Su funcionamiento seria el siguiente:

1. Se toma como pivote el ultimo elemento.
2. Desde la izquierda se toma el primer elemento que es mas grande que el pivote
3. Desde la derecha se toma el primer elemento que es mas chico que el pivote
4. Se hace un swap
5. Se repite desde 2. Pero si el item de la derecha se pasa significa que ya completamos por lo tanto hacemos un ultimo swap del item de la izquierda con el pivote.
6. Ahora vamos a tener una lista dividida en dos partes a la izquierda y derecha del pivote, en cada nueva lista aplico desde el item 1 hasta que quede una lista con 1 elemento.

![Animación quick sort](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif)

Demostración con el método de Hoare

**¿Seguís sin entenderlo?** Quizás este [video](https://www.youtube.com/watch?v=Hoixgm4-P4M&) pueda ayudarte

### _Counting Sort(Ordenamiento por cuentas)_

Es un algoritmo de ordenamiento en el cual se cuenta el número de elementos de cada clase para ordenarlos, solo puede ser utilizado por elementos contables (enteros). La version original del counting sort no puede ser utilizada para ordenar una lista con números negativos sin embargo hay una version que mejora esto. Este algoritmo suele ser **no-estable**, es **out-place**. Su complejidad es O(n + k) siendo k la cantidad de números no negativos.
Su funcionamiento es el siguiente:

1. Se busca el mínimo y el máximo de la lista
2. Se crea un vector auxiliar
3. Se recorre la lista de números y se cuenta los elementos, ejemplo si el numero 2 esta 4 veces en la lista entonces en el vector_auxiliar[2] = 4
4. Recorro el vector auxiliar y asi obtengo la lista ordenada

![Animación counting sort](https://camo.githubusercontent.com/a35a31e6076f51eab50ba224df0e237d85c029c9550e00dd11ae39fdce7fd3c8/68747470733a2f2f332e62702e626c6f6773706f742e636f6d2f2d6a4a63686c7931426b54632f574c4771434644647643492f41414141414141414148412f6c756c6a416c7a3270744d6e64495a4e48304b4c545475514d4e73667a44654651434c63422f73313630302f43536f72745570646174656453746570492e676966)

### _Heap Sort(Ordenamiento por montículos)_

Consiste en aprovechar las propiedades del árbol heap el cual siempre en su nodo raíz tendrá el elemento de mayor valor, por lo tanto solo tenemos que ir extrayendo siempre su raíz, luego de cada extracción el algoritmo pone en su nueva raíz a la ultima hoja derecha por el ultimo nivel (Lo cual hace que deje de ser un heap) pero mediante sift-down(el cual recupera la propiedad de heap) o sift-up este puede volver a utilizarse. Recordar que este algoritmo no puede ser utilizado directamente sobre una lista ya que esta debe pasar por un proceso de heapify(convertirlo en heap) antes. Es un algoritmo **no estable** y **in-place**, este algoritmo puede ser util cuando nos queremos **garantizar una complejidad O(n log n)** ya que quicksort no la garantiza y a su vez cuando queremos **garantizar no usar memoria extra** como es en el merge sort.Su complejidad es O(n log n)

![Animación heap sort](https://upload.wikimedia.org/wikipedia/commons/4/4d/Heapsort-example.gif)
En esta demostración podemos ver como se aplica heapify para luego aplicar heap sort.

### Comparativa entre ordenamientos

- [Comparación de Sorts visualizador online](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)
- [Video comparativa entre sorts](https://www.youtube.com/watch?v=ZZuD6iUe3Pc)
- [Articulo Wikipedia comparación entre algoritmos](https://en.wikipedia.org/wiki/Sorting_algorithm#Comparison_of_algorithms)

### Gráfico de complejidad

![Gráfico complejidad](https://miro.medium.com/max/1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

## Notas

- La utilización de módulos de terceros networkX y matplotlib no son necesarios para el funcionamiento del código por lo tanto estos pueden ser removidos, sin embargo estos sirven para darnos una ayuda visual sobre el grafo.
- Las complejidades indicadas en este archivo siempre son teniendo en cuenta los peores casos de los algoritmos.
