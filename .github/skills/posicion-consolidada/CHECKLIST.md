# Checklist de calidad — Skill: Posición Consolidada

## Antes de usar
- [ ] Servicio 1 corriendo: `python3 scripts/personas.py`
- [ ] Servicio 2 corriendo: `python3 scripts/saldos.py`
- [ ] Dependencia instalada: `pip install requests`

## Validación de la respuesta
- [ ] El número de cédula se extrajo correctamente del mensaje.
- [ ] El Servicio 1 respondió con nombre y dirección.
- [ ] El Servicio 2 respondió con saldo en USD.
- [ ] La respuesta final está en español y formato amigable.
- [ ] Si hubo error, se informa qué servicio falló y por qué.
- [ ] No se inventaron datos ante fallas.
