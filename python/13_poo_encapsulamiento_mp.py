print("Autor: Eduardo Perez")

class SalaEvento:
    nombre_sala: str
    __aforo_maximo: int

    def __init__(self, nombre_sala: str, aforo_maximo: int):
        self.nombre_sala = nombre_sala
        self.__aforo_maximo = aforo_maximo

    def mostrar_info(self):
        print("Sala:", self.nombre_sala)
        print("Aforo máximo permitido:", self.__aforo_maximo)
        print("-" * 30)

    def get_aforo_maximo(self) -> int:
        return self.__aforo_maximo

sala_1 = SalaEvento("Auditorio Magna", 500)
sala_2 = SalaEvento("Sala Taller 1", 80)
sala_3 = SalaEvento("Sala VIP Networking", 40)

sala_1.mostrar_info()
sala_2.mostrar_info()
sala_3.mostrar_info()

print("Nombre público:", sala_1.nombre_sala)
print("Aforo obtenido por getter (Sala 2):", sala_2.get_aforo_maximo())