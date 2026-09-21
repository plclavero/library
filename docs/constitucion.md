# Constitución SDD - Biblioteca Barrial

## Propósito

Definir los principios que toda decisión de producto, especificación, implementación y prueba del sistema debe respetar.

## Principios

1. **Reglas antes que código:** toda validación debe existir primero como regla documentada y criterio verificable.
2. **Un préstamo debe ser consistente:** nunca se crea si el libro no está disponible, el usuario no existe o supera su límite.
3. **El historial no se borra:** una devolución conserva el préstamo y cambia su estado.
4. **Los errores son recuperables:** una entrada inválida comunica el problema y no cierra el menú.
5. **Cada responsabilidad tiene un lugar:** las entidades modelan comportamiento propio; las funciones coordinan operaciones; las pruebas verifican reglas críticas.
6. **El producto debe poder explicarse:** se prioriza claridad sobre optimizaciones o complejidad innecesaria.

## Restricciones

- Python estándar, sin dependencias externas.
- Estado en memoria: no se implementa persistencia.
- Interfaz de consola, sin GUI.
- Plazo de vencimiento fijo: 14 días ingresados manualmente
