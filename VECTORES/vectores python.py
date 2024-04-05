

vacio = []


deportes = ['futbol', 'baloncesto', 'tenis','veisbol', 'bmx','atletismo']

print(len(vacio))
print('Numero de elementos de la lista deportes:',len(deportes))

   
primerdeporte  = deportes[0]
print("Primer deporte: " + primerdeporte)
deportedelcentro = deportes[len(deportes)//2]
print("deporte del centro: " + deportedelcentro)
ultimodeporte  = deportes[-1]
print("Ultimo deporte: " + ultimodeporte)


Datos_personales = []
Datos_personales.append("Cristian")
Datos_personales.append(22)
Datos_personales.append(1.80)
Datos_personales.append("soltero")
Datos_personales.append("villa de la candelaria")



it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']


it_companies.insert(4,'Acer')
print(it_companies)


does_exist = 'Facebook' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

revertir_lista = it_companies[::-1]
print(revertir_lista)

it_companies.pop(0)
print(it_companies)

del it_companies [4]
print(it_companies)

it_companies.clear()
print(it_companies)