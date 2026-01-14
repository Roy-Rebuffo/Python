import os
"""****************************************************VARIABLES GLOBALES****************************************************"""
ruta_del_script = os.path.dirname(__file__)

ruta_dni = os.path.join(ruta_del_script, "..", "Data", "dni.csv")
ruta_provincias = os.path.join(ruta_del_script, "..", "Data", "provincias.csv")
ruta_agenda = os.path.join(ruta_del_script, "..", "Data", "agenda.csv")
"""**************************************************************************************************************************"""
"""*****************************************************FUNCIONES GLOBALES***************************************************"""
def validarDNI(dni):
    with open(ruta_dni, "r", encoding="utf-8") as f:
        letras_dni = f.readline().strip()

    dni = dni.upper()

    if len(dni) != 9 or not dni[:8].isdigit():
        return False

    numero = int(dni[:8])
    letra = dni[8]

    return letras_dni[numero % 23] == letra
"""**************************************************************************************************************************"""
"""*************************************************LISTADO DE CONTACTOS*****************************************************"""
def mostrarTablaContactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar\n")
        return

    print("╔════════════╦════════════════╦════════════════════╦══════════════════════════╦═══════╦══════════════╦════════════════╦══════════════╦══════════════════════════════╦══════════════╗")
    print("║ DNI        ║ Nombre         ║ Apellidos          ║ Dirección                ║ CP    ║ Provincia    ║ Población      ║ Teléfono     ║ Email                        ║ Estado       ║")
    print("╠════════════╬════════════════╬════════════════════╬══════════════════════════╬═══════╬══════════════╬════════════════╬══════════════╬══════════════════════════════╬══════════════╣")


    for c in contactos:
        print(f"║ {c[0]:<10} ║ {c[1]:<14} ║ {c[2]:<18} ║ {c[3]:<24} ║ {c[4]:<5} ║ {c[5]:<12} ║ {c[6]:<14} ║ {c[7]:<12} ║ {c[8]:<28} ║ {c[9]:<12} ║")

    print("╚════════════╩════════════════╩════════════════════╩══════════════════════════╩═══════╩══════════════╩════════════════╩══════════════╩══════════════════════════════╩══════════════╝")


def listarContactos():
    print("\nLISTADO GENERAL DE CONTACTOS\n")
    contactos = []

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                contactos.append(linea.strip().split(";"))

        mostrarTablaContactos(contactos)

    except FileNotFoundError:
        print("No existe la agenda todavía")

def listarContactosPorEstado():
    estado_busqueda = input("Mostrar contactos (ACTIVO / NO ACTIVO): ").upper()
    contactos = []

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                if datos[9] == estado_busqueda:
                    contactos.append(datos)

        print(f"\nCONTACTOS {estado_busqueda}\n")
        mostrarTablaContactos(contactos)

    except FileNotFoundError:
        print("No existe la agenda todavía")

def listarContactosPorProvincia():
    busqueda = input("Introduzca provincia o código postal (2 primeros dígitos): ")
    contactos = []

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                provincia = datos[5]
                codigo = datos[4][:2]

                if busqueda.lower() == provincia.lower() or busqueda == codigo:
                    contactos.append(datos)

        print("\nCONTACTOS POR PROVINCIA\n")
        mostrarTablaContactos(contactos)

    except FileNotFoundError:
        print("No existe la agenda todavía")

def buscarPorDNI():
    dni = input("Introduzca el DNI a buscar: ").upper()

    if not validarDNI(dni):
        print("DNI no válido\n")
        return

    encontrado = False
    contactos = []

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                if datos[0] == dni:
                    contactos.append(datos)
                    encontrado = True
                    break
    except FileNotFoundError:
        print("No existe la agenda\n")
        return

    if encontrado:
        mostrarTablaContactos(contactos)
    else:
        print("No se encontró ningún contacto con ese DNI\n")

def buscarPorNombreApellido():
    busqueda = input("Introduzca nombre o apellido: ").lower()
    resultados = []

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                nombre = datos[1].lower()
                apellidos = datos[2].lower()

                if busqueda in nombre or busqueda in apellidos:
                    resultados.append(datos)
    except FileNotFoundError:
        print("No existe la agenda\n")
        return

    mostrarTablaContactos(resultados)
