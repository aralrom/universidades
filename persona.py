""" def test_crear_estudiante(self):
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
        assert(isinstance(e, Estudiante)) """




class Persona():
    def __init__(self, nombre, edad):
        self._nombre=nombre 
        self._edad=edad
        
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
  
 
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,valor):
        self._edad = valor



class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self._conocimientos = 0

    @property
    def conocimientos(self):
        return self._conocimientos
      
 
    @conocimientos.setter
    def conocimientos(self,valor):
        self._conocimientos = valor

          
    def estudiar(self):
        self._conocimientos = self._conocimientos + 5


class Profesor(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self._conocimientos = 100

    @property
    def conocimientos(self):
        return self._conocimientos
      
 
    @conocimientos.setter
    def conocimientos(self,valor):
        self._conocimientos = valor
    

    def ensenar(self, estudiante):
        self._conocimientos += 1
        estudiante._conocimientos += 10





