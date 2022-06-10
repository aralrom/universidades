# Universidad 

Se quiere implementar un programa que gestione una universidad.

La universidad cuenta con:

- Alumnos

- Profesores

- Asignaturas

- Bachelors

Un alumno tiene un nombre, una edad y unos conocimientos. Los conocimientos son 0 cuando empieza en la universidad. Cada vez que el alumno estudia por si solo sus conocimientos se incrementan en 5.

Un profesor tiene un nombre, una edad y unos conocimientos. Los conocimientos son 100 cuando la universidad contrata a un profesor. Un profesor puede enseñar a un alumno, en este caso el conocimiento del alumno se incrementa en 10 puntos y el del profesor en 1 punto, ya que al enseñar también se aprende.

Un Bacherlor tiene un nombre y asignaturas.

Una asignatura tiene nombre y código. A una asignatura se le puede asignar un profesor y se le pueden añadir alumnos. La asignatura debe permitir consultar el número actual de estudiantes.

La asignatura debe permitir dar una clase, donde el profesor enseñará a todos los alumnos. En caso de que no hayan alumnos registrados, la asignatura levantará la excepción ClaseSinEstudiantes, y en caso de que no haya profesor ClaseSinProfesor. Ambas excepciones deben ser ExcepcionesUniversidad.

Todos los atributos de las clases deben ser privados, es decir, deben empezar con un _ al inició. Por ejemplo: _nombre. Para permitir acceder a los atributos se deberán implementar todos los getters y los setters haciendo uso de properties para el caso de datos de tipo simples como enteros o string, y de funciones especificas en casos de atributos complejos como listas.



## Evaluación

La evaluación vendrá dada por el número de tests superados:

La nota de la actividad se desglosa de la siguiente forma:
    

- 6p Tests unitarios
      
- 2p Tests de integracion
      
- 2p Tests de excepciones



## Instalación en linux

Instalación de Visual Studio Code

```
snap install --classic code
```

Instalación de pytest

```
sudo apt-get install python3-pytest
```

Descarga del repositorio

```
git clone https://github.com/kiey/universidad_estudiantes
```

Abrir el repositorio

```
cd universidad_estudiantes
code .
```

Ejecutar los tests

```
pytest-3 test.py
```

Consultar la nota actual

```
python3 nota.py
```

