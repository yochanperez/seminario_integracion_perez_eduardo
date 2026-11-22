from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv",
            "autor": "Eduardo Perez",
            "version": "0.1.0"}

@router.get("/eduardo")
def endpoint_eduardo() -> Mensaje:
    return {"texto" : "Hola", 
            "campo_interno" : "imprime desde endpoint perez"}

@router.get("/perez", response_model=Mensaje)
def endpoint_perez():
    return {"texto": "Hola", 
            "prioridad": 5, 
            "campo_interno": "no debería salir"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Eduardo", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo",
            "campo_extra" : "no debe salir esto"}
