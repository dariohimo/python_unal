"""

En este ejemplo se muestra la aplicación de los conceptos vistos en la tercera unidad del curso. 
Para esta ocasión desarrollaremos un programa que tenga el comportamiento básico de una lista de 
reproducción de música ordenada por artistas.


💡 Problema: Listas de reproducción (I)

Con el paso de los años, usted y su grupo de amigos han adquirido la costumbre de reproducir música cada vez que se reunen.
 A pesar de que tienen gustos similares cuando se trata de sus artistas preferidos, es muy difícil estar de acuerdo al elegir 
 cuál de las canciones de un artista les gustaría escuchar a continuación. Para esto, usted decide aplicar los conocimientos
  que ha adquirido en su curso de programación para crear un programa que tenga listas de reproducción por artista 
  y que permita al grupo simplemente decidir cuál artista les gustaría escuchar. Este programa generará comandos que usted 
  puede luego ingresar en cualquiera de las plataformas de streaming que tengan a su alcance.


En una hoja de papel plantean los requisitos básicos que el programa debe tener para permitir añadir canciones y 
reportar la próxima canción que se debe escuchar. Finalmente, deciden que el programa funcionará por medio de comandos
 recibidos de la entrada en forma de texto, y que realizará una tarea específica en cada caso. Inicialmente,
  el programa tendría los siguientes 3 comandos.


añadir: primero que nada, su programa debería permitir añadir canciones nuevas. Para esto, el usuario puede agregar el 
título de una canción de un artista determinado. Una vez recibe el comando añadir, el programa recibe, en las dos líneas siguientes, 
el nombre de la canción y el nombre de artista y lo agrega a la lista de reproducción.
reproducir: una vez usted y sus amigos han añadido las canciones que más les gusta, deberían poder
 "reproducir" la siguiente canción. Después de ingresar el comando reproducir, en la siguiente línea se 
 ingresa el nombre de un artista, el programa deberá escribir en pantalla la siguiente canción a reproducirse. 
 Para simplificar las cosas, las canciones se reproducirán en el orden en el que fueron añadidas, reproduciendo
  primero las canciones más antiguas y eliminando las canciones conforme se van reproduciendo. El texto que reporta
   este comando tiene 3 formas:
- Si el artista tiene canciones en cola, deberá escribir el texto: Reproduciendo <canción> de <artista>.,
 con el título de la canción y el nombre del artista correspondientes
- Si ya se reprodujeron todas las canciones de un artista, deberá escribir el texto: No quedan canciones en cola.
- Si el artista ingresado nunca ha tenido canciones registradas, deberá escribir el mensaje El artista no tiene canciones registradas.
detener: como el artista recibe un número indeterminado de canciones, se tiene que definir una forma de terminar su ejecución.
 Cuando el programa recibe el comando detener, el programa deberá escribir el mensaje Terminando sesión.
  ¡Hasta pronto! y terminar su ejecución.

En caso de que el comando ingresado esté mal escrito o sea desconocido por el programa, 
se deberá informar al usuario con el mensaje Comando no reconocido. Intente de nuevo:

Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá un número indefinido de líneas. Cada comando irá en una líne individual. De igual forma cada entrada adicional relacionada a un comando irá en una nueva línea.


- comando: Hay tres comandos posibles que el progama debe aceptar añadir, reproducir y detener. Cualquier otro texto de comando será tomado como erroneo.

Dependiendo del comando ingresado, el programa recibirá otras entradas:


- Para el caso del comando añadir, el programa recibirá canción y artista en el mismo orden. Cada entrada en una línea individual.
- Para el caso del comando reproducir, el programa recibirá una entrada extra artista en la siguiente línea.


🖥️ Salida

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
No quedan canciones en cola.
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
No quedan canciones en cola.
No quedan canciones en cola.
El artista no tiene canciones registradas.
Terminando la sesión. ¡Hasta pronto!


"""



canciones = dict()

while True:
    command = input()
    # añadir
    if command == 'añadir':
        cancion = input()
        artista = input()

        if artista not in canciones:
            canciones[artista] = list()
        canciones[artista].append(cancion)
    #
    #reproducir
    elif command == 'reproducir':
        artista = input()
        if artista in canciones:
            if len(canciones[artista]) > 0:
                cancion = canciones[artista].pop(0)
                print(f"Reproduciendo {cancion} de {artista}.")
            else:
                print(f"No quedan canciones en cola.")
        else:
            print(f"El artista no tiene canciones registradas.")
    elif command == 'listar':
        artista = input()
        if artista in canciones:
            indice = 1
        if len(canciones[artista]) > 0:
            for artista in canciones.items():
                print(f'{indice} {cancion}')
                indice += 1
        else:
            print("El artista no tiene canciones registradas.")
    # detener
    elif command == 'detener' :
        print("Terminando la sesión. ¡Hasta pronto!")
        break
    # desconocido
    else:
        print("Comando no reconocido. Intente de nuevo:")
