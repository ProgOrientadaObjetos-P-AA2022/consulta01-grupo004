class Student:

    def __init__(self, name, subjects):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        elif not isinstance(subjects, list):
            raise TypeError("subjects must be a list")
        self.name = name
        self.subjects = subjects

    def print_info(self):
        print("Nombre: {}.".format(self.name))
        print("Asignaturas: {}.".format(self.subjects))

estudiante = Student("Daniel", ["Programacion", "Estructuras", "Algebra"])
estudiante.print_info()