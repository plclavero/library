# Especificación SDD - Sistema de préstamos de Biblioteca Barrial

**Producto:** Biblioteca Barrial  
**Versión de especificación:** 1.0  
**Estado:** implementado y verificado  
**Implementación:** `tp_integrador_01_biblioteca.py`

## 0. Contexto del producto

### Problema

El personal de una biblioteca barrial registra manualmente libros prestados, devoluciones y límites por persona usuaria. Esta práctica dificulta conocer si un ejemplar está disponible, habilita préstamos que superan límites acordados y oculta los casos vencidos hasta que alguien los revisa manualmente.

### Necesidad del negocio

La biblioteca necesita una consola simple para operar el préstamo de ejemplares sin duplicar registros ni perder el estado de cada préstamo. El resultado esperado es una decisión confiable al momento de prestar un libro y un reporte que permita priorizar el seguimiento.

### Personas usuarias

| Persona | Objetivo | Dolor actual |
|---|---|---|
| Personal de atención | Registrar operaciones correctamente. | Debe recordar disponibilidad y límites. |
| Estudiante | Obtener libros para estudiar. | Puede desconocer su límite de préstamos. |
| Docente | Obtener material para su actividad. | No tiene una vista de sus préstamos activos. |
| Coordinación | Supervisar actividad y vencimientos. | No posee un reporte consolidado. |

## 1. Principios del producto

1. **Integridad antes que velocidad:** un préstamo inválido no se registra.
2. **Trazabilidad:** cada préstamo conserva su historial incluso luego de la devolución.
3. **Reglas explícitas:** límites, plazos y disponibilidad no dependen de memoria humana.
4. **Recuperación ante error:** una entrada inválida informa el problema y devuelve al menú.
5. **Explicabilidad:** cada clase, función y decisión puede ser explicada por quien presenta el trabajo.

## 2. Objetivo y criterios de éxito

El sistema debe permitir registrar libros, estudiantes, docentes, préstamos y devoluciones mediante un menú. Debe impedir operaciones inválidas y generar un reporte de estado.

La solución es exitosa si:

- Nunca existen identificadores duplicados.
- Ningún libro tiene dos préstamos activos simultáneos.
- Ninguna persona supera su límite.
- El reporte identifica préstamos activos, vencidos y libros disponibles.
- Una entrada inválida no detiene la ejecución.

## 3. Alcance

### IN

- Registro de libros, estudiantes y docentes.
- Creación y devolución de préstamos.
- Clasificación de préstamo: `Activo`, `Vencido` o `Devuelto`.
- Reporte operativo y menú de consola.
- Validación con excepciones y pruebas automatizadas.

### OUT

- Persistencia en archivos o base de datos.
- Login, permisos o autenticación.
- Cálculo con fechas reales, multas o reservas.
- Búsqueda por título, autor o categoría.
- Interfaz gráfica o conexión con otros sistemas.

## 4. Modelo de dominio y datos

| Entidad | Responsabilidad | Datos | Comportamiento |
|---|---|---|---|
| `Libro` | Representar un ejemplar del catálogo. | ID, título, autor, disponibilidad. | Marcar préstamo o devolución. |
| `Prestamo` | Registro principal de una operación. | ID, libro, usuario, días transcurridos, devolución. | Calcular estado y registrar devolución. |
| `Usuario` | Clase base de persona usuaria. | ID, nombre. | Definir contrato de límite. |
| `Estudiante` | Usuario con política estudiantil. | Institución. | Máximo 2 préstamos. |
| `Docente` | Usuario con política docente. | Área o materia. | Máximo 5 préstamos. |

Las colecciones en memoria son `libros`, `usuarios` y `prestamos`. Se utilizan strings para IDs y textos, enteros para días y límites, booleanos para disponibilidad/devolución y listas para organizar objetos.

## 5. Datos de entrada, proceso y salida

