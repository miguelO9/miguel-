#1. Declarar una lista vacía
vector = []

#2. Declarar una lista con más de 5 elementos
lista = ['1','2','3','4','5','6','7']

#3. Encuentre la longitud de su lista
print("La longitud de la lista es: ",len(lista))

#4. Obtener el primer elemento, el elemento central y el último elemento de la lista
print("El primer elemento es",lista[0])
print("El elemento que esta en medio es",lista[3])
print("El ultimo elemento es",lista[6])

#5. Declara una lista llamada tipos_datos_mezclados, pon tu(nombre, edad, altura, estado civil, dirección)
tipo_dato_mezclado=['miguel',20,'1.82 CM', 'soltero','tierra baja']
print(tipo_dato_mezclado)

#6. Declare una variable de lista llamada it_companies y asígnele los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies=['facebook','google','microsoft','apple', 'ibm','oracle','amazon']
print(it_companies)

#7. Añadir una empresa de TI a it_companies utilizando los metodos de insercion.
it_companies.append('IT')
print(it_companies)

#8. Comprobar si una determinada empresa existe en la lista it_companies.
does_exist = 'google' in it_companies
print("La respuesta es: ",does_exist)#verdadero
does_exist = 'samsung' in it_companies
print("La respuesta es: ",does_exist)#falso

#9. Ordena la lista con el método sort()
it_companies.sort()
print(it_companies)

#10. Invierte la lista en orden descendente utilizando el método reverse()
it_companies.reverse()
print(it_companies)

#11. Elimine la primera empresa informática de la lista.
del it_companies[0]
print(it_companies)

#12. Eliminar todas las empresas de TI de la lista
it_companies.remove('IT')
print(it_companies)