print("Autor: Eduardo Perez")

def iniciar_conferencia():
    print("Silenciando micrófonos de sala...")
    print("¡Bienvenidos al Congreso Internacional de Tecnología!")

iniciar_conferencia()
iniciar_conferencia()

def registrar_asistente(nombre_asistente):
    print(nombre_asistente, "ha sido acreditado en el evento")

registrar_asistente("Eduardo")
registrar_asistente("Josue")
registrar_asistente("Diego")

def calcular_recaudacion(entradas, precio_unitario):
    total = entradas * precio_unitario
    return total

recaudacion_vip = calcular_recaudacion(4, 25)
print("La recaudación de entradas VIP es:", recaudacion_vip)

recaudacion_general = calcular_recaudacion(50, 15)
print("La recaudación de entradas generales es:", recaudacion_general)

def asignar_auditorio(titulo_charla, inscritos):
    if inscritos >= 150:
        print(f"La charla '{titulo_charla}' pasa al Auditorio Principal")
    else:
        print(f"La charla '{titulo_charla}' se mantiene en Sala Auxiliar")

asignar_auditorio("Inteligencia Artificial en 2026", 220)
asignar_auditorio("Introducción a Git", 45)

nombre_evento: str = "TechSummit Quito"
edicion: int = 4
costo_entrada: float = 35.50
es_presencial: bool = True

def calcular_presupuesto_catering(asistentes: int, costo_por_persona: float) -> float:
    return asistentes * costo_por_persona

presupuesto_total: float = calcular_presupuesto_catering(120, 8.5)
print("Presupuesto calculado de catering:", presupuesto_total)