#Ejercicio 1
print (type("Alex"))
print (type(333))
print (type(33.33))

#Ejercicio 2
print ("Roy Rebuffo edad: 25")
print ("Roy\nRebuffo\nedad: 25\n")
#Ejercicio 3
lado = float(input("Ingresa la longitud del lado del cuadrado: "))

area = lado **2

print (area)

print (lado)
#Ejercicio 4
def calcular_impuesto(ingresos, nHijos):
    impuesto = ((ingresos - 600) - (60 * nHijos)) / 3
    print(impuesto)
ingresos = float(input("Ingresa tus ingresos: "))
nHijos = float(input("Ingresa cuantos hijos tienes: "))
calcular_impuesto(ingresos, nHijos)
#Ejercicio 5
horaNow= "00:00:00"

totalHoras = 86400

def restante(horaNow):
    h = (int)(horaNow.split(":")[0])
    m = (int)(horaNow.split(":")[1])
    s = (int)(horaNow.split(":")[2])
    tH = h * 3600
    tM = m * 60

    tiempoRestante = totalHoras - (tH + tM + s)
    tiempoPasado = tH + tM + s
    print("El tiempo transcurrido en segundos es: " , tiempoPasado)
    print("Quedan " , tiempoRestante , "segundos para la siguiente medianoche")

horaNow =(input("En que hora del dia estas? : "))
restante(horaNow)
#Ejercicio 6

kmRecorridos = 0
lUsados = 0
costeG = 0
costeM = 0
vehiculos = {}
mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'lenguajes': ['Python', 'JavaScript']}

def calcular (res):
    vehiculos = {'V1':{'kmRecorridos':500, 'lUsados': 15, 'costeG': 1.40, 'costeM': 75}, 
                 'V2':{'kmRecorridos':1000, 'lUsados': 27, 'costeG': 1.32, 'costeM': 150}}

    kmPorLitro = vehiculos[res]['kmRecorridos'] / vehiculos[res]['lUsados'] 
    costeTotal = (vehiculos[res]['costeG']  * kmPorLitro) + vehiculos[res]['costeM'] 

    print(kmPorLitro)
    print(costeTotal)

res =input("Elige tu vehiculo : ")
calcular(res)
#Ejercicio 7
km = float(input("Introduce la longitud en km: "))
hm = km * 10
dm = km * 100
m = km * 1000
print("Equivalencia en Hm:", hm)
print("Equivalencia en Dm:", dm)
print("Equivalencia en m:", m)
#Ejercicio 8
texto_numerico = "45"
print(int(texto_numerico))
print(int(3.99999))
print(float(34))
#Ejercicio 9
lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
area = lado1 * lado2
perimetro = 2 * (lado1 + lado2)

print("Área:", area)
print("Perímetro:", perimetro)
#Ejercicio 10
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))
suma = a + b + c
media = suma / 3
producto = a * b * c

print("Suma:", suma)
print("Media:", media)
print("Producto:", producto)
#Ejercicio 11
tf = float(input("Introduce la temperatura en °F: "))
tc = (tf - 32) * 5 / 9
print("Temperatura en °C:", tc)
#Ejercicio 12
a = 3/2   
b = 3.0 / 2  
c = 3 // 2   
print("a=", a, "b=", b, "c=", c)
#Ejercicio 13
ventas = float(input("Introduce el total de ventas: "))
salario_base = 2000
comision = ventas * 0.03
bruto = salario_base + comision
neto = bruto * (1 - 0.32)

print("Salario neto:", neto)
#Ejercicio 14
euros = float(input("Introduce la cantidad en euros: "))
cambio = float(input("Introduce el tipo de cambio EUR→GBP: "))
gbp_bruto = euros * cambio
comision = gbp_bruto * 0.02
gbp_neto = gbp_bruto - comision

print("Equivalente en GBP:", gbp_neto)
#Ejercicio 15
fruta = "ciruela"
tipo = "claudia"
print(fruta + tipo)   # Une (concatena) las cadenas → "ciruelaclaudia"

print(fruta * 3)      # Repite la cadena 3 veces → "ciruelaciruelaciruela"

