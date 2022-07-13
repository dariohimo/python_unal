"""
En esta actividad se retomará problema descrito en el ejemplo anterior y se amplían los requisitos 
de la solución con el objetivo de evaluar la apropiación de los conceptos discutidos en la unidad.

Para efectos prácticos de la calificación el número que el usuario debe adivinar es dado al 
inicio de la ejecución, ya que es necesario que el juez pueda saber de antemano los resultados 
que se van a obtener; pero con unas cuantas modificaciones se pude obtener un número aleatorio 
de forma que termina siendo completamente oculto para el usuario. Esto se logra mediante el uso 
de una librería de Python (este tema será tratado en unidades posteriores del curso) la cual 
permite obtener números aleatorios de diferentes formas; entre ellas está la posibilidad de 
definir el intervalo en el que se quiere que se encuentre el número.


💡 Problema: Adivina el número (II)

El juego creado en el último evento fue un éxito total, por lo que se desea hacer el mismo 
juego para la próxima reunión del equipo del trabajo. El juego trataba de que los participantes 
deberán intentar adivinar un número secreto en un número determinado de intentos. 
Ahora, con un poco más de tiempo se decide implementar ciertas mejoras para hacer más interesante el juego.


El juego debe cumplir las siguientes reglas


- El organizador es quien debe ingresar el número secreto, un número máximo de intentos y el valor mínimo y máximo 
donde se puede encontrar el número secreto.
- El juego debe darle la bienvenida al jugador con el siguiente texto
- ¡Bienvenido! Por favor ingrese números entre <mínimo> y <máximo> para ganar.
- En cada ronda se debe indicar al jugador el número de intentos restantes con el que cuenta de la siguiente forma:
  Intentos restantes: <intentos>.
- El juego solo deberá permitir el ingreso de números entre el mínimo y máximo definidos como parámetros iniciales 
  (ambos valores están incluidos). Si el número ingresado no está dentro del intervalo, se debe imprimir el siguiente mensaje. 
  No se resta ningún intento y se avanza al siguiente turno.
- El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente
- Si el valor ingresado por el jugador es correcto se debe imprimir el siguiente mensaje
  ¡Felicidades! El número ingresado es correcto.
- En caso de que el valor ingresado sea incorrecto, pero el jugador aún tenga intentos, se debe indicar 
  al jugador si el número ingresado es mayor o menor al número secreto con uno de los siguientes dos mensajes, según corresponda
   Respuesta incorrecta. El número que ingresó es mayor que el número secreto.
   Respuesta incorrecta. El número que ingresó es menor que el número secreto.
- Si el jugador se queda sin intentos se debe imprimir el siguiente mensaje. No se indica si el número es mayor o menor que el número secreto
  Se acabaron los intentos. El número correcto era <valor>.
- Al finalizar el juego, sin importar el resultado, se debe imprimir el siguiente mensaje
   Fin del juego. ¡Gracias por participar!

Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá inicialmente dos líneas con los dos parámetros iniciales.


- num: número entero con el valor secreto que deberá intentar adivinar el jugador.
- intentos: número entero con el número máximo de intentos que puede realizar el jugador.
- min: valor mínimo del intervalo donde se puede encontrar el número secreto.
- max: valor máximo del intervalo donde se puede encontrar el número secreto.

Una vez definidos estos parámetros iniciales, se recibirán los intentos del jugador las veces que sean necesarias 
con un máximo de entradas igual al número de intentos definidos inicialmente.

Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. 
Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.

El programa debe imprimir en la salida las líneas que sean necesarias según el escenario correspondiente. 
Un ejemplo de ejecución es el descrito en la siguiente sección.

Ejemplos

¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. 
Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1

7
3
1
10
22
6
8
7
Salida Ejemplo 1

¡Bienvenido! Por favor ingrese números entre 1 y 10 para ganar.
Intentos restantes: 3.
El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente
Intentos restantes: 3.
Respuesta incorrecta. El número que ingresó es menor que el número secreto.
Intentos restantes: 2.
Respuesta incorrecta. El número que ingresó es mayor que el número secreto.
Intentos restantes: 1.
¡Felicidades! El número ingresado es correcto.
Fin del juego. ¡Gracias por participar!

Entrada Ejemplo 2

9
3
1
10
3
4
50
5

Salida Ejemplo 2

¡Bienvenido! Por favor ingrese números entre 1 y 10 para ganar.
Intentos restantes: 3.
Respuesta incorrecta. El número que ingresó es menor que el número secreto.
Intentos restantes: 2.
Respuesta incorrecta. El número que ingresó es menor que el número secreto.
Intentos restantes: 1.
El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente
Intentos restantes: 1.
Se acabaron los intentos. El número correcto era 9.
Fin del juego. ¡Gracias por participar!

ejemplo 3
-977
5
-1000
1000
977
0
-978
-977

ejemplo 4:
27
2
1
100
101
102
103
0
-10
-25
8
11111
420
27

"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 24 - 27 líneas de código)

# Entrada del programa (~ 4 líneas).
num = int(input())
intentos = int(input())
min = int(input())
max = int(input())

# Ciclo | variables | texto inicial (~ 19 - 21 líneas).
print(f"¡Bienvenido! Por favor ingrese números entre {min} y {max} para ganar.")

while intentos > 0:
       
    print(f"Intentos restantes: {intentos}.")
    adivinaNum = int(input())
       
    if adivinaNum == num:
            print("¡Felicidades! El número ingresado es correcto.")
            break
            
    if intentos == 1:
        print(f"Se acabaron los intentos. El número correcto era {num}.")
        break
        
    else:
        if adivinaNum < min or adivinaNum > max:           
            print("El número que ingresó no se encuentra en el rango de valores indicado. Intente nuevamente")
                 
        else:
            if adivinaNum > num:
                intentos -= 1
                print(f"Respuesta incorrecta. El número que ingresó es mayor que el número secreto.")    
       
            elif adivinaNum < num:
                intentos -= 1
                print(f"Respuesta incorrecta. El número que ingresó es menor que el número secreto.")
      
   
print("Fin del juego. ¡Gracias por participar!")