import random
"""Nota: Para hacer el ejercicio más cómodo ya que no hay menú he creado una función para llamar a los ejercicios por sus nombres en el if de aqui abajo."""

"""1. Escribe un código que implemente el siguiente comportamiento: “Si la compra es
superior a 100EUR se aplica un descuento del 5% si se paga al contado, pero si el pago
es con tarjeta sólo se aplica el 2%”. Asegúrate de que el importe de la compra es un
número válido antes de proceder a los cálculos (pista: usa try para comprobar que es
posible convertir la entrada a un float). """

def compras():
    d_compras = {
        "Inferiores a 100" : [],
        "Superiores a 100": [],
        "Pago con tarjeta": [],
        "Pago en efectivo": []
    }

    lista_compras = [150, 30, 75, 12, 310, 222, 10, 100,200,177]

    for x in lista_compras: 
        if x > 100:         
            categoria = "Superiores a 100"
            d_compras[categoria].append(x)
            res = input("Si quiere pagar con tarjeta pulse S, para otra cosa pulse otra tecla:   ")
            if res.lower() == "s":
                dcnto = f"Total Descuento por pago con tarjeta: {x * 0.02} euros del pago de {x}" 
                categoria = "Pago con tarjeta"
                d_compras[categoria].append(dcnto)
            else:
                dcnto = f"Total Descuento por pago en efectivo: {x * 0.05} euros"
                categoria = "Pago en efectivo"
                d_compras[categoria].append(dcnto)
        else:
            categoria = "Inferiores a 100"
            d_compras[categoria].append(x)

    print("Resultados: \n")
    for categoria, l in d_compras.items():
        print(f"{categoria} : {l}")

"""2. Una universidad acaba de modificar su sistema de representación de la calificación
de los alumnos, que como es sabido son valores entre 0 y 10. A partir de ahora, se
calificarán como “A” las notas mayores o iguales a 8,5, “B” las mayores o iguales a 6,5,
“C” las calificaciones mayores o iguales a 5, “D” las calificaciones mayores o iguales a
3,5, y “F” todas las demás. Programa una función que reciba una calificación numérica
y retorne la letra con la nueva calificación. Asegúrate de que la calificación introducida
es válida (idea: programa una función lo suficientemente genérica que se pueda luego
reutilizar en programas que necesiten una validación similar). """

def notas():
    """
    l_notas = []

    if(nota >= 8.5):
        categoria = "A"
    elif(nota >= 6.5):
        categoria = "B"
    elif(nota >= 5):
        categoria = "C"
    elif(nota >= 3.5):
        categoria = "D"
    else:
        categoria = "F"

    l_notas.append(nota)
    
    for l in l_notas:
        print(f"{l}")
        """

    
    d_notas = { #Diccionario de notas
        "A" : [],
        "B" : [],
        "C" : [],
        "D" : [],
        "F" : []
    }
    #Rellenamos el diccionario de notas
    for x in range(1,11):
        p = float(input(f"Dime la {x}ª nota del curso: "))

        if(p >= 8.5):
            categoria = "A"
        elif(p >= 6.5):
            categoria = "B"
        elif(p >= 5):
            categoria = "C"
        elif(p >= 3.5):
            categoria = "D"
        else:
            categoria = "F"
            
        d_notas[categoria].append(p)

    print("Resultados: \n")
    for categoria, n in d_notas.items():
        print(f"{categoria} : {n}")


"""3. Escribe un algoritmo que tras leer tres enteros los escriba en pantalla en orden
creciente. Como siempre, valida las entradas."""

def ordenar():
    numeros = []
    for x in range(1,5):
        while True:
            try:
                n = int(input(f"Dime el {x} número entero: "))
                numeros.append(n)
                break
            except ValueError:
                print("Introduzca un numero entero válido por favor")
    """numeros.sort()
    print("Los numeros ordenados son: ")
    for n in numeros:
        print(n)"""

    for n in range(len(numeros) - 1, 0, -1):
        for i in range(n):
            if(numeros[i]>numeros[i + 1]):
                temp = numeros[i]
                numeros[i] = numeros[i + 1]
                numeros[i + 1] = temp
    print(numeros);


"""4. Codifica un subprograma que reciba un número entero, y si es entre 1 y 12 escriba
un mensaje por pantalla indicando el mes a que dicho número corresponde. En caso
contrario deberá mostrar un mensaje de error. """

