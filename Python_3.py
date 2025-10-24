import random
print(r"""
 ______   __  __     ______   __  __     ______     __   __
/\  == \ /\ \_\ \   /\__  _\ /\ \_\ \   /\  __ \   /\ "-.\ \
\ \  _-/ \ \____ \  \/_/\ \/ \ \  __ \  \ \ \/\ \  \ \ \-.  \
 \ \_\    \/\_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\"\_ \
  \/_/     \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ \/_/
""")

def generar_temperaturas():
    """Genera una lista de tuplas (día, temp_min, temp_max) para 30 días"""
    temperaturas = []

    for dia in range(1, 31):
        temp_min = random.randint(-10, 25)
        max_posible = min(temp_min + 12, 25)  # No puede superar 25 ni pasar +12
        temp_max = random.randint(temp_min, max_posible)
        temperaturas.append((dia, temp_min, temp_max))

    return temperaturas


def calcular_estadisticas(temperaturas):
    """Calcula medias y el día más frío según la temperatura media"""
    suma_min = sum(temp_min for _, temp_min, _ in temperaturas)
    suma_max = sum(temp_max for _, _, temp_max in temperaturas)

    media_min = suma_min / len(temperaturas)
    media_max = suma_max / len(temperaturas)

    # Calcular temperatura media diaria
    medias_dia = [(dia, (temp_min + temp_max) / 2) for dia, temp_min, temp_max in temperaturas]
    dia_mas_frio, temp_media_minima = min(medias_dia, key=lambda x: x[1])

    return media_min, media_max, dia_mas_frio, temp_media_minima


def mostrar_resultados(temperaturas, media_min, media_max, dia_frio, temp_frio):
    print("📅 Temperaturas de los 30 días:\n")
    for dia, tmin, tmax in temperaturas:
        print(f"Día {dia:2d}: Mín = {tmin:>3}°C | Máx = {tmax:>3}°C | Media = {(tmin + tmax)/2:>5.1f}°C")

    print("\n📊 Estadísticas:")
    print(f"Temperatura media de las mínimas: {media_min:.2f}°C")
    print(f"Temperatura media de las máximas: {media_max:.2f}°C")
    print(f"El día más frío fue el día {dia_frio} con una temperatura media de {temp_frio:.2f}°C")


# --- Programa principal ---
temperaturas = generar_temperaturas()
media_min, media_max, dia_frio, temp_frio = calcular_estadisticas(temperaturas)
mostrar_resultados(temperaturas, media_min, media_max, dia_frio, temp_frio)
