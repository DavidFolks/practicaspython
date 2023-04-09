# texto_variado = "Palabra 123 +-*"
# print(type(texto_variado))

# podemos utilizar comillas triples para que el texto se muestre como una cadena escrita
# print(""" 
# Funcionamiento de \
# programa: (opciones)
#     -1 para acceder a opciones
#          -2 para salir
# """)

#################################################################
# Subscripting e indexado

# texto = 'Python'

# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) # Error no podemaos acceder a una posicion que no existe
# print(texto[-7]) # Error no podemaos acceder a una posicion que no existe

# letra = texto [0]
# print(letra)

# # texto[0] = 'p' # Error no podemos modificar una cadena

# letra = 'p'
# print(letra)

# texto_compuesto = letra + texto[2] # concatenacion
# print(texto_compuesto)

##################################################################

#Slicing o substringing
texto = 'python'

# print(texto [0:3])
# print(texto[0:-3])
# # print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1])

# print(texto[::-1])
# print(texto[1:50])
# print(texto[2:2])

###########################################################################
# Cadenas y Formatos

# texto = "Hola mundo! Buenastardes"
# print(texto.lower())
# print(texto.upper())
# print(texto.capitalize())
# print(texto.title())
# print(texto.swapcase())
# texto = texto.upper()
# print(texto)

print('{} + {} = {}'.format(2, 3, 2+3))
print('{} + {} = {}'.format('Hola', 'mundo', 'Hola mundo'))
print('{:.3f} + {:.4f} = {}'.format(2, 3, 2+3))
print('{1} + {0} = {2}'.format(2, 3, 2+3))
print('{2} + {0} = {1}'.format('Hola', 'munado', 'Hola mundo'))
print('{:d} = {:b} = {:o} = {:x}'.format(15, 15, 15, 15))
