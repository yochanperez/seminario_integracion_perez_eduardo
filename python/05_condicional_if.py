print("Condicional If")
print("Condicional Simple")
dinero = 10
if dinero >= 5:
    print("Homero puede comprar rosquillas")

print("Programa finalizó")


creditos = float(input("Cantidad de creditos disponibles"))
precio_respuesto = float (input("Precio respuesto"))

if (creditos >= precio_respuesto):
    print("Compra Autorizada")
else:
    print("Creditos insuficientes")
    print("Buscar solucion o trueque")

print("Condicional if - elif -else ")
print("Condicional Condiciones multiples")
combustible = float(input("combustible de la nave"))

if (combustible>=75):
    print("Optimo")
elif(combustible>=50):
    print("suficiente")
elif(combustible>=20):
    print("Bajo")
else:
    print("Critico")
    print("Localiza base mas cercana")

print("Condicional CONDICIONES ANINADAS")
piloto = input("Nombre del Piloto")
motor_funciona = input("El motor funciona (SI/NO)")
combustible = input("Combustible disponible")

if (motor_funciona=="SI"):
    print("Motor Verificado")
    if combustible>=50:
        print("Combustible suficiente")
        print("Participación Autorizada")
    else:
        print("Debe recargar combustible")
else:
    print("No puede participar")
    print("El motor necesita reparación")                           