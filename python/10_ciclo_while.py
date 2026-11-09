poder = 2000

while poder < 10000:
    print("Vegueta esta entrenando")
    poder += 2000
print("!Vegueta alcanzo su objetivo")

while poder >0:
    print("Majin Boo tiene", poder,' de poder')
    poder -= 500

print("Majin Boo tiene se quedo sin energia")

print("Continue y break")
dia = 0
while dia <0 :
    dia +=1
    if dia == 4:
        print("Dìa 4: gohan estudia")
        continue
    print("Dia", dia, "Gohan entrena")
    if dia ==8:
        print("Fin del sistema")
        break

for sector in range(1, 11):
    if sector == 3:
        print(f"Sector {sector}: Zona destruida detectada. Se omite el sector.")
        continue
    
    if sector == 7:
        print(f"Sector {sector}: ¡Se ha encontrado a los androides 17 y 18! Búsqueda finalizada.")
        break
    
    print(f"Sector {sector}: Exploración realizada normalmente.")