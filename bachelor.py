from persona import Profesor
from excepcionesUniversidad import *

class Bachelor():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__asignatura = []

    def anadir_asignatura(self, asignatura):
        self.__asignatura.append(asignatura)

    def eliminar_asignatura(self, asignatura):
        self.__asignatura.remove(asignatura)


class Asignatura():
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__profesor = None
        self.__estudiantes = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, profesor):
        self.__profesor = profesor

    def anadir_estudiantes(self, estudiante):
        self.__estudiantes.append(estudiante)

    def eliminar_estudiantes(self, estudiante):
        self.__estudiantes.remove(estudiante)

    def get_numero_estudiantes(self):
        return len(self.__estudiantes)

    def dar_clase(self):
        """El profesor da clase a todos los estudiantes de la clase"""
        if len(self.__estudiantes) == 0:
            raise ClaseSinEstudiantes
        elif self.__profesor is None:
            raise ClaseSinProfesor

        for estudiante in self.__estudiantes:
            self.__profesor.ensenar(estudiante)
