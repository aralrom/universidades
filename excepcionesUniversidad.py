# Implementar excepciones
from excepcionesUniversidad import *


class ExcepcionesUniversidad(Exception):
    """Clase base de Excepciones"""
    def __str__(self):
        return f'{self.message}'


class ClaseSinEstudiantes(ExcepcionesUniversidad):
    """Raise cuando la asignatura no tiene estudiantes"""
    def __init__(self, message="La asignatura no tiene estudiantes"):
        self.message = message
        super().__init__(self.message)


class ClaseSinProfesor(ExcepcionesUniversidad):
    """Raised cuando la asignatura no tiene profesor"""
    def __init__(self, message="La asignatura no tiene un profesor"):
        self.message = message
        super().__init__(self.message)
