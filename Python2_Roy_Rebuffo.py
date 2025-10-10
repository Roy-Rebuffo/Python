import math;
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
    notas = {a1,a2,a3}#Lista
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

def converterKm(km):
    hm = km * 10
    dm = km * 100
    m = km * 1000
    print("Equivalencia en Hm:", hm)
    print("Equivalencia en Dm:", dm)
    print("Equivalencia en m:", m)
    
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
            case "0":
                print("Seleccione un número válido.\n")

menu()




