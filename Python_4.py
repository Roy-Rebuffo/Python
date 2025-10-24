import random
print(r"""
 ______   __  __     ______   __  __     ______     __   __
/\  == \ /\ \_\ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \
\ \  _-/ \ \____ \  \/_/\ \/ \ \  __ \  \ \ \/\ \  \ \ \-.  \
 \ \_\    \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\"\_ \
  \/_/     \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ \/_/
""")
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

compras()

"""2. Una universidad acaba de modificar su sistema de representación de la calificación
de los alumnos, que como es sabido son valores entre 0 y 10. A partir de ahora, se
calificarán como “A” las notas mayores o iguales a 8,5, “B” las mayores o iguales a 6,5,
“C” las calificaciones mayores o iguales a 5, “D” las calificaciones mayores o iguales a
3,5, y “F” todas las demás. Programa una función que reciba una calificación numérica
y retorne la letra con la nueva calificación. Asegúrate de que la calificación introducida
es válida (idea: programa una función lo suficientemente genérica que se pueda luego
reutilizar en programas que necesiten una validación similar). """

def notas(nota):
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
        p = float(input(f"Dime la {x} nota del curso"))

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
            
        d_notas[categoria].append(nota)

    print("Resultados: \n")
    for categoria, n in d_notas.items():
        print(f"{categoria} : {n}")

p = float(input("Escriba su nota para averiguar a que categoría pertenece: "))
notas(p);