"""**************************************************************************************************************************"""
"""************************************************INTRODUCCIÓN DE DATOS*****************************************************"""
def introducirContacto():

    while True:
        # ================= DNI =================
        while True:
            dni = input("Introduzca el DNI (12345678Z): ").upper()

            if validarDNI(dni):
                print("DNI válido")
                break
            else:
                print("DNI incorrecto. Formato o letra no válidos.")

        nombre = input("Introduzca el nombre: ")
        apellidos = input("Introduzca los apellidos: ")
        direccion = input("Introduzca la dirección: ")

        # ================= CÓDIGO POSTAL =================
        while True:
            try:
                cod_postal = input("Introduzca el código postal: ")
                if len(cod_postal) != 5:
                    raise ValueError
                provincia_codigo = cod_postal[:2] #Saco los 2 primeros digitos
                break
            except ValueError:
                print("Código postal inválido")

        # ================= PROVINCIA =================
        provincia = "DESCONOCIDA"
        with open(ruta_provincias, "r", encoding="utf-8") as prov_file:
            for linea in prov_file:
                partes = linea.strip().split(";")
                codigo = partes[0]
                nombre_prov = partes[1]

                if codigo == provincia_codigo:
                    provincia = nombre_prov
                    break

        poblacion = input("Introduzca la población: ")
        telefono = input("Introduzca el teléfono: ")
        email = input("Introduzca el email: ")

        activo = input("¿Contacto activo? (S/N): ").upper()
        estado = "ACTIVO" if activo == "S" else "NO ACTIVO"

        # ================= GUARDAR CONTACTO =================
        with open(ruta_agenda, "a", encoding="utf-8") as agenda:
            agenda.write(
                f"{dni};{nombre};{apellidos};{direccion};{cod_postal};"
                f"{provincia};{poblacion};{telefono};{email};{estado}\n"
            )

        print("Contacto añadido correctamente")

        res = input("¿Desea añadir otro registro? (S/N): ").upper()
        if res != "S":
            break 


"""**************************************************************************************************************************"""
"""************************************************MODIFICACIÓN DE DATOS*****************************************************"""
def modDni():
    dni_buscar = input("Introduzca el DNI del contacto a modificar: ").upper()

    if not validarDNI(dni_buscar):
        print("DNI no válido")
        return

    contactos = []
    encontrado = False

    # ================= LEER AGENDA =================
    with open(ruta_agenda, "r", encoding="utf-8") as agenda:
        for linea in agenda:
            contactos.append(linea.strip().split(";"))

    # ================= BUSCAR CONTACTO =================
    for contacto in contactos:
        if contacto[0] == dni_buscar:
            encontrado = True
            mostrarTablaContactos([contacto])

            nuevo_nombre = input("Nuevo nombre (Enter para no cambiar): ")
            if nuevo_nombre:
                contacto[1] = nuevo_nombre

            nuevos_apellidos = input("Nuevos apellidos (Enter para no cambiar): ")
            if nuevos_apellidos:
                contacto[2] = nuevos_apellidos

            nueva_direccion = input("Nueva dirección (Enter para no cambiar): ")
            if nueva_direccion:
                contacto[3] = nueva_direccion

            nuevo_cp = input("Nuevo código postal (Enter para no cambiar): ")
            if nuevo_cp:
                contacto[4] = nuevo_cp

            nueva_provincia = input("Nueva provincia (Enter para no cambiar): ")
            if nueva_provincia:
                contacto[5] = nueva_provincia

            nueva_poblacion = input("Nueva población (Enter para no cambiar): ")
            if nueva_poblacion:
                contacto[6] = nueva_poblacion

            nuevo_tel = input("Nuevo teléfono (Enter para no cambiar): ")
            if nuevo_tel:
                contacto[7] = nuevo_tel

            nuevo_email = input("Nuevo email (Enter para no cambiar): ")
            if nuevo_email:
                contacto[8] = nuevo_email

            nuevo_estado = input("¿Activo? (S/N) (Enter para no cambiar): ").upper()
            if nuevo_estado == "S":
                contacto[9] = "ACTIVO"
            elif nuevo_estado == "N":
                contacto[9] = "NO ACTIVO"
            break

    if not encontrado:
        print("DNI no encontrado en la agenda")
        return

    # ================= REESCRIBIR AGENDA =================
    with open(ruta_agenda, "w", encoding="utf-8") as agenda:
        for c in contactos:
            agenda.write(";".join(c) + "\n")

    print("Contacto modificado correctamente")

def borrarContacto():
    dni_borrar = input("Introduzca el DNI del contacto a borrar: ").upper()
    contactos = []
    eliminado = False

    with open(ruta_agenda, "r", encoding="utf-8") as agenda:
        for linea in agenda:
            datos = linea.strip().split(";")
            if datos[0] == dni_borrar:
                eliminado = True
            else:
                contactos.append(datos)

    if not eliminado:
        print("DNI no encontrado")
        return

    confirm = input("¿Seguro que desea borrar el contacto? (S/N): ").upper()
    if confirm != "S":
        print("Operación cancelada")
        return

    with open(ruta_agenda, "w", encoding="utf-8") as agenda:
        for c in contactos:
            agenda.write(";".join(c) + "\n")

    print("Contacto eliminado correctamente")
