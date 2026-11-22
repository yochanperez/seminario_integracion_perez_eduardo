class Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre:str,raza:str):
        self.nombre= nombre
        self.raza= raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza", self.raza)

goku = Guerrero("Goku","Saiyajin")
vegeta= Guerrero("Vegetta", "Saiyajin")
eduardo= Guerrero("Eduardo", 'Humano')

vegeta.mostrar_info
eduardo.mostrar_info
goku.mostrar_info