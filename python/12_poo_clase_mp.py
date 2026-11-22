print("Autor: Eduardo Perez")

class Conferencia:
    titulo: str
    ponente: str

    def __init__(self, titulo: str, ponente: str):
        self.titulo = titulo
        self.ponente = ponente

    def mostrar_info(self):
        print("Conferencia:", self.titulo)
        print("Ponente:", self.ponente)
        print("-" * 30)

conf_1 = Conferencia("Desarrollo Backend con Python", "Eduardo Pérez")
conf_2 = Conferencia("Seguridad en Redes Empresariales", "Josué Ruiz")
conf_3 = Conferencia("Arquitectura de Microservicios", "Ana Morales")

conf_1.mostrar_info()
conf_2.mostrar_info()
conf_3.mostrar_info()