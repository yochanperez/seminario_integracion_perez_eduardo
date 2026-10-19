naves= ["N-1", "Transporte", "Naboo"]
print("Naves ", naves)
print("tipo: ", type(naves))
print("Tuplas")
coordenadas=(15,30,45)
print("coordenadas: ", coordenadas)
print("tipo: ", type(naves))
print("Diccionario")
droide = {
    "modelo": "R2-D2",
    "tipo": "Astromecanico",
    "activo": True
}
print("droide: ", coordenadas)
print("tipo: ", type(naves))
print("Conjunto")
planetas = {
    "Naboo",
    "Kmino",
    "Alderan"
}
print("planetas: ", planetas)
print("tipo: ", type(planetas))

print("CRUD DE LISTAS EN PYTHON")
Avengers = [
    {"id": 1,"nombre":"Tony Stark", "heroe":"Iron Man", "estado":"Activo"},
    {"id": 2,"nombre":"Steve Rogers", "heroe":"Capitan America", "estado":"Activo"},
    {"id": 3,"nombre":"Thor Odison", "heroe":"Thor", "estado":"Activo"},
]

id_publico =4
def create():
    id= 4
    print("Reclutar Avengers")
    nombre=input("Nomber Heroe:")
    heroe=input("Heroe: ")
    estado= input("Estado (Activo, Retirado, Desaparecido)")
    nuevo_avengers = {
        "id": id,
        "nombre":nombre,
        "heroe":heroe,
        "estado":estado
    }

    Avengers.append(nuevo_avengers)