def meses():
    meses = [
        "ENERO", "FEBRERO", "MARZO", "ABRIL",
        "MAYO", "JUNIO", "JULIO", "AGOSTO",
        "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"
    ]

    while True:
        try:
            p = int(input("Escriba el nº del mes en el que ha nacido (1 = ENERO ... 12 = DICIEMBRE): "))
            
            if 1 <= p <= 12:
                print(f"El mes es: {meses[p - 1]}")
                break
            else:
                print("El número debe estar entre 1 y 12.")
                
        except ValueError:
            print("Introduzca un número entero válido, por favor.")

"""5. Escribe un programa que, después de preguntar cuántos números se van a
introducir, pida esos números (enteros o reales) y devuelva su media aritmética, el
mayor y el menor. El programa debe controlar que la cantidad de números es mayor de
2 y en caso contrario ha de mostrar un mensaje de error.
"""

def media():
    c = 0
    t = 0
    p = int(input("Cuantos numeros va a introducir?: "))

    for x in range(p):
        while True:
            try:
                res = int(input(f"Introduzca el {x+1} número: "))
                c += res;
                t +=1;
                media = c/t;
                break;
            except ValueError:
                print("Escriba un numero correcto.")
    
    print(f"La media de los numeros es: {media}")

"""6. Escribir una función que sume dos listas de igual longitud y retorne otra lista que
contenga la suma de las originales elemento a elemento. """

def sumaListas():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [6, 5, 4, 3, 2, 1]
    l3 = []

    for i in range(len(l1)):
        suma = l1[i] + l2[i]
        l3.append(suma)
    print(f"La lista con la suma de las dos primeras listas es: {l3}")


import random

# 7. Sumar listas desiguales: los sobrantes se añaden al final
def sumaListasDesiguales():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [6, 5, 4, 3]
    l3 = []
    min_len = min(len(l1), len(l2))

    for i in range(min_len):
        l3.append(l1[i] + l2[i])

    if len(l1) > len(l2):
        l3.extend(l1[min_len:])
    else:
        l3.extend(l2[min_len:])

    print(f"Lista resultante: {l3}")


# 8. Generar dos listas con 20 números: una creciente y otra decreciente
def dosListasOrdenadas():
    nums = [random.randint(1, 100) for _ in range(20)]
    lista_creciente = sorted(nums)
    lista_decreciente = sorted(nums, reverse=True)
    print("Creciente:", lista_creciente)
    print("Decreciente:", lista_decreciente)


# 9. Lista de enteros aleatorios, media, máximo y mínimo
def listaEstadisticas():
    lista = [random.randint(1, 20) for _ in range(10)]
    media = sum(lista) / len(lista)
    print("Lista:", lista)
    print("Media:", round(media, 2))
    print("Máximo:", max(lista))
    print("Mínimo:", min(lista))


# 10. Comprobar si una palabra es palíndromo
def esPalindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    if palabra == palabra[::-1]:
        print("Es un palíndromo ✅")
    else:
        print("No es un palíndromo ❌")


# 11. Poner en mayúsculas la primera letra de cada palabra
def capitalizarFrase(frase):
    print(frase.title())


# 12. Comprobar si dos cadenas son iguales
def cadenasIguales(cad1, cad2):
    print("Son iguales" if cad1 == cad2 else "Son diferentes")


# 13. Comprobar si una palabra contiene todas las vocales
def contieneTodasVocales(palabra):
    palabra = palabra.lower()
    vocales = set("aeiou")
    if vocales.issubset(palabra):
        print("Contiene todas las vocales ✅")
    else:
        print("No contiene todas las vocales ❌")


# 14. Codificar frase según las reglas dadas
def codificarFrase(frase):
    codigos = {"a": "4", "e": "3", "i": "1", "o": "0", "u": "#"}
    frase_codificada = ""
    for letra in frase:
        frase_codificada += codigos.get(letra.lower(), letra)
    print(frase_codificada)


# 15. Leer palabras hasta “fin” y mostrar estadísticas de longitudes
def estadisticaPalabras():
    conteo = [0] * 25
    while True:
        palabra = input("Introduce una palabra (o 'fin' para terminar): ")
        if palabra.lower() == "fin":
            break
        if len(palabra) <= 25:
            conteo[len(palabra) - 1] += 1
    for i, c in enumerate(conteo, start=1):
        print(f"Palabras de longitud {i}: {c}")


# 16. Almacenar información anónima (nº, sexo, edad)
def persona():
    num = int(input("Número de secuencia: "))
    sexo = input("Sexo (M/F): ")
    edad = int(input("Edad: "))
    persona = {"Número": num, "Sexo": sexo, "Edad": edad}
    return persona

def mostrarPersona(p):
    print(f"Número: {p['Número']}, Sexo: {p['Sexo']}, Edad: {p['Edad']}")


