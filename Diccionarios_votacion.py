"""
En esta práctica trabajaremos con el proceso de creación de diccionarios
y de acceso a su contenido por medio de estructuras iterativas.
Problema: Votación

En una institución educativa de educación media se está realizando el proceso de elección de un representante estudiantil,
 que cumplirá con este rol en el transcurso del año. En esta edición, las directivas de la institución están trabajando 
 por implementar nuevas tecnologías y han decidido solicitar la creación de un programa que haga el recuento de las votaciones.


Para una prueba de la utilidad de la idea en la próxima votación, se decidió usarla como apoyo en el conteo de los votos.
 Para esto, un jurado de votación introducirá por nombre el candidato de cada una de las boletas de su mesa. Finalmente,
  el programa escribirá un reporte con el nombre del ganador.


Escriba un programa que reciba una lista de votos por diferentes candidatos y calcule cuál es el candidato ganador. 
Si hay un empate el programa debe imprimir la palabra EMPATE. En caso contrario, debe imprimir el nombre del candidato ganador.

Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá n + 1 líneas de entrada:


- n: La primera línea de la entrada contiene un entero n indicando el número de votos totales.
- nombres Después de la primera línea, el programa recibirá un total de n lineas con el nombre del candidato registrado en el voto.

Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.


El programa debe imprimir en la salida una única línea.


- resultado cadena de texto con el nombre del candidato ganador o con la palabra EMPATE si dos o más candidatos tiene el mismo número de votos.

Ejemplos

¿Cómo debe funcionar mi programa?
A continuación, podrá ver y comparar sus resultados con algunos casos de prueba de ejemplo. 
Utilice las entradas provistas y compare el resultado con las salidas correspondientes.

Entrada Ejemplo 1

5
Juan
María
Pedro
María
Juan
Salida Ejemplo 1

EMPATE

Entrada Ejemplo 2

6
Juan
María
Pedro
María
Juan
María

Salida Ejemplo 2

María

###
1
Pedro



##########

En el diseño de este programa, no se contempla la posibilidad de tener de antemano los nombres de todos
 los candidatos que participaron en la elección. En su lugar, el jurado encargado puede ingresar cualquier nombre,
  que se debe ir guardando. Para este problema, necesitamos una colección que cumpla con lo siguiente:


- La colección debe permitir el acceso por nombre del candidato, el cual es una cadena de texto recibida en la entrada.
- La colección debe permitir tener el registro de un número entero con la cantidad de votos asociados a cada candidato.

Lo apropiado en este caso es usar un diccionario, donde la clave es una cadena con el nombre del candidato 
y el valor es un número entero mayor o igual a 1.

Además, tenemos dos escenarios cuando recibimos un nombre nuevo:

# Creamos el registro con un voto para el candidato.

votos[candidato] = 1

- El candidato tiene por lo menos un voto. Si el candidato ya tiene una pareja clave-valor, podemos afirmar que se ha registrado por lo menos un voto en el pasado. En este caso, nos interesa sumar 1 voto a la cantidad anterior, que solo existiría y solo conoceríamos si en su momento creamos un registro inicial con 1 voto.

# Sumamos un voto para el registro del candidato.

votos[candidato] += 1

La forma más clara para realizar esa comprobación es mediante el uso de condicionales:

# opción 1

if nombre in candidatos:
  # El candidato YA tiene votos.
else:
  # El candidato todavía NO tiene votos.

########

Flujo de la votación
El programa puede ser planteado con dos etapas distintas:

Se reciben todos los votos y se registran en una colección.

Exploramos la colección para identificar un candidato ganador o la presencia de un empate.

Nuestro programa debería poder recibir una cantidad variable de votos para entradas distintas.
Para determinar el momento en el que se deja de recibir entradas, es importante tener una 
condición que nos indique que se recibió el último voto. Como tenemos el número de votos que se deben esperar,
podemos simplemente usar un programa con un número exacto de iteraciones con la ayuda de un rango numérico:

# En este ejemplo se esperan 10 votos.
# En su programa, este número está dado en la primera entrada del programa

n = 10

# Iteramos sobre los números entre 0 y n - 1, con un total de n iteraciones.

for i in range(n):
  # 1. Obtenemos el voto número 'i'
  # 2. Guardamos el voto en nuestra colección

Una vez termina este ciclo, debemos obtener el cantidato con el máximo de votos.
Dado que los diccionarios no tienen orden, tenemos que iterar en el diccionario e identificar el valor
con número máximo de votos. Para esto, podemos usar nuevamente una estructura iterativa, iterando sobre 
las parejas de clave-valor en el diccionario.

Por cada candidato, se compara los votos que obtuvó con los del candidato que va ganando hasta ese momento.
Recuerde, si queremos que una variable conserve su valor para distintas iteraciones de nuestro ciclo 
tenemos que declarar su valor antes del inicio del mismo.

# ¿qué información necesitamos del candidato que va ganando?
# Esta variable debería cambiar en el ciclo que le sigue.

ganador = ...

for candidato, conteo in votos.items():

  # Revisamos el número de votos del candidato actual
  # ¿Tiene más votos que el que va ganando?

Tenga especial cuidado en el caso de los empates. Si el candidato actual tiene la misma cantidad de votos que el que va ganando,
debería marcarse como un empate, sin importar si ocurre con 2 o con más candidatos.

"""

num_entradas = int(input()) 

candidatos = {} 

#if nombres in votos:

for i in range(num_entradas):
    
    nombres = input().capitalize()  #.lower() 

    if nombres in candidatos:
       candidatos[nombres] +=  1       #candidatos[nombres] + 1
    else:
       candidatos[nombres] = 1


max_key = max(candidatos, key=lambda key: candidatos[key])

max_keys = [key for key, value in candidatos.items() if value == max(candidatos.values())]
print("keys vvv",max_keys)
print("len vvv", len(max_keys), len(max_key))

#consultaCandidatos = candidatos[0]

#"print("datos", consultaCandidatos)

"""
if votos.values() != votos.values():  
    print("EMPATE")
else:
    print(f"\n {max_key}")

"""

#max_item = max(candidatos.values())

#print("\n" , max_item, max_key)
#type(max_item)

maximo = max(candidatos.values())
#print("max >>>>", maximo)

#max(candidatos.values())

sumCandidato = 0

print("\n")
#print(candidatos, maximo)

for nom, voto in candidatos.items():
    #max(votos.values())
#   #print(f"if > {maximo}")
    #print(nombre, voto)
    #print(type(voto))
    #print(sumCandidato)
    
       
    if voto == max(candidatos.values()) :
       sumCandidato += 1
       #print(nom, sumCandidato)
       #break
       if voto == num_entradas:
           print(nom)
            
       if sumCandidato > 1:
           print("EMPATE")
           break
       

    else:
        print(max_key)
        break
    #print("sino", nom, voto, sumCandidato, max(candidatos.values()))

#print(nom)
#print("Empates+++++")



#print("empate **")

#print(f"totalCandidato:", sumCandidato)
    
        

#for nom,vot in candidatos.items():
#    if vot > maximo:
#        print(nom)


        #print(f"if > {nombre}  {votacion} {max_item}")
#        break
    #print(f"for {candidato}, {votacion}")

#print(f"Gano >> {max_key} ")
#max_key2 = max(votos, key = votos.get)
#print(max_key)

#print(f"maximo valor {max(votos.values()), votos.items() }  ")

#print(type(nombres)) 

print("\n", candidatos, sumCandidato )

