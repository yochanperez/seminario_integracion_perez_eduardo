print("Autor: Eduardo Perez")

for acreditacion in range(1, 6):
    print("Acreditación de asistente Nro.", acreditacion)

for fila in range(1, 11):
    print("Capacidad acumulada:", 5, "*", fila, "=", 5 * fila)

for fila in range(1, 11, 2):
    print("Asientos VIP en fila:", 5, "*", fila, "=", 5 * fila)

print("\nGESTIÓN DE PONENTES DEL EVENTO")
ponentes = [
    {"id": 1, "nombre": "Ana Morales", "charla": "Arquitectura Cloud", "estado": "Confirmado"},
    {"id": 2, "nombre": "Carlos Vega", "charla": "Ciberseguridad Aplicada", "estado": "Confirmado"},
    {"id": 3, "nombre": "Laura Méndez", "charla": "IA Generativa", "estado": "Confirmado"},
]

print("Lista de Ponentes:")
for ponente in ponentes:
    print(f"{ponente['id']} - Nombre: {ponente['nombre']} | Charla: {ponente['charla']}")

salas = ["Auditorio Principal", "Sala Norte", "Sala Innovación"]
for sala in salas:
    print("Sala habilitada:", sala)

aforo_charlas = {
    "DiccionarioKeynote Apertura": 350,
    "Taller Python": 120,
    "Panel DevOps": 180,
    "Mesa Redonda UX": 45
}

for charla, asistentes in aforo_charlas.items():
    if asistentes >= 200:
        print(charla, "requiere el Auditorio Principal")
    else:
        print(charla, "puede realizarse en una sala estándar")

lista_salas = ["Auditorio A", "Sala B", "Sala C", "Sala D", "Sala E"]
for sala in lista_salas:
    print("Cronograma de:", sala)
    for bloque in range(1, 4):
        print("  Bloque horario:", bloque)

print("\nRevisión de disponibilidad (Break y Continue)")
for sala in lista_salas:
    if sala == "Sala D":
        print("Se detiene la revisión en:", sala)
        break
    if sala == "Sala B":
        continue
    print("Sala verificada y lista:", sala)