| Operación | Entrada | Proceso | Salida |
|---|---|---|---|
| Registrar libro | ID, título, autor. | Validar obligatorios y unicidad. | Libro creado/disponible o error. |
| Registrar usuario | Tipo, ID, nombre, institución/área. | Crear subclase correspondiente. | Usuario creado o error. |
| Crear préstamo | ID, ID de libro, ID de usuario, días. | Validar existencia, disponibilidad, límite y días. | Préstamo y estado, o error. |
| Devolver | ID de préstamo. | Validar existencia/estado y restaurar disponibilidad. | Devolución confirmada o error. |
| Reportar | Colecciones actuales. | Recorrer préstamos y libros. | Métricas y persona con más activos. |

## 6. Reglas de negocio

| ID | Regla | Justificación |
|---|---|---|
| RN-01 | Los IDs de libro, usuario y préstamo son únicos por colección. | Evita ambigüedad y duplicados. |
| RN-02 | Un libro disponible puede tener un solo préstamo activo. | Un ejemplar físico no puede estar prestado a dos personas. |
| RN-03 | Estudiante tiene límite de 2 préstamos activos. | Política de préstamo estudiantil. |
| RN-04 | Docente tiene límite de 5 préstamos activos. | Política de préstamo docente. |
| RN-05 | Días transcurridos es entero mayor o igual a 0. | Evita estados imposibles. |
| RN-06 | Más de 14 días clasifica el préstamo como `Vencido`. | Plazo operativo de la biblioteca. |
| RN-07 | La devolución cambia el estado a `Devuelto`, pero conserva el préstamo. | Mantiene trazabilidad. |
| RN-08 | La devolución habilita nuevamente el libro. | Permite un próximo préstamo válido. |
| RN-09 | Un dato inválido no interrumpe el menú. | El personal puede corregir y continuar. |

## 7. Flujo de la persona usuaria

```text
Abrir aplicación
       |
       v
Elegir opción del menú
       |
       +-- 1 Registrar libro ------> validar -> guardar -> confirmar/error
       |
       +-- 2 Registrar usuario ----> elegir tipo -> validar -> guardar -> confirmar/error
       |
       +-- 3 Crear préstamo -------> validar reglas -> crear -> informar estado/error
       |
       +-- 4 Registrar devolución -> validar -> devolver -> confirmar/error
       |
       +-- 5 Ver reporte ----------> calcular métricas -> mostrar reporte
       |
       +-- 6 Salir ----------------> cerrar aplicación
       |
       v
Volver al menú mientras no se elija salir
```

## 8. Flujos de decisión

### 8.1 Creación de préstamo

```text
Recibir ID préstamo, libro, usuario y días
                 |
                 v
¿ID de préstamo único y días >= 0?
       | sí                     | no
       v                        v
¿Existen libro y usuario?     Mostrar error
       | sí        | no
       v           v
¿Libro disponible?          Mostrar error
       | sí        | no
       v           v
¿Usuario bajo su límite?  Mostrar error
       | sí        | no
       v           v
Crear préstamo y marcar libro no disponible
```

### 8.2 Clasificación de estado

```text
¿El préstamo fue devuelto?
      | sí              | no
      v                 v
  Devuelto        ¿Días > 14?
                    | sí      | no
                    v         v
                 Vencido    Activo
```

### 8.3 Devolución

```text
Ingresar ID de préstamo
           |
           v
¿Existe y no fue devuelto?
       | sí            | no
       v               v
Marcar devuelto,      Mostrar error
habilitar libro
```

## 9. Requisitos funcionales priorizados

| ID | Prioridad | Requisito |
|---|---|---|
| RF-01 | Must | Registrar libros únicos. |
| RF-02 | Must | Registrar estudiantes y docentes con límites distintos. |
| RF-03 | Must | Crear préstamos solo cuando cumplen todas las reglas. |
| RF-04 | Must | Registrar devoluciones y restaurar disponibilidad. |
| RF-05 | Must | Clasificar préstamos por estado. |
| RF-06 | Must | Generar reporte de cuatro métricas. |
| RF-07 | Must | Recuperarse de entradas numéricas inválidas. |

