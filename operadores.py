#Operadores aritmeticos
print(3+4)  #suma
print(5-2)  #resta
print(3*5)  #multiplicacion
print(7/4)  #division
print(7%4)  #modulo
print(3**2)  #potencia
print(7//4)  #division redondeada

# operadores de asignacion
x=23
x+=1    # x=x+1
print(x)
x-=2    # x=x-2
print(x)
x*=3    # x=x*3
print(x)
x/=6    # x=x/6
print(x)
x%=5    # x=x%5
print(x)
x//=3   # x=x//3
print(x)
x=10
x**=2   # x=x**2
print(x)
x=x

#operadores de comparacion
y=5
## igualdad
if y==5:
    print("Son iguales")
## no igual
y+=1
if y!=5:
    print('No son iguales')
# mayor que
if y>2:
    print('y es mayor que 2')
# menor que
if y<10:
    print('y es menor que 10')
# >=  mayor o igual que
# <=  menor o igual que

# operadores logicos
# "and" retorna true si los ambos enunciado son verdaderos
print(5<10 and 2>1)
# "or" retorn true si uno de los enunciados es verdadero
print(5<10 or 2<1)
# "not" invierte el resultado, retorna falso si el resultado es verdadero
print(not(5<10 or 2<1))

# operadores de identidad
# "is" retorna true si ambas variables son el mismo objeto (con la misma locacion de memoria)
# "is not" retorna true si ambas variables no son el mismo objeto