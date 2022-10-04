nombre = str(input('Hola cual es tu nombre(s)? '))
while(nombre == ''):
	nombre = str(input('No puedes avanzar, ingresa tu nombre(s)? '))

apellidop = str(input('Cuales tu apellido paterno? '))
while(apellidop == ''):
    apellidop = str(input('No puedes avanzar, ingresa tu apellido paterno: '))

apellidom = str(input('Y tu apellido materno? '))
while(apellidom == ''):
    apellidom = str(input('No puedes avanzar, ingresa tu apellido materno: '))

edad = int(input(F'Bienvenido {nombre} {apellidop} {apellidom} comenzemos a calcular tu IMC ingresando tu edad?'))
peso = float(input( 'tu peso en kilogramos: '))
altura = float(input( 'y tu altura en metros: '))

imc = round((peso)/(altura ** 2), 2)
if imc >= 30:
    print(f'Gracias {nombre} {apellidop} {apellidom} tu Indice de Masa Moscular es: {imc} y es catalogado como Obesidad')
elif 25.9 <= imc < 30:
    print(f'Gracias {nombre} {apellidop} {apellidom} tu Indice de Masa Moscular es: {imc} y es catalogado como Sobrepeso')
elif 18.5 <= imc < 25.9:
    print(f'Gracias {nombre} {apellidop} {apellidom} tu Indice de Masa Moscular es: {imc} y es catalogado como Peso Saludable')
elif imc < 18.5:
    print(f'Gracias {nombre} {apellidop} {apellidom} tu Indice de Masa Moscular es: {imc} y es catalogado como Bajo peso')



