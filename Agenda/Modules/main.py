import os
"""****************************************************VARIABLES GLOBALES****************************************************"""
ruta_del_script = os.path.dirname(__file__)

ruta_dni = os.path.join(ruta_del_script, "..", "Data", "dni.csv")
ruta_provincias = os.path.join(ruta_del_script, "..", "Data", "provincias.csv")
ruta_agenda = os.path.join(ruta_del_script, "..", "Data", "agenda.csv")
"""**************************************************************************************************************************"""
"""*************************************************LISTADO DE CONTACTOS*****************************************************"""
def listarContactos():
    print("\nLISTADO GENERAL DE CONTACTOS\n")

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                print(f"{datos[1]} {datos[2]} - {datos[0]} - {datos[5]} ({datos[9]})")
    except FileNotFoundError:
        print("No existe la agenda todavía")

def listarContactosPorEstado():
    estado_busqueda = input("Mostrar contactos (ACTIVO / NO ACTIVO): ").upper()

    print(f"\nCONTACTOS {estado_busqueda}\n")

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")
                if datos[9] == estado_busqueda:
                    print(f"{datos[1]} {datos[2]} - {datos[0]} - {datos[5]}")
    except FileNotFoundError:
        print("No existe la agenda todavía")

def listarContactosPorProvincia():
    busqueda = input("Introduzca provincia o código postal (2 primeros dígitos): ")

    print("\nCONTACTOS POR PROVINCIA\n")

    try:
        with open(ruta_agenda, "r", encoding="utf-8") as agenda:
            for linea in agenda:
                datos = linea.strip().split(";")

                provincia = datos[5]
                codigo = datos[4][:2]

                if busqueda.lower() == provincia.lower() or busqueda == codigo:
                    print(f"{datos[1]} {datos[2]} - {provincia} ({datos[4]})")
    except FileNotFoundError:
        print("No existe la agenda todavía")

"""**************************************************************************************************************************"""
"""************************************************INTRODUCCIÓN DE DATOS*****************************************************"""
def introducirContacto():

    while True:
        # ================= DNI =================
        with open(ruta_dni, "r", encoding="utf-8") as f:
            letras_dni = f.readline().strip()

        while True:
            dni = input("Introduzca el DNI (12345678Z): ").upper()

            # Comprobación de formato
            if len(dni) != 9:
                print("Formato de DNI incorrecto")
                continue

            # Separar número y letra
            numero = int(dni[:8])
            letra = dni[8]

            # Comprobar letra
            letra_correcta = letras_dni[numero % 23]

            if letra != letra_correcta:
                print(f"Letra del DNI incorrecta. Debería ser {letra_correcta}")
                continue

            # DNI válido
            print("DNI válido")
            break

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
    contactos = []
    encontrado = False

    #Leer agenda completa
    with open(ruta_agenda, "r", encoding="utf-8") as agenda:
        for linea in agenda:
            datos = linea.strip().split(";")
            contactos.append(datos)

    #Buscar contacto
    for contacto in contactos:
        if contacto[0] == dni_buscar:
            encontrado = True
            print("\nContacto encontrado:")
            print(f"Nombre: {contacto[1]}")
            print(f"Apellidos: {contacto[2]}")
            print(f"Teléfono: {contacto[7]}")
            print(f"Email: {contacto[8]}")

            #Modificar campo
            nuevo_tel = input("Nuevo teléfono (Enter para no cambiar): ")
            if nuevo_tel != "":
                contacto[7] = nuevo_tel

            nuevo_email = input("Nuevo email (Enter para no cambiar): ")
            if nuevo_email != "":
                contacto[8] = nuevo_email

            nuevo_estado = input("¿Activo? (S/N, Enter para no cambiar): ").upper()
            if nuevo_estado == "S":
                contacto[9] = "ACTIVO"
            elif nuevo_estado == "N":
                contacto[9] = "NO ACTIVO"

            break

    if not encontrado:
        print("DNI no encontrado")
        return

    #Reescribir agenda
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

"""******************************************************SISTEMA*************************************************************"""
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

        print("║1 .- Modificar Por Nombre                  ║")

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
"""***************************************************SYSTEM MENU************************************************************"""
def menuSistema():
    print(r"""
   _____     __                
  / __(_)__ / /____ __ _  ___ _
 _\ \/ (_-</ __/ -_)  ' \/ _ `/
/___/_/___/\__/\__/_/_/_/\_,_/ 
                               
          """)
    opcion = -1  # valor inicial

    while opcion != "0":
        print("╔═══════════════════════════════════════════╗")
        print("║             📘 MENÚ SISTEMA               ║")
        print("╠═══════════════════════════════════════════╣")

        print("║1 .- Crear copia de seguridad              ║")
        
        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) VOLVER                               ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nCreando copia de seguridad...\n")
                #copiaSeguridad()
                print("\n\n")
            case "0":
                print("Seleccione un número válido.\n")

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
        print("║4 .- Administración del Sistema            ║")

        print("╠═══════════════════════════════════════════╣")
        print("║ ( 0) SALIR                                ║")
        print("╚═══════════════════════════════════════════╝")

        opcion = input("Teclee la opción que desea realizar: ")

        match opcion:
            case "1":
                print("\n\nEjecutando 'Búsqueda de Contactos'...\n")
                menuBusquedaContactos()
                print("\n\n")
            case "2":
                print("\n\nEjecutando 'Introducción de Datos'...\n")
                menuValidacionDatos()
            case "3":
                print("\n\nEjecutando 'Modificación de datos'...\n")
                menuRelacionFicheros()
            case "4":
                print("\n\nEjecutando 'Administración del sistema'...\n")
                menuSistema()
            case "0":
                print("Seleccione un número válido.\n")

menu()
"""**************************************************************************************************************************"""