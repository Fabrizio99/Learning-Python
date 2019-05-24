x="Lenguaje De Programacion"

# accediendo a un caracter, indicando la posicion
#el primer caracter posee la posicion 0 y no 1
print(x[2])

#subcadenas
print(x[2:8])
print(x[::-1])  #inversa de una cadena
print(x[4:1:-1])

#longitud de un string
print(len(x))

# convertir los caracteres de un string en minuscula
print(x.lower())

# convertir los caracteres de un string en mayuscula
print(x.upper())

# reemplazas un string por otro
# convertir los caracteres de un string en minuscula
print(x.replace('e','3'))

#split()
# permite separar una cadena en subcadenas, indicando el separador
print(x.split('e'))

# input()
# permite ingresar datos por consola
print('Escriba su nombre:')
x=input()
print("Hola",x)