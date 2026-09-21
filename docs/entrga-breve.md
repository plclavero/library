# Documento breve de entrega - Biblioteca barrial

## Dominio elegido

El programa modela los préstamos de una biblioteca barrial. Permite al personal de atención registrar libros, estudiantes, docentes, préstamos y devoluciones.

## Problema que resuelve

El sistema evita prestar un libro que no está disponible, superar límites de préstamos y perder el seguimiento de préstamos vencidos. También permite conocer rápidamente cuántos libros quedan disponibles y qué persona concentra más préstamos activos.

## Organización del código

`Libro` representa el catálogo y controla disponibilidad. `Prestamo` es el registro central y calcula su estado. `Usuario` es la clase base; `Estudiante` y `Docente` heredan de ella con `super().__init__()` y definen límites distintos.

Las funciones buscan registros, registran libros y usuarios, crean préstamos, gestionan devoluciones y generan el reporte. El menú usa `try/except` para que una entrada inválida no interrumpa la aplicación.

## Cómo usarlo

Ejecutar:

```text
python tp_integrador_01_biblioteca.py
```

Luego elegir opciones del menú del 1 al 6. Para verificar las reglas principales, ejecutar:

```text
python -m unittest test_tp_integrador_01_biblioteca.py
```
