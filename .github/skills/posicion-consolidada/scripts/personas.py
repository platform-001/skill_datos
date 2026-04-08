from fastapi import FastAPI

app = FastAPI()

personas = {
    "123": {"nombre": "Juan Perez", "edad": 30, "direccion": "Calle 123"},
    "456": {"nombre": "Maria Lopez", "edad": 25, "direccion": "Avenida 456"}
}

@app.get("/persona/{id}")
def obtener_persona(id: str):
    return personas.get(id, {"error": "No encontrado"})