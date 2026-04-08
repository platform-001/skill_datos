# Skill: Consulta de Posición Consolidada

## Propósito
Consultar la posición consolidada de un cliente a partir de su número de identificación (cédula).
Orquesta dos servicios locales: uno de información básica y otro de consulta de saldos.

## Cuándo usar esta skill
Usa esta skill cuando el usuario pregunte algo como:
- "¿Puedes darme la posición consolidada del número [cédula]?"
- "Consulta la posición de la identificación [número]"
- "¿Qué saldo tiene el cliente con cédula [número]?"

## Entradas esperadas
- Número de identificación del cliente (cédula), proporcionado por el usuario en el chat.

## Salida esperada
Un resumen consolidado con:
- Nombre completo del cliente
- Dirección / lugar de residencia
- Saldo disponible en USD

## Instrucciones de ejecución para el agente

1. Extraer el número de identificación del mensaje del usuario.
2. Ejecutar el script orquestador `scripts/consultar_posicion.py` pasando la cédula como argumento.
3. El script internamente:
   - Llama al **Servicio 1** (`/info-basica?cedula=<número>`) → devuelve nombre y dirección.
   - Llama al **Servicio 2** (`/saldo?nombre=<nombre_completo>`) → devuelve saldo en USD.
4. Recibir el JSON consolidado del script y presentarlo al usuario en lenguaje natural.

## Reglas de formato de respuesta
- Responder siempre en español.
- Presentar los datos en formato claro y legible (no JSON crudo).
- Ejemplo de respuesta esperada:

```
📋 Posición Consolidada

Nombre:     Maria García
Cedula:     12345679
Dirección:  Vive en La Carolina
Saldo:      USD 1,000.00
```

## Criterio de calidad mínimo
- El número de identificación debe extraerse correctamente del mensaje.
- Ambos servicios deben responder antes de mostrar el resultado.
- Si algún servicio falla, informar al usuario cuál falló y con qué error.
- No inventar datos si un servicio no responde.

## Mensaje sugerido para invocar en Copilot Chat
"Aplica la skill posicion-consolidada: consulta la posición del número de identificación [CÉDULA]."