## 10. Criterios de aceptación

### CA-01: registrar catálogo

**Dado** un ID de libro no registrado, **cuando** se ingresan ID, título y autor válidos, **entonces** debe crearse un libro disponible.

### CA-02: evitar duplicados

**Dado** un libro ya registrado, **cuando** se intenta usar su mismo ID, **entonces** debe informarse un error sin crear un segundo libro.

### CA-03: límite de estudiante

**Dado** un estudiante con 2 préstamos activos, **cuando** se intenta crear el tercero, **entonces** se debe rechazar sin modificar el nuevo libro.

### CA-04: límite de docente

**Dado** un docente con 4 préstamos activos, **cuando** se crea el quinto, **entonces** debe permitirse; el sexto debe rechazarse.

### CA-05: libro no disponible

**Dado** un libro con préstamo activo, **cuando** otra persona lo solicita, **entonces** debe rechazarse.

### CA-06: vencimiento

**Dado** un préstamo con 15 días, **cuando** se consulta su estado, **entonces** debe ser `Vencido`.

### CA-07: devolución

**Dado** un préstamo activo, **cuando** se registra su devolución, **entonces** su estado debe ser `Devuelto` y el libro debe estar disponible.

### CA-08: error recuperable

**Dado** texto en un campo numérico, **cuando** se procesa la opción, **entonces** se muestra un error y el menú sigue disponible.

## 11. Casos límite y manejo de excepciones

| Situación | Comportamiento esperado |
|---|---|
| Menú fuera de rango | Informar opción inválida. |
| Texto en días | Capturar `ValueError` y volver al menú. |
| Días negativos | Rechazar creación del préstamo. |
| ID de libro/usuario inexistente | Rechazar préstamo. |
| Devolución repetida | Informar que ya fue devuelto. |
| No hay préstamos activos | Reportar ausencia de persona líder. |
| Empate de préstamos activos | Mostrar la primera persona registrada con el máximo. |

## 12. Reporte y métricas

El reporte recorre las listas en memoria y calcula:

1. Cantidad de préstamos activos.
2. Cantidad de préstamos vencidos.
3. Cantidad de libros disponibles.
4. Persona con mayor cantidad de préstamos activos, si existe.

## 13. Trazabilidad

| Regla/Requisito | Criterio | Código | Prueba |
|---|---|---|---|
| RN-01 / RF-01 | CA-02 | `agregar_libro`, `agregar_usuario`, `crear_prestamo` | `test_identificador_duplicado` |
| RN-03 | CA-03 | `Estudiante.limite_prestamos` | `test_estudiante_no_puede_superar_dos_prestamos` |
| RN-04 | CA-04 | `Docente.limite_prestamos` | `test_docente_puede_tener_cinco_prestamos` |
| RN-02 | CA-05 | `crear_prestamo` | `test_libro_no_disponible` |
| RN-06 | CA-06 | `Prestamo.estado` | `test_prestamo_vencido_y_devolucion` |
| RN-07/RN-08 | CA-07 | `registrar_devolucion` | `test_prestamo_vencido_y_devolucion` |
| RF-06 | Reporte | `generar_reporte` | `test_reporte` |

## 14. Plan técnico y tareas completadas

1. Modelar clases y herencia con `super().__init__()`.
2. Crear funciones de búsqueda, registro, préstamo, devolución y reporte.
3. Construir menú con manejo de excepciones.
4. Implementar pruebas automatizadas de reglas críticas.
5. Documentar operación, límites y trazabilidad.

## 15. Transparencia sobre asistencia de IA y autoría

Este material fue desarrollado mediante colaboración entre una persona humana y Codex. La persona humana definió el dominio, las reglas y decisiones finales; Codex asistió en documentación, diseño, pruebas y código. Quien presente el trabajo debe poder explicar el funcionamiento de cada parte entregada.
