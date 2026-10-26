print("Autor: Eduardo Perez")

def kamehameha():
    print("Goku Concentra su energia")
    print("!Kamehameha")

kamehameha()
kamehameha()
kamehameha()
kamehameha()

def atacar(guerrero):
    print(guerrero,"Realizar un ataque")

atacar("Eduardo")
atacar("Josue")
atacar("Diego")

def calcular_poder(poder,ataque):
    danio = poder * ataque
    return danio

resultado = calcular_poder(4,25)
print("El poder de Eduardo Perez es :", resultado)

resultado = calcular_poder(4,5000)
print("El poder de goku es :", resultado)

def transformar_saiyajin(nombre,poder):
    if poder >=9000:
        print(f"Transformación de {nombre} a superSaiyajing exitosa")
    else:
        print(f"{nombre} Necesita aumentar tu poder")

transformar_saiyajin('Eduardo',500000)
transformar_saiyajin("Josue",25)

nombre_personaje: str = 'Goku'
edad: int =33
altura: float = 1.74
es_activo: bool= True

def multiplicador_poder(entrenamiento: float, edad: int) -> float:
     return entrenamiento * edad


poder: float = multiplicador_poder(15, 5.2)
print("Poder calculado:", poder)