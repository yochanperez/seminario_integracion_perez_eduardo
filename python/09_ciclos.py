for flexion in range(1,6):
    print("Goku hace la flexion", flexion)

for numero in range(1,11):
    print("Multiplicacion ", 5,"*", numero,"=",5*numero)

for numero in range(1,11,2):
    print("Multiplicacion ", 5,"*", numero,"=",5*numero)

print("CRUD DE LISTAS EN PYTHON")
Avengers = [
    {"id": 1,"nombre":"Tony Stark", "heroe":"Iron Man", "estado":"Activo"},
    {"id": 2,"nombre":"Steve Rogers", "heroe":"Capitan America", "estado":"Activo"},
    {"id": 3,"nombre":"Thor Odison", "heroe":"Thor", "estado":"Activo"},
]

print("Lista de Avengers")
for avenger in Avengers:
    print(f"{avenger["id"]} - nombre : {avenger["nombre"]}")

nombres = ["Pedro", "Pablo" , "Juan"]

for nombre in nombres:
    print("Nombre Actual: ", nombre)

guerreros = {
    "Goku": 9500,
    "Vegetta": 6000,
    "Gohan": 6000,
    "Piccolo": 4500
}

for nombre, poder in guerreros.items():
    if poder >= 9000:
        print(nombre,"puede enfrentar a Freezer")
    else:
        print(nombre,"necesita entrenar mas")

guerreros = ["Goku", "Vegeta", "Gohan", "Piccolo", "Majinbu"]
for guerrero in guerreros:
    print ("Turno de: ", guerrero)
    for ronda in range (1,4):
        print ("Ronda: ", ronda)

print ("Break y Continue")
for guerrero in guerreros:
    if (guerrero == "Piccolo"):
        break
    if (guerrero == "Vegeta"):
        continue
    print ("Guerrero", guerrero)