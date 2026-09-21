import unittest

from tp_integrador_01_biblioteca import (
    Estudiante,
    agregar_libro,
    agregar_usuario,
    crear_prestamo,
    generar_reporte,
    registrar_devolucion,
)


class BibliotecaBarrialTest(unittest.TestCase):
    def setUp(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def test_estudiante_no_puede_superar_dos_prestamos(self):
        estudiante = agregar_usuario(self.usuarios, "1", "U1", "Ana", "UNAJ")
        for indice in range(1, 4):
            agregar_libro(self.libros, f"L{indice}", f"Libro {indice}", "Autor")
        crear_prestamo(self.prestamos, self.libros, self.usuarios, "P1", "L1", estudiante.identificador, 0)
        crear_prestamo(self.prestamos, self.libros, self.usuarios, "P2", "L2", estudiante.identificador, 0)
        with self.assertRaisesRegex(ValueError, "límite"):
            crear_prestamo(self.prestamos, self.libros, self.usuarios, "P3", "L3", estudiante.identificador, 0)

    def test_docente_puede_tener_cinco_prestamos(self):
        docente = agregar_usuario(self.usuarios, "2", "U1", "Luis", "Historia")
        for indice in range(1, 6):
            agregar_libro(self.libros, f"L{indice}", f"Libro {indice}", "Autor")
            crear_prestamo(self.prestamos, self.libros, self.usuarios, f"P{indice}", f"L{indice}", docente.identificador, 0)
        self.assertEqual(len(self.prestamos), 5)

    def test_libro_no_disponible(self):
        agregar_usuario(self.usuarios, "1", "U1", "Ana", "UNAJ")
        agregar_usuario(self.usuarios, "1", "U2", "Sol", "UNAJ")
        agregar_libro(self.libros, "L1", "Libro", "Autor")
        crear_prestamo(self.prestamos, self.libros, self.usuarios, "P1", "L1", "U1", 0)
        with self.assertRaisesRegex(ValueError, "disponible"):
            crear_prestamo(self.prestamos, self.libros, self.usuarios, "P2", "L1", "U2", 0)

    def test_identificador_duplicado(self):
        agregar_libro(self.libros, "L1", "Libro", "Autor")
        with self.assertRaisesRegex(ValueError, "existe"):
            agregar_libro(self.libros, "L1", "Otro", "Autor")

    def test_prestamo_vencido_y_devolucion(self):
        agregar_usuario(self.usuarios, "1", "U1", "Ana", "UNAJ")
        libro = agregar_libro(self.libros, "L1", "Libro", "Autor")
        prestamo = crear_prestamo(self.prestamos, self.libros, self.usuarios, "P1", "L1", "U1", 15)
        self.assertEqual(prestamo.estado(), "Vencido")
        registrar_devolucion(self.prestamos, "P1")
        self.assertTrue(libro.disponible)
        self.assertEqual(prestamo.estado(), "Devuelto")

    def test_reporte(self):
        agregar_usuario(self.usuarios, "1", "U1", "Ana", "UNAJ")
        agregar_libro(self.libros, "L1", "Libro 1", "Autor")
        agregar_libro(self.libros, "L2", "Libro 2", "Autor")
        crear_prestamo(self.prestamos, self.libros, self.usuarios, "P1", "L1", "U1", 15)
        reporte = generar_reporte(self.libros, self.usuarios, self.prestamos)
        self.assertEqual(reporte["prestamos_vencidos"], 1)
        self.assertEqual(reporte["libros_disponibles"], 1)


if __name__ == "__main__":
    unittest.main()
