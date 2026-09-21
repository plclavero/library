# Diplomatura - Fundamentos de Programación Asistida por IA
Este repositorio reúne ejercicios y documentación de la diplomatura. Su proyecto principal es el Trabajo Integrador del Curso 1: un sistema de consola para gestionar préstamos de una biblioteca barrial.

## Trabajo integrador: Biblioteca Barrial
La biblioteca necesita registrar libros, estudiantes, docentes, préstamos y devoluciones sin duplicar registros ni prestar ejemplares no disponibles. El sistema aplica límites de préstamos por tipo de persona usuaria e identifica préstamos vencidos.

### Funcionalidades
- Registrar libros, estudiantes y docentes.
- Crear préstamos solo cuando el libro está disponible y la persona usuaria no supera su límite.
- Registrar devoluciones y restaurar la disponibilidad del libro.
- Clasificar préstamos como activos, vencidos o devueltos.
- Generar un reporte de actividad y disponibilidad.

### Ejecutar el programa
```bash
python tp_integrador_01_biblioteca.py
```

### Ejecutar las pruebas

```bash
python -m unittest test_tp_integrador_01_biblioteca.py
```

## Documentación SDD

- [Consigna del trabajo](docs/consigna.md)
- [Especificación funcional SDD](RFC-Biblioteca.md)
- [Constitución del producto](Constitucion.md)
- [Plan de implementación](Plan-Implementacion.md)
- [Tareas y trazabilidad](Tareas.md)
- [Documento breve de entrega](docs/entrega-breve.md)

## Transparencia sobre asistencia de IA
El material fue desarrollado mediante colaboración entre una persona humana y Codex. La persona humana definió objetivos, reglas y decisiones finales; Codex asistió en documentación, diseño, pruebas y código. Quien presente el trabajo debe poder explicar el funcionamiento de cada parte.
