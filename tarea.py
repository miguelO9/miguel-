# 1 Crea un diccionario vacío llamado perro
perro = {
    # 2 Añade nombre, color, raza, patas y edad al diccionario perro.
'nombre':'gema',
'color':'blanco',
'raza':'chanda',
'patas':'4',
'edad':'2 meses'
}
print(perro)

# 3 Crea un diccionario de estudiante y añade nombre,
# apellido, sexo, edad, estado civil, habilidades,
# país, ciudad y dirección como claves del diccionario
estudiante = {
    'nombre':'miguel',
    'apellido':'oyola',
    'sexo':'masculino',
    'edad':'20',
    'esatdo civil':'soltero',
    'habilidades':['entiende rapido','matematicas'],
    'pais':'colombia',
    'ciudad':'cartagena',
    'direccion':'tierra baja'
}

# 4 Obtén la longitud del diccionario del alumno
print(len(estudiante))

# 5 Obtenga el valor de las habilidades y compruebe el tipo de datos, debe ser una lista
print(type(estudiante['habilidades']))

# 6 Modifique los valores de las habilidades añadiendo una o dos habilidades.
hab=[estudiante['habilidades']]
hab.append('ajedrez')

# 7  Obtener las claves del diccionario como una lista
print(estudiante.items())

# 8 Obtener los valores del diccionario como una lista
valores = estudiante

# 9 Cambie el diccionario a una lista de tuplas utilizando el método items()

# 10 Eliminar uno de los elementos del diccionario
estudiante.popitem()
print(estudiante)
# 11 Borrar uno de los diccionarios
del estudiante
