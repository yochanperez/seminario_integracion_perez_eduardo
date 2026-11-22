print("Autor: Eduardo Perez")

entradas_vendidas = 20

while entradas_vendidas < 100:
    print("Vendiendo lote de entradas... Total actual:", entradas_vendidas)
    entradas_vendidas += 20
print("¡Se alcanzó el aforo mínimo del evento!")

kits_disponibles = 100

while kits_disponibles > 0:
    print("Quedan", kits_disponibles, "kits de bienvenida en recepción")
    kits_disponibles -= 25
print("Se agotaron todos los kits de bienvenida")

print("\nCronograma de montaje (Continue y Break)")
dia = 0
while dia < 10:
    dia += 1
    if dia == 4:
        print("Día 4: Pausa técnica y revisión de sonido (no hay montaje)")
        continue
    print("Día", dia, "- Equipo logístico preparando stands")
    if dia == 8:
        print("Día 8: Todo listo. Fin de la fase de montaje")
        break

print("\nInspección de Stands")
for stand in range(1, 11):
    if stand == 3:
        print(f"Stand {stand}: En mantenimiento eléctrico. Se omite inspección.")
        continue

    if stand == 7:
        print(f"Stand {stand}: ¡Patrocinador principal ubicado! Inspección prioritaria finalizada.")
        break

    print(f"Stand {stand}: Inspección de seguridad aprobada.")