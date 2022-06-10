from persona import Estudiante
import pytest
from persona import *
from bachelor import *
from excepcionesUniversidad import *


class Test_unitariossetter():
    def test_crear_estudiante(self):
        e = Estudiante("Beethoven", 30)
        assert(e.nombre == "Beethoven")
        assert(e.edad == 30)

    def test_getter_setter_estudiante(self):
        e = Estudiante("Beethoven", 30)
        e.nombre = "Ludwig"
        assert(e.nombre == "Ludwig")
        e.edad = 20
        assert(e.edad == 20)

    def test_estudiar(self):
        e = Estudiante("Beethoven", 30)
        assert(e._conocimientos == 0)

        e.estudiar()
        assert(e._conocimientos == 5)

    def test_herencia_estudiante(self):
        e = Estudiante("Beethoven", 30)
        assert(isinstance(e, Persona))
        assert(isinstance(e, Estudiante))

    def test_herencia_profesor(self):
        e = Profesor("Bach", 40)
        assert(isinstance(e, Persona))
        assert(isinstance(e, Profesor))

    def test_crear_profesor(self):
        p = Profesor("Bach", 40)
        assert(p._conocimientos == 100)

    def test_ensenar(self):
        p = Profesor("Bach", 40)
        assert(p._conocimientos == 100)

        e = Estudiante("Beethoven", 30)
        assert(e._conocimientos == 0)

        p.ensenar(e)
        assert(e._conocimientos == 10)
        assert(p._conocimientos == 101)

    def test_crear_asignatura(self):
        a = Asignatura("Python", 3112)

    def test_getter_setters_asignatura(self):
        a = Asignatura("Python2", 3112)
        assert(a.codigo == 3112)
        assert(a.nombre == "Python2")

        a.codigo = 20
        a.nombre = "Python1"
        assert(a.codigo == 20)
        assert(a.nombre == "Python1")

    def test_anadir_profesor(self):
        a = Asignatura("Python2", 3112)
        assert(a.profesor is None)
        p = Profesor("Bach", 40)
        a.profesor = p
        assert(a.profesor is p)

    def test_anadir_estudiantes(self):
        a = Asignatura("Python2", 3112)
        assert(a.profesor is None)

        e = Estudiante("Beethoven", 30)
        e2 = Estudiante("Mozzart", 16)
        a.anadir_estudiantes(e)
        a.anadir_estudiantes(e2)
        assert(a.get_numero_estudiantes() == 2)

    def test_bachelor_getters_setters(self):
        b = Bachelor("Data Science")
        a = Asignatura("Python2", 1234)
        b.anadir_asignatura(a)
        b.eliminar_asignatura(a)

    def test_bachelor_eliminar_asignatura_no_anadida(self):
        b = Bachelor("Data Science")
        a = Asignatura("Python2", 1234)
        with pytest.raises(ValueError) as e:
            b.eliminar_asignatura(a)
        assert e.type == ValueError


class Test_integracion():

    def test_dar_clase(self):
        a = Asignatura("Python2", 3112)

        e = Estudiante("Beethoven", 30)
        e2 = Estudiante("Mozzart", 16)
        a.anadir_estudiantes(e)
        a.anadir_estudiantes(e2)

        p = Profesor("Bach", 40)
        a.profesor = p

        a.dar_clase()

        assert(e.conocimientos == 10)
        assert(e2.conocimientos == 10)
        assert(p._conocimientos == 102)


class Test_excepciones():

    def test_dar_clase_sin_estudiantes(self):
        a = Asignatura("Python2", 3112)
        p = Profesor("Bach", 40)

        a.profesor = p
        with pytest.raises(ClaseSinEstudiantes) as e:
            a.dar_clase()
        assert e.type == ClaseSinEstudiantes

    def test_dar_clase_sin_profesor(self):
        a = Asignatura("Python2", 3112)

        e = Estudiante("Beethoven", 30)
        e2 = Estudiante("Mozzart", 16)
        a.anadir_estudiantes(e)
        a.anadir_estudiantes(e2)

        with pytest.raises(ClaseSinProfesor) as e:
            a.dar_clase()
        assert e.type == ClaseSinProfesor

    def test_excpecion_generica(self):

        assert(issubclass(ClaseSinEstudiantes, ExcepcionesUniversidad))
        assert(issubclass(ClaseSinProfesor, ExcepcionesUniversidad))
