print("incluir datos con input")
nombre_asistente = input("¿Cuál es el nombre del asistente? ")
print("Hola", nombre_asistente, "!")
print("Bienvenido al Congreso Internacional de Tecnología")
print("Hasta luego, " + nombre_asistente)

cantidad_pases = int(input("¿Cuántos pases generales desea adquirir? "))
total_pases = cantidad_pases + 2
print("Pases totales asignados (incluyendo cortesías):", total_pases)

print("CONVERSIONES")
print("--- MÓDULO DE FACTURACIÓN Y REGISTRO ---")
nombre_empresa = input("Nombre de la empresa / asistente: ")
precio_entrada = float(input("Precio de la entrada al evento: "))
cantidad_entradas = int(input("Cantidad de entradas: "))
total_facturado = cantidad_entradas * precio_entrada
print("Total a pagar:", total_facturado)
print("Total a pagar (round): ", round(total_facturado, 2))
print(f"Total a pagar (f): ${total_facturado:.2f}")