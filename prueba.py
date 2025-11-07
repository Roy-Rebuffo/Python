#Preguntas para examen
"""
QUE PREGUNTE POR TECLADO NOMBRE Y APELLIDO, 
ESCRIBIRLO EN EL FICHERO 
LUEGO LEERLO
"""
#Lectura de ficheros básicas
"""
fich = open('locos.txt','r')

for l in fich:
    print(l)

lEnteros = []

for l in fich:
    lEnteros.append(int(l))
print(lEnteros)

fich.close()
"""
#Uso de with
"""
with open('locos.txt','r+') as fich:
    lEnteros = []
    for l in fich:
        #lEnteros.append(l)
        lEnteros.append(int(l))
print(lEnteros)
"""
"""
try:
    with open('locos.txt','r+') as fich:
        lEnteros = [0]*10 # Línea "artificial" que genera un error de índice en este ejemplo
        for i, linea in enumerate(fich):
            lEnteros[i] = int(linea)
except(FileNotFoundError, IndexError) as error:
    print(error)
else:
    print(lEnteros)
"""

#Otras formas de lectura de ficheros

# Leyendo del fichero "valores_en_columna.txt"  con readlines()

"""
with open('locos.txt', 'r') as fich_ent:
    lista_lineas = fich_ent.readlines()

print("Lista con las líneas del fichero\n{}".format(lista_lineas))
# Transformamos cada una de las líneas en el entero correspondiente
lista_enteros = [int(linea) for linea in lista_lineas]  # Lista por comprensión
print("Lista con los enteros del fichero\n{}".format(lista_enteros))
"""

# Leyendo del fichero "valores_en_columna.txt"  con read()
"""
with open('locos.txt', 'r') as fich_ent:
    lineas_unidas = fich_ent.read()

print("Una única cadena de caracteres correspondiente a todo el fichero\n{}".format(lineas_unidas))
"""

# Leyendo del fichero "valores_en_columna.txt"  con read()
"""
with open('locos.txt', 'r') as fich_ent:
    lineas_unidas = fich_ent.read()

lista_enteros = [int(palabra) for palabra in lineas_unidas.split()]
print("Lista con los enteros del fichero en columna\n{}".format(lista_enteros))
"""

lista = []

try:
    with open('locos.txt', 'w') as fich:
        for i in range(3):
            nom = input('Escriba su nombre: ')
            ape1 = input(f'Escriba el {i+1}er apellido: ')
            ape2 = input(f'Escriba el {i+1}º apellido 2: ')

            registro = f"{nom};{ape1};{ape2}\n"

            fich.write(registro)

            lista.append(registro)

except FileNotFoundError as error:
    print("Error:", error)

else:
    print("Datos guardados correctamente:")
    print(lista)

finally:
    print("Fichero cerrado correctamente.")

    #git remote add origin https://github.com/Roy-Rebuffo/Trabajo-Grupal-Python.git
