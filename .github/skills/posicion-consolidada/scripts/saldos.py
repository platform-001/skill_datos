from fastapi import FastAPI

app = FastAPI()

saldos = {
    "Juan Perez": 1500,
    "Maria Lopez": 3200
}

@app.get("/saldo/{nombre}")
def obtener_saldo(nombre: str):
    return {"saldo": saldos.get(nombre, 0)}