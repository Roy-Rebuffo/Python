import math;
print(r"""
 ______   __  __     ______   __  __     ______     __   __
/\  == \ /\ \_\ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \
\ \  _-/ \ \____ \  \/_/\ \/ \ \  __ \  \ \ \/\ \  \ \ \-.  \
 \ \_\    \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\"\_ \
  \/_/     \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ \/_/
""")


""" 1. Implementa una función “fuerza” que retorne el valor de la fuerza en función de
los valores de masa y aceleración recibidos como parámetros. Implementa,
posteriormente, un programa probador que, leyendo de teclado los valores
necesarios, invoque a la función “fuerza” y muestre por pantalla el valor de la
fuerza a partir de una masa y aceleración dadas. """

def fuerza (masa,aceleracion):
    fuerza = (masa * aceleracion)
    print("\nLa fuerza es:" ,fuerza)

"""2. Implementa un programa modularizado que, leyendo de teclado los valores
necesarios, muestre en pantalla el área de un círculo, un cuadrado y un triángulo.
Utiliza el valor 3.1416 como aproximación de П (pi) o importa el valor del módulo
“math”. """

def area(radio, lado, base, altura):
    pi = round(math.pi, 4) #4 decimales para el pi
    circulo = pi * math.pow(radio,2)
    cuadrado = lado * lado
    triangulo = (base * altura) / 2
    print ("\nEl area del circulo es: ", circulo)
    print ("\nEl area del cuadrado es: ", cuadrado)
    print ("\nEl area del triangulo es: ", triangulo)

""" 3. El Barn (también llamado a veces granero) es una unidad de superficie,
equivalente a 10-28 m². Un Barn es, aproximadamente, el área de la sección
transversal del núcleo de un átomo de uranio, por lo que son muy utilizados en
física de partículas para medir las secciones en reacciones nucleares. Programa dos
funciones, una que permita convertir unidades en m² a Barns, y su inversa. """

def metroAbarns():
    metros = float(input("Introduzca unidades en metros"))
    #convertor = metros * math.pow(metros,-28) OTRA FORMA DE HACERLO. SE VE EL EXPONENCIAL NEGATIVO
    convertor = metros *(metros**-28)
    print (convertor)

def barnsAmetros():
    barns = float(input("Introduzca unidades en barns"))
    convertor = barns * (barns ** 28)
    print (convertor)
""" 4. Implementa un programa modularizado que, leyendo la nota obtenida por tres
alumnos en una asignatura, muestre por pantalla la media de las notas. """
def media(a1,a2,a3):
    notas = {a1,a2,a3}#Diccionario
    cont = 0
    acum = 0

    for n in notas:
        cont += 1       
        acum += n

    total = acum / cont
    print("\nLa media es: ", total)

""" 5. La Tasa de Interés Efectivo Anual (TIEA) se calcula a partir de una tasa nominal
anual (TNA) y de un determinado número entero de períodos de capitalización (m)
de la tasa nominal anual en el año: TIEA=(1 + TNA/n)n-1, siendo n el número de
periodos total de un año, es decir, 12 si hablamos de períodos mensuales. Escribe
una función que calcule el TIEA a partir del TNA y el número de períodos (4 si es
trimestral, 2 si es semestral, etc.). """

def tasaInteres():
    TNA = int(input("Introduzca el TNA"))
    periodo = input("Introduzca el periodo del año (1) Semestre | (2)Trimestre |(3)Bimestre | (4)Mensual: ")
    if(periodo == "1"):
        TIEA = (1 + TNA/2)
        print("La Tasa de Interés Efectivo Anual Semestral es:", TIEA)
    elif(periodo == "2"):
        TIEA = (1 + TNA/4)
        print("La Tasa de Interés Efectivo Anual Trimestral es:", TIEA)
    elif(periodo == "3"):
        TIEA = (1 + TNA/6)
        print("La Tasa de Interés Efectivo Anual Bimestral es:", TIEA)
    else:
        TIEA = (1 + TNA/12)
        print("La Tasa de Interés Efectivo Anual Mensual es:", TIEA)

""" 6. Define una función que convierta radianes en grados (recuerda que 360 grados
son 2П radianes.) """
def converterRadianes():
    pi = round(math.pi, 4)
    rad = int(input("Introduzca los radianes: "))
    converter = (2*pi*rad) / 360
    print("Radianes a grados =",converter,"º")

""" 7. Escribe un programa modularizado que solicite al usuario una hora en formato
[hora, minutos y segundos] y utilizando una función que calcule el número total de
segundos transcurridos desde la última medianoche, lo muestre posteriormente por
pantalla. """

def totalSegundos(horaNow):
    totalHoras = 86400

    h = (int)(horaNow.split(":")[0])
    m = (int)(horaNow.split(":")[1])
    s = (int)(horaNow.split(":")[2])
    tH = h * 3600
    tM = m * 60

    tiempoTranscurrido = tH + tM + s
    print("El tiempo transcurrido en segundos es: " , tiempoTranscurrido)
