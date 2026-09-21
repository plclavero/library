"""Sistema de consola para gestionar préstamos de una biblioteca barrial."""

PLAZO_PRESTAMO_DIAS = 14


class Libro:
    def __init__(self, identificador, titulo, autor):
        self.identificador = identificador
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True


class Usuario:
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre

    def limite_prestamos(self):
        raise NotImplementedError("Cada tipo de usuario debe definir su límite.")


class Estudiante(Usuario):
    def __init__(self, identificador, nombre, institucion):
        super().__init__(identificador, nombre)
        self.institucion = institucion

    def limite_prestamos(self):
        return 2


class Docente(Usuario):
    def __init__(self, identificador, nombre, area):
        super().__init__(identificador, nombre)
        self.area = area

    def limite_prestamos(self):
        return 5


class Prestamo:
    def __init__(self, identificador, libro, usuario, dias_transcurridos):
        self.identificador = identificador
        self.libro = libro
        self.usuario = usuario
        self.dias_transcurridos = dias_transcurridos
        self.devuelto = False

    def estado(self):
        if self.devuelto:
            return "Devuelto"
        if self.dias_transcurridos > PLAZO_PRESTAMO_DIAS:
            return "Vencido"
        return "Activo"

    def registrar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()


def buscar_libro(libros, identificador):
    return next((libro for libro in libros if libro.identificador == identificador), None)


def buscar_usuario(usuarios, identificador):
    return next((usuario for usuario in usuarios if usuario.identificador == identificador), None)


def buscar_prestamo(prestamos, identificador):
    return next((prestamo for prestamo in prestamos if prestamo.identificador == identificador), None)


def agregar_libro(libros, identificador, titulo, autor):
    if not identificador or not titulo or not autor:
        raise ValueError("Identificador, título y autor son obligatorios.")
    if buscar_libro(libros, identificador):
        raise ValueError("Ya existe un libro con ese identificador.")
    libro = Libro(identificador, titulo, autor)
    libros.append(libro)
    return libro


def agregar_usuario(usuarios, tipo, identificador, nombre, dato_extra):
    if not identificador or not nombre or not dato_extra:
        raise ValueError("Todos los datos de la persona usuaria son obligatorios.")
    if buscar_usuario(usuarios, identificador):
        raise ValueError("Ya existe una persona usuaria con ese identificador.")
    if tipo == "1":
        usuario = Estudiante(identificador, nombre, dato_extra)
    elif tipo == "2":
        usuario = Docente(identificador, nombre, dato_extra)
    else:
        raise ValueError("El tipo debe ser 1 para estudiante o 2 para docente.")
    usuarios.append(usuario)
    return usuario


def prestamos_activos_de_usuario(prestamos, usuario):
    return [prestamo for prestamo in prestamos if prestamo.usuario is usuario and not prestamo.devuelto]


def crear_prestamo(prestamos, libros, usuarios, identificador, id_libro, id_usuario, dias_transcurridos):
    if buscar_prestamo(prestamos, identificador):
        raise ValueError("Ya existe un préstamo con ese identificador.")
    if dias_transcurridos < 0:
        raise ValueError("Los días transcurridos no pueden ser negativos.")

    libro = buscar_libro(libros, id_libro)
    usuario = buscar_usuario(usuarios, id_usuario)
    if libro is None:
        raise ValueError("No existe el libro indicado.")
    if usuario is None:
        raise ValueError("No existe la persona usuaria indicada.")
    if not libro.disponible:
        raise ValueError("El libro no está disponible para préstamo.")
    if len(prestamos_activos_de_usuario(prestamos, usuario)) >= usuario.limite_prestamos():
        raise ValueError("La persona usuaria alcanzó su límite de préstamos activos.")

    prestamo = Prestamo(identificador, libro, usuario, dias_transcurridos)
    libro.prestar()
    prestamos.append(prestamo)
    return prestamo


def registrar_devolucion(prestamos, identificador):
    prestamo = buscar_prestamo(prestamos, identificador)
    if prestamo is None:
        raise ValueError("No existe un préstamo con ese identificador.")
    if prestamo.devuelto:
        raise ValueError("Ese préstamo ya fue devuelto.")
    prestamo.registrar_devolucion()
    return prestamo


def generar_reporte(libros, usuarios, prestamos):
    activos = [prestamo for prestamo in prestamos if prestamo.estado() == "Activo"]
    vencidos = [prestamo for prestamo in prestamos if prestamo.estado() == "Vencido"]
    disponibles = sum(libro.disponible for libro in libros)
    conteo_por_usuario = {
        usuario.identificador: len(prestamos_activos_de_usuario(prestamos, usuario))
        for usuario in usuarios
    }
    mayor_usuario = None
    if conteo_por_usuario and max(conteo_por_usuario.values()) > 0:
        id_mayor = max(conteo_por_usuario, key=conteo_por_usuario.get)
        mayor_usuario = buscar_usuario(usuarios, id_mayor)

    return {
        "prestamos_activos": len(activos),
        "prestamos_vencidos": len(vencidos),
        "libros_disponibles": disponibles,
        "usuario_con_mas_prestamos": mayor_usuario,
    }


def mostrar_reporte(libros, usuarios, prestamos):
    reporte = generar_reporte(libros, usuarios, prestamos)
    mayor = reporte["usuario_con_mas_prestamos"]
    print("\n--- Reporte de préstamos ---")
    print(f"Préstamos activos: {reporte['prestamos_activos']}")
    print(f"Préstamos vencidos: {reporte['prestamos_vencidos']}")
    print(f"Libros disponibles: {reporte['libros_disponibles']}")
    if mayor:
        print(f"Persona con más préstamos activos: {mayor.nombre} ({mayor.identificador})")
    else:
        print("No hay préstamos activos registrados.")


def menu():
    libros, usuarios, prestamos = [], [], []
    while True:
        print("\n1. Registrar libro\n2. Registrar persona usuaria\n3. Crear préstamo")
        print("4. Registrar devolución\n5. Mostrar reporte\n6. Salir")
        opcion = input("Elegí una opción del 1 al 6: ").strip()
        try:
            if opcion == "1":
                agregar_libro(libros, input("ID del libro: ").strip(), input("Título: ").strip(), input("Autor: ").strip())
                print("Libro registrado correctamente.")
            elif opcion == "2":
                tipo = input("Tipo: 1 estudiante / 2 docente: ").strip()
                etiqueta = "Institución educativa" if tipo == "1" else "Área o materia"
                agregar_usuario(usuarios, tipo, input("ID de usuario: ").strip(), input("Nombre completo: ").strip(), input(f"{etiqueta}: ").strip())
                print("Persona usuaria registrada correctamente.")
            elif opcion == "3":
                dias = int(input("Días transcurridos desde el préstamo (0 o más): "))
                prestamo = crear_prestamo(prestamos, libros, usuarios, input("ID del préstamo: ").strip(), input("ID del libro: ").strip(), input("ID de usuario: ").strip(), dias)
                print(f"Préstamo creado. Estado actual: {prestamo.estado()}.")
            elif opcion == "4":
                registrar_devolucion(prestamos, input("ID del préstamo a devolver: ").strip())
                print("Devolución registrada correctamente.")
            elif opcion == "5":
                mostrar_reporte(libros, usuarios, prestamos)
            elif opcion == "6":
                print("Gracias por usar el sistema de biblioteca.")
                break
            else:
                print("Opción inválida. Elegí un número del 1 al 6.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    menu()
