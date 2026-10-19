print("OPERADORES ARITMETICOS - LOGISTICA DE EVENTOS")
print("+ Total asistentes (Sala A + Sala B): ", 50, "+", 50, "=", 50 + 50)
print("- Cupos restantes (Aforo - Registrados): ", 50, "-", 30, "=", 50 - 30)
print("* Total credenciales por bloque: ", 50, "*", 3, "=", 50 * 3)
print("/ Promedio de horas por conferencia: ", 15, "/", 3, "=", 15 / 3)
print("// Mesas completas requeridas: ", 100, "//", 6, "=", 100 // 6)
print("% Asistentes restantes para completar mesa: ", 100, "%", 6, "=", 100 % 6)
print("** Combinaciones de accesos por nivel: ", 2, "**", 3, "=", 2 ** 3)

print("Proyección de ingresos por paquetes de entradas ($50 c/u)")
print(50, "*", 1, "=", 50 * 1)
print(50, "*", 2, "=", 50 * 2)
print(50, "*", 3, "=", 50 * 3)
print(50, "*", 4, "=", 50 * 4)
print(50, "*", 5, "=", 50 * 5)
print(50, "*", 6, "=", 50 * 6)
print(50, "*", 7, "=", 50 * 7)
print(50, "*", 8, "=", 50 * 8)
print(50, "*", 9, "=", 50 * 9)
print(50, "*", 10, "=", 50 * 10)

print("OPERADORES DE COMPARACION - CONTROL DE ACCESO")
print("== Cupo exacto alcanzado : ", 50, "==", 50, 50 == 50)
print("== Cupo exacto alcanzado : ", 50, "==", 40, 50 == 40)
print("!= Modificación en aforo : ", 50, "!=", 40, 50 != 40)
print("!= Modificación en aforo : ", 50, "!=", 50, 50 != 50)
print("> Supera aforo mínimo : ", 100, ">", 80, 100 > 80)
print("> Supera aforo mínimo : ", 100, ">", 180, 100 > 180)
print("< Disponibilidad en sala : ", 100, "<", 180, 100 < 180)
print("< Disponibilidad en sala : ", 100, "<", 180, 100 < 180)
print(">= Cumple aforo reglamentario : ", 100, ">=", 80, 100 >= 80)
print(">= Cumple aforo reglamentario : ", 100, ">=", 180, 100 >= 180)
print("<= Dentro del límite de seguridad : ", 100, "<=", 180, 100 <= 180)
print("<= Dentro del límite de seguridad : ", 100, "<=", 180, 100 <= 180)

print("OPERADORES LOGICOS - VALIDACION DE CONFERENCIAS")
print("Operador and : (50==50) and (40>30)", (50 == 50) and (40 > 30))
print("Operador and : (50==50) and (40>80)", (50 == 50) and (40 > 80))
print("Operador or : (50==50) or (40>80)", (50 == 50) or (40 > 80))
print("Operador or : (50==60) or (40>80)", (50 == 60) or (40 > 80))
print("Operador not : not (50==60)", not (50 == 60))
print("Operador not : not (50==50)", not (50 == 50))

print("Operador not : not (50==50)", not (50 == 50))

tiene_ticket = True
registro_abierto = True

puede_ingresar = tiene_ticket and registro_abierto
print("¿Puede ingresar a la conferencia?", puede_ingresar)

es_ponente_invitado = True
tiene_ticket = False
acceso_sala_vip = es_ponente_invitado or tiene_ticket
print("¿Acceso a sala VIP autorizado?", acceso_sala_vip)