""". Escribe un programa que lea una longitud en kilómetros y muestre su 
equivalencia en Hm, Dm y m utilizando una función para cada cálculo.   """
def converterKm(km):
    hm = km * 10
    dm = km * 100
    m = km * 1000
    print("Equivalencia en Hm:", hm)
    print("Equivalencia en Dm:", dm)
    print("Equivalencia en m:", m)

""" Escribe una función que determine si un punto de coordenadas en 2D está o no 
sobre la circunferencia x2+y2=1000.  """
def dimensiones():

    d_dimensiones = {# Diccionario
        "dentro": [],#claves
        "sobre": [],
        "fuera": []
    }
    lista_puntos = [(30, 10), (20, 20), (35, 0), (0, 32), (5, 28)] #valores

    for (x, y) in lista_puntos:
        calc = x ** 2 + y ** 2

        if calc == 1000:
            print("El punto de coordenadas está sobre la circunferencia")
            categoria = "sobre"
        elif calc < 1000:
            categoria = "dentro"
        else:
            categoria = "fuera"

        d_dimensiones[categoria].append((x, y)) #añado los valores

    print("Resultados de clasificación:")
    for categoria, lista in d_dimensiones.items(): #.items devuelve la clave y valor
        print(f"{categoria}: {lista}") #Clave(categoria), valor (lista)

"""  El antiguo sistema anglosajón de unidades sigue en vigor en muchos lugares y 
su uso es frecuente en algunos contextos. Programa una función que determine el 
número de pintas que contiene una cierta cantidad de líquido expresada en 
mililitros, sabiendo que 1 pinta (pt) = 473,176473 ml.   """
def pinta(ml):
    pinta = ml / 473.176473
    print(f"{ml} ml equivalen a {pinta:.4f} pintas.")

""" Escribe un programa que muestre por pantalla la tabla de multiplicar de un 
número dado invocando para ello una función a la que le pasará dicho número. 
Utilice el siguiente formato (ejemplo para la tabla del 1):  """
def t_mult(n):
    print(f"La tabla de multiplicar del {n} es: \n")
    for i in range(1, 11):
        res = i * n
        print(f"{i} * {n} =", res)
""" La temperatura expresada en grados centígrados TC, se puede convertir a 
grados Fahrenheit (TF) mediante la siguiente fórmula: TF = 9*TC/5 + 32. 
Igualmente, es sabido que −273,15 °C corresponden con el 0 Kelvin. Escribe una 
función devuelva la temperatura en grados Farenheit y otra en Kelvin a partir de la 
temperatura en grados centígrados. Escribe un programa para probarlas que pida al 
usuario una temperatura en grados centígrados.  """
def grados(res):
    g_f = ((9 * res) / 5) + 32
    g_k = 273.15 + res;
    print (f"La temperatura grados Fahrenheit (TF) es : {g_f}")
    print (f"La temperatura grados Kelvin (TK) es : {g_k}")
    
""" Escribe una función que a partir de las coordenadas 3D de dos puntos en el 
espacio en formato (x, y, z) calcule la distancia que hay entre dichos puntos. 
Prueba su función y el resultado por pantalla.   """

def distancia(x1,y1,z1,x2,y2,z2):
    p1 = x1,y1,z1
    p2 = x2,y2,z2

    dis = math.sqrt((x2 - x1)**2  + (y2 - y1)**2 + (z2-z1)**2)
    print(f"La distancia entre {p1} y {p2} es: {dis:.4f}")

"""Un número complejo es un número de la forma a+bi, donde a y b son números 
reales y el valor de i es √−1 . Las cuatro operaciones aritméticas básicas sobre 
números complejos se definen como:  
 Suma: (a+bi)+(c+di)=(a+c)+(b+d)i  
 Resta: (a+bi)-(c+di)=(a-c)+(b-d)i  
 Producto: (a+bi)*(c+di)=(ac-bd)+(ad+bc)i  
 División: (a+bi)/(c+di) = ((ac+bd)/(c2+d2)) + ((bc-ad)/(c2+d2))i, 
suponiendo c2+d2<>0
Programa funciones, para cada una de las operaciones descritas, y posteriormente, 
realiza un programa probador que lea dos números complejos y muestre por 
pantalla el resultado de las operaciones reseñadas.  """
def suma_complejos(p1, p2):
    """Suma dos números complejos p1 + p2"""
    a, b = p1
    c, d = p2
    return (a + c, b + d)

def resta_complejos(p1, p2):
    """Resta dos números complejos p1 - p2"""
    a, b = p1
    c, d = p2
    return (a - c, b - d)

def producto_complejos(p1, p2):
    """Producto de dos números complejos p1 * p2"""
    a, b = p1
    c, d = p2
    return (a * c - b * d, a * d + b * c)

