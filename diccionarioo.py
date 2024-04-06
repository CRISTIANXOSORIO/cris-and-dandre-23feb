

perro = {}

perro ['Nombre'] = 'hernando'
perro['Color'] = 'marron'
perro['Raza'] = 'labrador'
perro['Patas'] = '4'
perro['edad'] ='5 años'

Estudiante = {}
Estudiante ['nombre'] = 'Cristian'
Estudiante['Apellido'] = 'Osorio'
Estudiante['Sexo'] = 'Masculino'
Estudiante['Edad']= '22'
Estudiante ['Estado civil'] = 'Soltero'
Estudiante ['habilidades']= 'los deportes'
Estudiante ['país'] = 'Colombia'
Estudiante ['Ciudad'] = 'Cartagena'
Estudiante ['Dirección'] = 'villa de la candelaria'


print("longitud de la lista estudiante: " + str(len(Estudiante)))

print(Estudiante['habilidades'])

Estudiante['habilidades'] = "destreza mental",

llaves = Estudiante.keys()
print((llaves))

valores = Estudiante.values()
print((valores))

print(Estudiante.items())

Estudiante.pop('país')
print((Estudiante))

del Estudiante


