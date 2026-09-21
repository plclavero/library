# Plan de implementación - Biblioteca Barrial

## Arquitectura

- `tp_integrador_01_biblioteca.py`: entidades de dominio, reglas, funciones de operación y menú.
- `test_tp_integrador_01_biblioteca.py`: pruebas automatizadas con `unittest`.
- `TP-Integrador-01-RFC-Biblioteca.md`: especificación funcional, flujos y trazabilidad.

## Flujo de datos

1. El menú recibe entradas de consola.
2. Las funciones validan y crean o modifican objetos en listas de memoria.
3. `Prestamo` modifica la disponibilidad de `Libro` y calcula su estado.
4. El reporte recorre las listas para producir métricas operativas.

## Estrategia de validación

- `try/except` captura conversiones de días inválidas en el menú.
- Las funciones de dominio lanzan `ValueError` para reglas incumplidas.
- Las pruebas cubren límites, duplicados, disponibilidad, vencimiento, devolución y reporte.