def division_complejos(p1, p2):
    """División de dos números complejos p1 / p2"""
    a, b = p1
    c, d = p2
    if c == 0 and d == 0:
        raise ValueError("No se puede dividir por cero.")
    divisor = c**2 + d**2
    return ((a * c + b * d) / divisor, (b * c - a * d) / divisor)

def mostrar_complejo(p):
    """Muestra un número complejo en formato a + bi"""
    x, y = p
    if y >= 0:
        return f"{x:.4f} + {y:.4f}i"
    else:
        return f"{x:.4f} - {abs(y):.4f}i"
    
def numerosComplejos(c1,c2):

    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
""" Un año es bisiesto si es divisible por 400 o si lo es por 4 pero no por 100. 
Programa una función que reciba un año y decida si es o no bisiesto. """

def bisiesto(a):
    return (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
def menu():
    #valorar opcion de hacer un for in range
    opcion = -1  # valor inicial

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║             📘 MENÚ PRINCIPAL             ║")
        print("╠═══════════════════════════════════════════╣")

        for i in range(1, 16):
            print(f"║ ({i:>2}) Ejercicio {i:<27}║")

        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) SALIR                                ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nEjecutando ejercicio 1...\n")
                masa = float(input("Introduzca la masa: "))
                aceleracion = float (input("Introduzca la aceleracion: "))
                fuerza(masa,aceleracion)
                print("\n\n")
            case "2":
                print("\n\nEjecutando ejercicio 2...\n")
                radio = int(input("Introduzca radio del circulo: "))
                lado = int(input("Introduzca el lado del cuadrado"))
                base = int(input("Introduzca la base"))
                altura = int(input("Introduzca la altura del triangulo"))
                area(radio,lado,base,altura)
                print("\n\n")
            case "3":
                print("\n\nEjecutando ejercicio 3...\n")
                res = input("Metros a barns (1) | Barns a metros (2): ")
                if res == "1":
                    metroAbarns()
                elif res == "2":
                    barnsAmetros()
                else:
                    print("Opción no válida.\n")
                print("\n\n")
            case "4":
                print("\n\nEjecutando ejercicio 4...\n")
                a1 = int(input("Introduzca la nota del primer alumno: "))
                a2 = int(input("Introduzca la nota del segundo alumno: "))
                a3 = int(input("Introduzca la nota del tercer alumno: "))
                media(a1,a2,a3)
                print("\n\n")
            case "5":
                print("\n\nEjecutando ejercicio 5...\n")
                tasaInteres()
            case "6":
                print("\n\nEjecutando ejercicio 6...\n")
                converterRadianes()
            case "7":
                print("\n\nEjecutando ejercicio 7...\n")
                horaNow =(input("En que hora del dia estas?(en formato 00:00:00): "))
                totalSegundos(horaNow)
            case "8":
                print("\n\nEjecutando ejercicio 8...\n")
                km = float(input("Introduce la longitud en km: "))
                converterKm(km)
            case "9":
                print("\n\nEjecutando ejercicio 9...\n")
                dimensiones()
                print("\n\n")
            case "10":
                print("\n\nEjecutando ejercicio 10...\n")
                res = int(input("Escriba el valor del liquido"))
                pinta(res)
            case "11":
                print("\n\nEjecutando ejercicio 11...\n")
                res = int(input("Escriba un numero para averiguar su tabla de multiplicar"))
                t_mult(res)
            case "12":
                print("\n\nEjecutando ejercicio 12...\n")
                res = int(input("Escriba la temperatura en ºC: "))
                grados(res)
            case "13":
                print("\n\nEjecutando ejercicio 13...\n")
                x1 = int(input("Escriba la coordenada x del punto 1: "))
                y1 = int(input("Escriba la coordenada y del punto 1: "))
                z1 = int(input("Escriba la coordenada z del punto 1: "))

                x2 = int(input("Escriba la coordenada x del punto 2: "))
                y2 = int(input("Escriba la coordenada y del punto 2: "))
                z2 = int(input("Escriba la coordenada z del punto 2: "))
                distancia(x1,y1,z1,x2,y2,z2)
            case "14":
                print("\n\nEjecutando ejercicio 13...\n")
                comp1 = complex(input("Indtroduzca el primer numero complejo(ej. 2+3j): "))
                comp2 = complex(input("Indtroduzca el segundo numero complejo(ej. 2+3j): "))
                numerosComplejos(comp1,comp2);
                
            case "15":
                print("\n\nEjecutando ejercicio 13...\n")
                print("Introduce el año para saber si es bisiesto:")
                a = int(input("a : "))
                print("Bisiesto" if bisiesto(a) else "No es bisiesto") #Lo mas parecido a un ternario en Java
            case "0":
                print("Seleccione un número válido.\n")

menu()




