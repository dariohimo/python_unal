"""
En esta actividad retomaremos el problema descrito en el anterior ejemplo, ampliando las 
funcionalidades que debe cumplir el programa objetivo.

💡 Problema: Listas de reproducción (II)

El programa ha sido un éxito en las reuniones con su grupo de amigos. El proceso de elegir canción se ha simplificado, 
y pueden poner su atención en otras actividades. Sin embargo, tras discutirlo varias veces con sus amigos, se decide que estaría bien que el programa permitiera listar las canciones que siguen a continuación para un artista y que en vez de eliminar las canciones reproducidas, estas fueran añadidas al final de la cola para tener una reproducción ilimitada.

Vuelven a revisar los detalles del programa, y definen que tendrá los siguientes 4 comandos:

añadir: primero que nada, su programa debería permitir añadir canciones nuevas. Para esto, el usuario puede agregar el título
de una canción de un artista determinado. Una vez recibe el comando añadir, el programa recibe, en las dos líneas siguientes,
el nombre de la canción y el nombre de artista y lo agrega a la lista de reproducción.

reproducir: una vez usted y sus amigos han añadido las canciones que más les gustan, deberían poder "reproducir" 
la siguiente canción. Después de ingresar el comando reproducir, en la siguiente línea se ingresa el nombre de un artista,
el programa deberá escribir en pantalla la siguiente canción a reproducirse. Las canciones se reproducirán en el orden en el 
que fueron añadidas, reproduciendo primero las canciones más antiguas y continuando en la lista de reproducción por orden de llegada.
Cuando se reproduce la última canción, la próxima canción que se reproduzca será la primera canción que se agregó a la lista originalmente. 
El texto que reporta este comando tiene 3 formas:

- Si el artista tiene canciones en cola, deberá escribir el texto: Reproduciendo <canción> de <artista>.,
  con el título de la canción y el nombre del artista correspondientes, tal como quedaron registrados.
- Si el artista ingresado nunca ha tenido canciones registradas, deberá escribir el mensaje El artista no tiene canciones registradas.

detener: como el artista recibe un número indeterminado de canciones, se tiene que definir una forma de terminar su ejecución. 
Cuando el programa recibe el comando detener, el programa deberá escribir el mensaje Terminando sesión. ¡Hasta pronto! y terminar su ejecución.

listar: este nuevo comando deberá permitir al usuario ver la lista de canciones de un artista en el orden en el que se van a reproducir. 
Primero recibirá del usuario el nombre del artista a explorar, y luego imprimirá en pantalla las canciones con el mostrado a continuación.

Deberá escribir antes del título de la canción, un número que indique su posición en la lista de reproducción, empezando 
desde el número 1 siendo la próxima canción a reproducir.

1. Speak to me
2. Breathe
3. On the Run
4. Time
5. The Great Gig in the Sky

En caso de que el comando ingresado esté mal escrito o sea desconocido por el programa,
 se deberá informar al usuario con el mensaje Comando no reconocido. Intente de nuevo:.

Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. 
Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá un número indefinido de líneas. Cada comando irá en una líne individual. 
De igual forma cada entrada adicional relacionada a un comando irá en una nueva línea.


- comando: Hay tres comandos posibles que el progama debe aceptar añadir, reproducir y detener. 
Cualquier otro texto de comando será tomado como erroneo.

Dependiendo del comando ingresado, el programa recibirá otras entradas:


- Para el caso del comando añadir, el programa recibirá canción y artista en el mismo orden. Cada entrada en una línea individual.
- Para el caso del comando reproducir, el programa recibirá una entrada extra artista en la siguiente línea.
- Para el caso del comando listar, el programa recibirá una entrada extra artista en la siguiente línea.

Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. 
Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.


El programa debe imprimir en la salida las líneas que sean necesarias según el escenario correspondiente. 
Un ejemplo de ejecución es el descrito en la siguiente sección.

Ejemplos

¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1

añadir
Feel Good Inc.
Gorillaz
reproducir
gorillaz
reproducir
Gorillaz
reproducir
Gorillaz
ditinir
detener
Salida Ejemplo 1

El artista no tiene canciones registradas.
Reproduciendo Feel Good Inc. de Gorillaz.
Reproduciendo Feel Good Inc. de Gorillaz.
Comando no reconocido. Intente de nuevo:
Terminando la sesión. ¡Hasta pronto!

Entrada Ejemplo 2

añadir
Yesterday
The Beatles
añadir
El día de mi suerte
Héctor Lavoe
Let it Be
añadir
Let it Be
The Beatles
reproducir
The Beatles
reproducir
The Beatles
reproducir
Héctor Lavoe
reproducir
The Beatles
reproducir
The Beatles
reproducir
Shakira
detener
Salida Ejemplo 2

Comando no reconocido. Intente de nuevo:
Reproduciendo Yesterday de The Beatles.
Reproduciendo Let it Be de The Beatles.
Reproduciendo El día de mi suerte de Héctor Lavoe.
Reproduciendo Yesterday de The Beatles.
Reproduciendo Let it Be de The Beatles.
El artista no tiene canciones registradas.
Terminando la sesión. ¡Hasta pronto!








values = ["a", "b", "c"]

index = 1

for value in values:
    print(index, value)
    index += 1
"""

canciones={}

while True: 
    comando= input() 
    if comando=="añadir":
        cancion=input()
        artista=input()
    
        if artista not in canciones:
            canciones[artista]=list() 
        if artista in canciones:
            canciones[artista].append(cancion) 
    #reproducir
    elif comando=="reproducir": 
        artista = input() 
        if artista in canciones: 
            if len(canciones[artista]) > 0: 
                cancion=canciones[artista]   #.pop(0) 
                print(f"Reproduciendo {cancion} de {artista}.")
            else: 
                print(f"No quedan canciones en la cola.")
        else: 
            print(f"El artista no tiene canciones registradas.")

    elif comando=="detener":
        print(f"Terminando la sesión. ¡Hasta pronto!") 
        break

    elif comando == "listar":
        artista=input() 
        if artista in canciones: 
          indice=1
        if len(canciones[artista]) > 0:
            for i in range (0,len(canciones[artista])): 
                print(f"{indice}. {cancion}") 
                indice += 1 
        else: 
            print(f"El artista no tiene canciones registradas.")

    else: 
        print(f"Comando no reconocido. Intente de nuevo:")