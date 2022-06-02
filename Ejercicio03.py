class Student:
    '''
    En este ejemplo se hace uso del Establecer y Obtener(set y get)
    '''
    def __init__(self, name, subjects):
        self.set_name(name)
        self.set_subjects(subjects)

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    def set_subjects(self, subjects):
        if not isinstance(subjects, list):
            raise TypeError("subjects must be a list")
        self.subjects = subjects

    def get_name(self):
        return self._name

    def get_subjects(self):
        return self.subjects

'Creamos el objeto estudiante de tipo Student y lo inicializamos con su constructor'
student = Student("Eduardo", ["Mate", "POO", "Humanismo"])

'Decidimos actualizar los datos por valores diferentes'
student.set_name("Daniel")
student.set_subjects(["Programacion", "Estructuras", "Algebra"])

'Comprobamos lo ingresado, debería obtenerse los datos actualizados'
print("Estudiante: {}".format(student.get_name()))
print("Materias: {}".format(student.get_subjects()))

