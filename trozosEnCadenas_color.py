"""
Problema: Representación numérica del color

Los colores que vemos en la pantalla de nuestros dispositivos electrónicos como el computador o los teléfonos inteligentes son codificados en forma de números.


Para lograr esto, se utiliza una de las propiedades de la luz visible, que nos permite considerar cada color como la intensidad de tres colores principales: rojo (red en inglés), verde (green en inglés) y azul (blue en inglés). Este tipo de codificación recibe el nombre de rgb, y es usada en los píxeles de las pantallas que usamos cada día.


Para un programador o un artista digital, un color en rgb no es más que tres valores enteros que van desde 0 hasta 255, con los cuales se representa la intensidad de los colores rojo, verde y azul. En esta codificación, 0 significa la ausencia de dicho color, y 255 significa su presencia con una intensidad máxima.


Por ejemplo, un color con componentes rgb (255, 0, 0) nos producirá el color rojo más puro, con su máximo de intensidad y ausencia total de colores verde y azul. Esto también aplica para el caso del color verde (0,255,0) y azul (0, 0, 255)

Le invitamos a escribir en Google "rgb 255 0 0" y ver la herramienta ofrecida como resultado, la cual permite variar los números y ver los tipos de colores que se van formando.


Para facilitar el trabajo y la selección de colores, es común utilizar otro tipo de representaciones para estos números. Una de esas formas es la notación hexadecimal, que normalmente se representa con una cadena de texto como #ff33a2, iniciando con el símbolo "#", seguido de seis dígitos hexadecimales. Cada dos dígitos representan un color rgb.

Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá un único valor de entrada:


- color: cadena de texto que representa un color en formato hexadecimal. La cadena contiene un valor hexadecimal que se encuentran entre #000000 hasta #ffffff.

Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida una única línea:


- color_rgb: el programa debe imprimir una cadena de texto de la forma R: <valor_r> G: <valor_g> B: <valor_b>, en donde cada valor corresponde a cada componente de color en formato decimal.

Ejemplos

¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1

#6e00ff
Salida Ejemplo 1

R: 110 G: 0 B: 255

Entrada Ejemplo 2

#28ad2f
Salida Ejemplo 2

R: 40 G: 173 B: 47

Entrada Ejemplo 3

#fadc82
Salida Ejemplo 3

R: 250 G: 220 B: 130

Notas

La conversión de números entre las bases decimal y hexadecimal se discutió en la primera unidad del curso. Para realizar la conversión de una cadena con un valor entero en base hexadecimal a un valor numérico en base decimal puede hacer lo siguiente:

color_int = int("ff", 16)


"""



color_int = int("ff", 16)

#print(color_int)


#color = "#6e00ff"

#color = "#28ad2f"
color = "#fadc82"
color2 = "#fadc82"


r = int(color[-6 : -4], 16)
g = int(color[-4 : -2], 16)
b = int(color[-2 : ], 16)
print("con menos")
print(r,g,b)
#print(int(r, 16))
#print(int(g, 16))
#print(int(r, g, b, 16))

print(f"R: {r} , G: {g} , B: {b}")
#print(b)

#R: 110 G: 0 B: 255

#funciona sin digitos extras.

print(color2[1:3], color2[3:5], color2[5:7])

valor_r = int(color2[1:3],16)
valor_g = int(color2[3:5],16)
valor_b = int(color2[5:7],16)

print(f"R: {valor_r} G: {valor_g} B: {valor_b}")