"""**************************************************************************************************************************"""
"""*****************************************************ESTADÍSTICAS*********************************************************"""
def estadisticasGenerales():
    total = 0
    activos = 0
    no_activos = 0
    provincias = {}

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                total += 1

                # Estado
                if datos[9] == "ACTIVO":
                    activos += 1
                else:
                    no_activos += 1

                # Provincias
                prov = datos[5]
                provincias[prov] = provincias.get(prov, 0) + 1

        provincia_top = max(provincias, key=provincias.get)

        print("\nESTADÍSTICAS GENERALES\n")
        print(f"Total de contactos: {total}")
        print(f"Contactos activos: {activos}")
        print(f"Contactos no activos: {no_activos}")
        print(f"Provincia con más contactos: {provincia_top} ({provincias[provincia_top]})\n")

    except FileNotFoundError:
        print("No existe la agenda todavía\n")

def estadisticasPorProvincia():
    provincias = {}

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                prov = datos[5]
                provincias[prov] = provincias.get(prov, 0) + 1

        print("\nCONTACTOS POR PROVINCIA\n")
        for prov, total in provincias.items():
            print(f"{prov}: {total}")

        print()

    except FileNotFoundError:
        print("No existe la agenda todavía\n")

def porcentajeActivos():
    total = 0
    activos = 0

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                total += 1
                if datos[9] == "ACTIVO":
                    activos += 1

        if total == 0:
            print("No hay contactos\n")
            return

        porcentaje = (activos / total) * 100

        print("\nPORCENTAJE DE CONTACTOS ACTIVOS\n")
        print(f"Activos: {porcentaje:.2f}%\n")

    except FileNotFoundError:
        print("No existe la agenda todavía\n")
"""**************************************************************************************************************************"""

"""*******************************************************MENÚS**************************************************************"""
"""**************************************************************************************************************************"""

"""*****************************************************LIST MENU************************************************************"""
def menuBusquedaContactos():
    print(r"""
    __    _      __            __             __                         __             __            
   / /   (_)____/ /_____ _____/ /___     ____/ /__     _________  ____  / /_____ ______/ /_____  _____
  / /   / / ___/ __/ __ `/ __  / __ \   / __  / _ \   / ___/ __ \/ __ \/ __/ __ `/ ___/ __/ __ \/ ___/
 / /___/ (__  ) /_/ /_/ / /_/ / /_/ /  / /_/ /  __/  / /__/ /_/ / / / / /_/ /_/ / /__/ /_/ /_/ (__  ) 
/_____/_/____/\__/\__,_/\__,_/\____/   \__,_/\___/   \___/\____/_/ /_/\__/\__,_/\___/\__/\____/____/  
                                                                                                
          """)
    opcion = -1  # valor inicial

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║             📘 MENÚ LIST                  ║")
        print("╠═══════════════════════════════════════════╣")
        print("║1 .- Listado General de contactos          ║")
        print("║2 .- Listar Actividad de los contactos     ║")
        print("║3 .- Listar Provincias por Código Postal   ║")
        print("║4 .- Listar por DNI                        ║")
        print("║5 .- Listar por Nombre o Apellido          ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) VOLVER                               ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nEjecutando 'Listado de contactos'...\n")
                listarContactos()
                print("\n\n")
            case "2":
                print("\n\nEjecutando 'Actividad de contactos'...\n")
                listarContactosPorEstado()
                print("\n\n")
            case "3":
                print("\n\nEjecutando 'Listar por Código postal/Provincia'...\n")
                listarContactosPorProvincia()
                print("\n\n")
            case "4":
                print("\n\nEjecutando 'Listar por DNI'...\n")
                buscarPorDNI()
                print("\n\n")
            case "5":
                print("\n\nEjecutando 'Listar por Nombre o Apellido'...\n")
                buscarPorNombreApellido()
                print("\n\n")
            case "0":
                print("Seleccione un número válido.\n")
"""**************************************************************************************************************************"""
"""******************************************INSERT MENU*********************************************************************"""
def menuValidacionDatos():
    print(r"""
   ____     __              __             _  __            __      ___       __         
  /  _/__  / /________  ___/ /_ __________(_)/_/ ___    ___/ /__   / _ \___ _/ /____  ___
 _/ // _ \/ __/ __/ _ \/ _  / // / __/ __/ / _ \/ _ \  / _  / -_) / // / _ `/ __/ _ \(_-<
/___/_//_/\__/_/  \___/\_,_/\_,_/\__/\__/_/\___/_//_/  \_,_/\__/ /____/\_,_/\__/\___/___/
                                                                                                                                                                                                                
          """)
    opcion = -1  # valor inicial

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║             📘 MENÚ INSERTS               ║")
        print("╠═══════════════════════════════════════════╣")
        print("║1 .- Introducción de un Contacto           ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) VOLVER                               ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nEjecutando 'Introducir un Contacto'...\n")
                introducirContacto()
                print("\n\n")
            case "0":
                print("Seleccione un número válido.\n")
