"""
En esta práctica trabajaremos en la creación de conjuntos de Python,
 y en la aplicación práctica de sus operaciones básicas.

💡 Problema: Semejanza de textos

¿Cómo podemos conocer si dos textos son semejantes?

Una forma de medir la semejanza entre dos textos, se plantea medir esta semejanza con la cantidad de palabras y 
signos de puntuación utilizados y compartidos por ambos textos.

En primer lugar, se podría conocer cuantas palabras distintas fueron usadas en total al escribir los dos textos, 
para tener una idea del tamaño del vocabulario usado por sus escritores. Además, para determinar si podría tenerse
una semejanza se podría ver los términos repetidos, calculando cuantas de estas palabras se encuentran tanto en el
primer documento como en el segundo.

En esta actividad deberá escribir un programa que reciba dos líneas con cadenas de texto distintas, y que imprima 
como resultado el número de palabras compartidas y el total de palabras únicas encontradas en ambas cadenas.

Por ejemplo, si vemos las siguientes dos frases: "vaso medio lleno" y "vaso medio vacío". 
Podemos notar que comparten "vaso" y "medio", por lo que nuestro valor para palabras compartidas es 2. 
Además, tenemos las palabras "vacío" y "lleno", las cuales son únicas, ya que pertenecen a la primera o a la segunda frase,
 pero no a ambas, por lo que tendríamos un valor de 2 para palabras únicas.
"""



listado_a = (input()).split()
listado_b = (input()).split()


lis_a = set(listado_a)
lis_b = set(listado_b)

#print(listado_a)
#print(listado_b)
print(lis_a)
print(lis_b)
print(lis_a & lis_b)
print(len(lis_a & lis_b))
print(lis_a ^ lis_b)
print(len(lis_a ^ lis_b))