"""
En este ejemplo se demuestra la aplicación de los conceptos vistos durante la segunda unidad del curso. Para esta ocasión se desarrollará un pequeño juego donde el usuario intente adivinar un número entero con una cantidad máxima de intentos.


Para efectos prácticos de la calificación el número que el usuario debe adivinar es dado al inicio de la ejecución, ya que es necesario que el juez pueda saber de antemano los resultados que se van a obtener; pero con unas cuantas modificaciones se pude obtener un número aleatorio de forma que termina siendo completamente oculto para el usuario. Esto se logra mediante el uso de una librería de Python (este tema será tratado en unidades posteriores del curso) la cual permite obtener números aleatorios de diferentes formas.


💡 Problema: Adivina el número (I)

En un evento social organizado por su equipo de trabajo se considera la idea de realizar una especie de juego o concurso básico con el cual entretener a los asistentes. Tras una sesión de intercambio de ideas, se decide implementar un juego sencillo controlado por computador con texto. Este es un juego de adivinanzas en el cual los participantes deberán intentar adivinar un número secreto en un número determinado de intentos.


El juego debe cumplir las siguientes reglas.


El organizador es quien debe ingresar el número secreto y un número máximo de intentos al programa
En cada ronda se debe indicar al jugador el número de intentos restantes con el que cuenta de la siguiente forma
Intentos restantes: <intentos>.
Si el valor ingresado por el jugador es correcto se debe imprimir el siguiente mensaje
¡Felicidades! El número ingresado es correcto.
En caso de que el valor ingresado sea incorrecto, se debe imprimir el siguiente mensaje y restar un intento
Respuesta incorrecta. Intente de nuevo.
Si el jugador se queda sin intentos se debe imprimir el siguiente mensaje
Se acabaron los intentos. El número correcto era <valor>.
Al finalizar el juego, sin importar el resultado, se debe imprimir el siguiente mensaje
 Fin del juego. ¡Gracias por participar!


Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá inicialmente dos líneas con los dos parámetros iniciales.


- numero_secreto: número entero con el valor secreto que deberá intentar adivinar el jugador.
- intentos: número entero con el número máximo de intentos que puede realizar el jugador.

Una vez definidos estos parámetros iniciales, se recibirán los intentos del jugador las veces que sean necesarias con un máximo de entradas igual al número de intentos definidos inicialmente.



🖥️ Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.


El programa debe imprimir en la salida las líneas que sean necesarias según el escenario correspondiente. Un ejemplo de ejecución es el descrito en la siguiente sección.

Ejemplos

¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. Utilice las entradas provistas y compare el resultado con las salidas correspondientes.


Entrada Ejemplo 1

7
3
22
6
8
Salida Ejemplo 1

Intentos restantes: 3.
Respuesta incorrecta. Intente de nuevo.
Intentos restantes: 2.
Respuesta incorrecta. Intente de nuevo.
Intentos restantes: 1.
Se acabaron los intentos. El número correcto era 7.
Fin del juego. ¡Gracias por participar!

Entrada Ejemplo 2

9
3
3
4
5
Salida Ejemplo 2

Intentos restantes: 3.
Respuesta incorrecta. Intente de nuevo.
Intentos restantes: 2.
Respuesta incorrecta. Intente de nuevo.
Intentos restantes: 1.
Se acabaron los intentos. El número correcto era 9.
Fin del juego. ¡Gracias por participar!
"""


print("ingrese un numero")
num = int(input())
print("ingrese intentos")
intentos = int(input())

while intentos > 0:
    print(f"Intentos restantes: {intentos}.")
    print("adivina")
    intento = int(input())

    if intento == num:
        print("¡Felicidades! El numero ingresado es correcto.")
        break

    else:
        intentos -= 1

        if intentos == 0:
            print(f"Se acabaron los intentos. El numero correo era {num}.")
        else:
            print("Respuesta incorrecta. Intente de nuevo.")


print("Fin del juego. ¡Gracias por participar!")



