# lista1 = [1,3,5,7]
# tupla1 = tuple(lista1)

# print('tupla1:\t',tupla1)
# print('tupla1[:3]:\t', tupla1[:3])
# print('tupla1[1:]:\t', tupla1[1:])
# print('tupla1[0:1]:\t', tupla1[1:2])
# print('tupla1[1:-1]:\t', tupla1[2:-1])
# print('tupla1[:-1]:\t', tupla1[:-1])
# print('tupla1[:]:\t', tupla1[:])
# print('tupla1[::2]:\t', tupla1[::3])
# print('tupla1[-2]:\t', tupla1[:-2])
# tup2 = (1,"John", tupla1, True, -23.1)

# print('tup2[lol]:\t', tup2[2][:1])
# print('tup2[lol]:\t', tup2[2][1:2])

# lista1 = ['Alvaro', 'Daniel', 'Pilar', 'Beatriz']
# for i in lista1:
#  print(i, end=' ')
# print('')

# alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
# alfabeto2 = (9,2,7,3,5,4)

# alfaL = []
# alfal2 = []

# p=int(input("Teclee un nº porfis: "))

# alfal2 = list(alfabeto)
# alfabeto2 = list(alfabeto2)
# alfabeto2.append(p)
# print(alfabeto2)

# alfalCp = alfabeto2.copy()
# print(alfalCp, "copia alfabeto2")

# alfalCount = alfabeto2.count(99)
# print(alfalCount)

# alfaLDel = alfabeto2.clear();
# print(alfaLDel)

# alfalExtend = alfabeto2.extend(lista1)
# print(alfalExtend, "dsada")

# alfalIndex = alfabeto.index('n')
# print(alfalIndex)

# alfalInsert = alfal2.insert(2,"jjj")
# print(alfal2)

capitales = { 'Argentina' : [("Buenos Aires",42000000)],
        'España' : [("Madrid",50000000)],
        'Uruguay' : [("Provincia de Argentina",30000000)],
        'Brasil' : [("Hijo de Argentina",55000000)]}

nuevas = {"Brasil": [(("Brasilia", 213000000))], "Uruguay": [(("Montevideo", 213000000))]}

for pais, c in capitales.items():
    print(f"Pais {pais} como KEY + capital {c} como valor")

print("\nTodo el diccionario", capitales)

c2 = capitales.copy()
print("\ncopiaaaa",c2)

c3 = c2.get('Argentina')
print("\nyatusaa", c3)

c4 = c2.popitem()
print("\nsisaas",c4)

c5 = c2.setdefault('Brasil', [("Siempre lo será", 213000000)])
print("\nlmao",c5)

c2.update(nuevas)
print("\njejsjdajsdsa", c2)

print("\nITEMS: ", c2.items()) #imprime clave valor

print("\nVALUES: ",c2.values()) #imprime solo valores

print("\nNisu", c2.popitem())

c1 = capitales.clear()
print(capitales)



lolaso = { 'Argentina' : "Buenos Aires",
        'España' : "Madrid",
        'Uruguay' : "Provincia de Argentina",
        'Brasil' : "Hijo de Argentina"}
tupla_dic = {}

for x in lolaso.items():
    l2 = tuple(x)
    print("dsada", l2)