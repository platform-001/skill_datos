# Skill: Consulta de Posición Consolidada

Consulta la posición financiera de un cliente a partir de su cédula,
orquestando dos servicios locales en Python.

## Flujo de uso en GitHub Copilot (VS Code)

1. Abre dos terminales y levanta los servicios:
   ```bash
   # Terminal 1
   python3 .github/skills/posicion-consolidada/scripts/personas.py

   # Terminal 2
   python3 .github/skills/posicion-consolidada/scripts/saldos.py
   ```

2. Abre Copilot Chat y escribe:
   ```
   Aplica la skill posicion-consolidada: consulta la posición del número de identificación 1234567890
   ```

3. Copilot ejecutará el script orquestador y te mostrará el resultado consolidado.

## Archivos de la skill
- `SKILL.md` — instrucciones principales del agente.
- `skill.config.json` — metadatos y configuración.
- `prompts/generacion.md` — prompt base para Copilot.
- `scripts/consultar_posicion.py` — orquestador que llama los dos servicios.
- `scripts/personas.py` — Servicio 1: cédula → nombre y dirección.
- `scripts/saldos.py` — Servicio 2: nombre → saldo en USD.
- `examples/` — entrada y salida de referencia.
- `CHECKLIST.md` — verificación rápida antes de usar.

## Dependencias
```bash
pip install requests
```

## Personalización
- Edita `CLIENTES` en `personas.py` para agregar tus datos reales.
- Edita `SALDOS` en `saldos.py` para agregar tus saldos reales.

