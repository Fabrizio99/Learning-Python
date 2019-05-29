# Funciones
Una función es un bloque de código que se ejecuta una vez que es llamado.
```Python
# Sintaxis
def nombreFuncion():
    bloqueDeCodigo

# Ejemplos
def mensajeHolaMundo():
    print('Hola mundo')
# Si queremos llamar a una función, escribimos su nombre juntos a los paréntesis
mensajeHolaMundo()      # Hola mundo
```
## Parámetro
Es la información que se le puede pasar a una función mediante paréntesis, se puede ingresar cualquier cantidad de parámetros pero separado por comas.
```Python
def mensaje(pais):
print('Soy de '+pais)

mensaje('Peru')         # Soy de Peru
mensaje('Inglaterra')   # Soy de Inglaterra
```