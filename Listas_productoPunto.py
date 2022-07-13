"""
En esta práctica trabajaremos con el tipo de dato lista, su declaración, 
la operación de acceso a los elementos que contiene y su uso en forma de iterable con estructuras de control iterativas.

💡 Problema: Producto Punto

El producto punto o producto escalar es una de las operaciones básicas de álgebra lineal, 
una rama de las matemáticas que tiene en su centro el concepto de vector. En pocas palabras,
y sin entrar en detalles teóricos, un vector es un objeto matemático con una secuencia de números reales,
conocidos como componentes del vector. Esta secuencia tiene un tamaño, que es conocido como la dimensión del vector.

Por ejemplo, un vector a de dimensión 2, cuyos componentes son los números 0 y 1, se escribiría de la forma v=(10,2).

La operación de producto punto entre dos vectores u y v con la misma dimensión 
(que tienen la misma cantidad de elementos) consiste en realizar las siguientes operaciones:


- Multiplicar los componentes de cada vector que están ubicados en la misma posición.
 La operación no es válida para vectores con dimensión distinta.
- Sumar el resultado de los productos realizados en el paso anterior. 
De esta forma, el resultado es siempre un número, independientemente de la dimensión de los vectores.

Como se puede ver a continuación, el producto punto para los vectores u=(1,3,5) y v=(4,2,0) 
tendría la multiplicación de los componentes de cada vector en orden, de izquierda a derecha, y finalmente la suma de cada producto obtenido.

Para este ejemplo, el resultado se obtendría con la siguiente secuencia de operaciones:
u=(1,3,5) 

v=(4,2,0)

u⋅v=(1×4)+(3×2)+(5×0)

u⋅v=4+6+0

u⋅v=10

Para esta actividad deberá escribir un programa de Python que tome como entrada dos secuencias de números y calcule el producto
punto de los vectores correspondientes.

⌨️ Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa debe recibir dos entradas, cada una en una línea:

- vector_u: primera cadena de texto formada por n números enteros separados por espacios.
- vector_v: segunda cadena de texto formada por n números enteros separados por espacios.

Ambas cadenas de texto contienen la misma cantidad de números n. los valores internos son números enteros.

🖥️ Salida
¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. 
Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida una única línea:

producto_punto: valor numérico que representa el resultado de realizar la operación con los dos vectores.

🧩 Ejemplos

¿Cómo debe funcionar mi programa?

A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. 
Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1:

-32 -4 -13 -36 -7
-22 20 37 11 -38

Salida Ejemplo 1:
13

Notas

La entrada del programa es entregada en forma de cadena de texto.
 Para separar los elementos separados por espacio y convertirlos en enteros puede utilizar el siguiente código:

# Obtener una lista de números enteros

lista = [int(elemento) for elemento in input().split()]

Si lo desea, siéntase libre de crear su propia implementación.

"""
### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 6-11 líneas de código)
# Entrada del programa (~ 2-4 líneas).
# vectores a operar

vector_u = [int(elemento) for elemento in input().split()]
vector_v = [int(elemento) for elemento in input().split()]


# Cálculo del producto punto (~ 3-6 líneas).
producto_punto = 0

for i in range(len(vector_u)):
    producto_punto += (vector_u[i] * vector_v[i])

# Salida del programa (~ 1 línea).
print(producto_punto)