"""**************************************************************************************************************************"""
"""********************************************MODS MENU*********************************************************************"""
def menuRelacionFicheros():
    print(r"""
   __  ___        ___ ____              _  __         ___       __         
  /  |/  /__  ___/ (_) _(_)______ _____(_)/_/ ___    / _ \___ _/ /____  ___
 / /|_/ / _ \/ _  / / _/ / __/ _ `/ __/ / _ \/ _ \  / // / _ `/ __/ _ \(_-<
/_/  /_/\___/\_,_/_/_//_/\__/\_,_/\__/_/\___/_//_/ /____/\_,_/\__/\___/___/                                
    """)
    opcion = -1  # valor inicial

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║         📘 MENÚ MODS / BORRADO            ║")
        print("╠═══════════════════════════════════════════╣")
        print("║1 .- Modificar Por DNI                     ║")
        print("║2 .- Borrar un Contacto                    ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) VOLVER                               ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nEjecutando 'Modifacar por DNI'...\n")
                modDni()
                print("\n\n")
            case "2":
                print("\n\nEjecutando 'Borrado por DNI'...\n")
                borrarContacto()
                print("\n\n")
            case "0":
                print("Seleccione un número válido.\n")
"""**************************************************************************************************************************"""
"""***************************************************STATS MENU************************************************************"""
def menuEstadisticas():
    print(r"""
  ______  ______  ______   ______  _____    __  ______  ______  __  ______   ______  ______    
 /\  ___\/\  ___\/\__  _\ /\  __ \/\  __-. /\ \/\  ___\/\__  _\/\ \/\  ___\ /\  __ \/\  ___\   
 \ \  __\\ \___  \/_/\ \/ \ \  __ \ \ \/\ \\ \ \ \___  \/_/\ \/\ \ \ \ \____\ \  __ \ \___  \  
  \ \_____\/\_____\ \ \_\  \ \_\ \_\ \____- \ \_\/\_____\ \ \_\ \ \_\ \_____\ \_\ \_\/\_____\ 
   \/_____/\/_____/  \/_/   \/_/\/_/\/____/   \/_/\/_____/  \/_/  \/_/\/_____/\/_/\/_/\/_____/ 
                                                                                               
""")
    
    opcion = -1

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║           📊 MENÚ ESTADÍSTICAS            ║")
        print("╠═══════════════════════════════════════════╣")
        print("║1 .- Estadísticas generales                ║")
        print("║2 .- Contactos por provincia               ║")
        print("║3 .- Porcentaje de contactos activos       ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) VOLVER                               ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                estadisticasGenerales()
            case "2":
                estadisticasPorProvincia()
            case "3":
                porcentajeActivos()
            case "0":
                break
            case _:
                print("Opción no válida\n")


"""**************************************************************************************************************************"""
"""*****************************************************MAIN MENU************************************************************"""
def menu():
    print(r"""
         ______   __  __     ______   __  __     ______     __   __
        /\  == \ /\ \_\ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \
        \ \  _-/ \ \____ \  \/_/\ \/ \ \  __ \  \ \ \/\ \  \ \ \-.  \
         \ \_\    \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\"\_ \
          \/_/     \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ \/_/
        """)

    opcion = -1  # valor inicial

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║             📘 MENÚ PRINCIPAL             ║")
        print("╠═══════════════════════════════════════════╣")

        print("║1 .- Gestión y Búsqueda de Contactos       ║")
        print("║2 .- Introducción de Datos                 ║")
        print("║3 .- Modificación y Borrado de Datos       ║")
        print("║4 .- Estadísticas                          ║")

        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) SALIR                                ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nEjecutando 'Menú de Búsqueda de Contactos'...\n")
                menuBusquedaContactos()
                print("\n\n")
            case "2":
                print("\n\nEjecutando 'Menú de Introducción de Datos'...\n")
                menuValidacionDatos()
            case "3":
                print("\n\nEjecutando 'Menú de Modificación de datos'...\n")
                menuRelacionFicheros()
            case "4":
                print("\n\nEjecutando 'Menú de Estadísticas...\n")
                menuEstadisticas()
            case "0":
                print("Seleccione un número válido.\n")

menu()
"""**************************************************************************************************************************"""