# 17 y 18. Estructura Cronología con fechas (nacimiento, matrimonio, deceso)
def cronologia():
    fechas = []
    for evento in ["nacimiento", "matrimonio", "deceso"]:
        dia = int(input(f"Día de {evento}: "))
        mes = int(input(f"Mes de {evento}: "))
        año = int(input(f"Año de {evento}: "))
        fechas.append((dia, mes, año))
    # Comprobar orden lógico
    if fechas[0] <= fechas[1] <= fechas[2]:
        print("Fechas válidas ✅")
    else:
        print("Fechas incorrectas ❌")
    print("Fechas:", fechas)


# 19. Restar cada valor con el siguiente y el último con el primero
def restarArray():
    arr = [int(input(f"Valor {i+1}: ")) for i in range(10)]
    resultado = []
    for i in range(len(arr)):
        siguiente = arr[(i + 1) % len(arr)]
        resultado.append(arr[i] - siguiente)
    print("Resultado:", resultado)


# 20. Calcular gastos de gasolina y tienda para 10 clientes
def gastosGasolinera():
    gas = []
    tienda = []
    total = []
    for i in range(10):
        g = float(input(f"Gasto gasolina cliente {i+1}: "))
        t = float(input(f"Gasto tienda cliente {i+1}: "))
        gas.append(g)
        tienda.append(t)
        total.append(g + t)
    for i in range(10):
        print(f"Cliente {i+1}: total = {total[i]}€")


# 21. Agenda telefónica
def llenarAgenda():
    agenda = {}
    while True:
        nombre = input("Nombre: ")
        if nombre in agenda:
            print("Ese nombre ya existe.")
            continue
        telefono = input("Teléfono: ")
        agenda[nombre] = telefono
        if input("¿Agregar otro? (s/n): ").lower() != "s":
            break
    return agenda

def mostrarAgenda(agenda):
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")


# 22. Recibir diccionario y lista → generar dos listas según estén o no
def separarDiccionario(dic, lista):
    en_dic = []
    no_en_dic = []
    for item in lista:
        if item in dic:
            en_dic.append(dic[item])
        else:
            no_en_dic.append(item)
    print("Valores en el diccionario:", en_dic)
    print("Elementos NO en el diccionario:", no_en_dic)

if __name__ == "__main__":
    print(r"""
         ______   __  __     ______   __  __     ______     __   __
        /\  == \ /\ \_\ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \
        \ \  _-/ \ \____ \  \/_/\ \/ \ \  __ \  \ \ \/\ \  \ \ \-.  \
         \ \_\    \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\"\_ \
          \/_/     \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ \/_/
        """)
    # 🔹 1. Ordenar tres enteros
    # compras()

    # 🔹 2. Calificar notas
    # notas()

    # 🔹 3. Ordenar tres enteros
    # ordenar()

    # 🔹 4. Mostrar mes correspondiente al número
    # meses(5)

    # 🔹 5. Calcular media, mayor y menor
    # media()

    # 🔹 6. Sumar listas iguales
    # sumaListas([1, 2, 3], [4, 5, 6])

    # 🔹 7. Sumar listas desiguales
    # sumaListasDesiguales([1, 2, 3, 4], [10, 20])

    # 🔹 8. Dos listas ordenadas (aleatorias)
    # dosListasOrdenadas()

    # 🔹 9. Media, máximo y mínimo de lista aleatoria
    # listaEstadisticas()

    # 🔹 10. Palíndromo
    # esPalindromo("Anita lava la tina")

    # 🔹 11. Capitalizar frase
    # capitalizarFrase("hola que tal roy")

    # 🔹 12. Cadenas iguales
    # cadenasIguales("hola", "hola")

    # 🔹 13. Contiene todas las vocales
    # contieneTodasVocales("murciélago")

    # 🔹 14. Codificar frase
    # codificarFrase("Un perro del hortelano")

    # 🔹 15. Estadísticas de palabras
    # estadisticaPalabras()

    # 🔹 16. Persona (crea y muestra persona)
    # p = persona(1, "M", 25)
    # mostrarPersona(p)

    # 🔹 17 y 18. Cronología
    # cronologia([(1, 1, 2000), (5, 5, 2020), (1, 1, 2070)])

    # 🔹 19. Restar cada valor con el siguiente
    # restarArray([10, 20, 30, 40])

    # 🔹 20. Gasolinera
    # gastosGasolinera([10, 20, 30], [5, 10, 15])

    # 🔹 21. Agenda
    # agenda = llenarAgenda()
    # mostrarAgenda(agenda)

    # 🔹 22. Diccionario y lista
    # separarDiccionario({"rojo": "color", "perro": "animal"}, ["rojo", "gato", "perro"])