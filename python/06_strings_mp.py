nombre1 = "Ponente"
print(f"Tipo de datos: {type(nombre1)}")
nombre2 = "Dra. Elena Rostova"
print(f"Conferencista 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

print("Funciones comunes de texto")
sala_1 = "Auditorio-A"
sala_2 = "Salon-B2"
longitud_sala_1 = len(sala_1)
longitud_sala_2 = len(sala_2)
print("nombre sala 1", sala_1)
print("longitud sala 1", longitud_sala_1)
print("nombre sala 2", sala_2)
print("longitud sala 2", longitud_sala_2)

print("Convertir Mayusculas y minúsculas")
mensaje = "El comité confirma la apertura del Congreso Tech"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje Original", mensaje)
print("Mensaje en Mayuscula", mensaje_mayuscula)
print("Mensaje en Minuscula", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "La ponencia se trasladará a la Sala Virtual"
nuevo_mensaje = mensaje.replace("Sala Virtual", "Auditorio Principal")
print("Mensaje Original", mensaje)
print("Mensaje Modificado", nuevo_mensaje)

print("Separacion de Cadenas")
sedes = "Quito,Guayaquil,Cuenca"
print("sedes: ", sedes)
lista_sedes = sedes.split(",")
print(lista_sedes)
print("Primera sede : ", lista_sedes[0])

print("Extraer subcadenas")
mensaje = "Registro oficial de ponencias del congreso"
subcadena_1 = mensaje[0:8]
subcadena_2 = mensaje[20:29]
print("subcadena 1 es : ", subcadena_1)
print("subcadena 2 es : ", subcadena_2)

print("Comprobaciones útiles")
codigo_ticket = "TK2026"
numero_aforo = "350"
institucion = "UniversidadUTE"
identificador_sala = "SALA01"

print(codigo_ticket.isalnum())
print(numero_aforo.isdigit())
print(institucion.isalpha())
print(identificador_sala.isalnum())
print(identificador_sala.isdigit())