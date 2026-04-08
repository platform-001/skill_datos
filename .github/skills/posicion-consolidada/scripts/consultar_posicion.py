"""
consultar_posicion.py
---------------------
Orquestador de la skill 'posicion-consolidada'.
Llama al Servicio 1 (info básica) y al Servicio 2 (saldo)
y devuelve un JSON consolidado a stdout.

Uso:
    python3 consultar_posicion.py <cedula>

Ejemplo:
    python3 consultar_posicion.py 1234567890
"""

import sys
import json
from personas import obtener_persona
from saldos import obtener_saldo


def consultar_info_basica(cedula: str) -> dict:
    persona = obtener_persona(cedula)

    if "error" in persona:
        return {"ok": False, "error": "Cédula no encontrada"}

    return {
        "ok": True,
        "data": {
            "nombre": persona["nombre"],
            "direccion": persona.get("direccion", "No disponible")
        }
    }


def consultar_saldo(nombre_completo: str) -> dict:
    saldo = obtener_saldo(nombre_completo)

    return {
        "ok": True,
        "data": {
            "saldo": saldo["saldo"],
            "moneda": "USD"
        }
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "ok": False,
            "error": "Debes proporcionar un número de cédula. Uso: python3 consultar_posicion.py <cedula>"
        }))
        sys.exit(1)

    cedula = sys.argv[1].strip()

    # ── Paso 1: Consultar información básica ────────────────────────────────
    resultado_info = consultar_info_basica(cedula)
    if not resultado_info["ok"]:
        print(json.dumps({"ok": False, "servicio": "info-basica", "error": resultado_info["error"]}))
        sys.exit(1)

    info = resultado_info["data"]
    nombre_completo = info.get("nombre", "")
    direccion       = info.get("direccion", "No disponible")

    if not nombre_completo:
        print(json.dumps({"ok": False, "servicio": "info-basica", "error": "Cédula no encontrada en el sistema."}))
        sys.exit(1)

    # ── Paso 2: Consultar saldo con el nombre obtenido ──────────────────────
    resultado_saldo = consultar_saldo(nombre_completo)
    if not resultado_saldo["ok"]:
        print(json.dumps({"ok": False, "servicio": "saldos", "error": resultado_saldo["error"]}))
        sys.exit(1)

    saldo_data = resultado_saldo["data"]
    saldo      = saldo_data.get("saldo", 0)
    moneda     = saldo_data.get("moneda", "USD")

    # ── Paso 3: Devolver resultado consolidado ──────────────────────────────
    resultado = {
        "ok": True,
        "cedula":          cedula,
        "nombre":          nombre_completo,
        "direccion":       direccion,
        "saldo":           saldo,
        "moneda":          moneda
    }

    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
