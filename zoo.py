
class Animal:
    def __init__(self, nombre, edad, salud=50, felicidad=50):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad

    def display_info(self):
        print(self.nombre, ': Salud:', self.salud, '%, Felicidad:', self.felicidad, '%')

    def alimentar(self, cuánto=10):
        self.salud += cuánto
        self.felicidad += cuánto

class León(Animal):
    def __init__(self, nombre, edad=0, salud=70, felicidad=60):
        super().__init__(nombre, edad, salud, felicidad)
        self.rugido = 'groagrrrr'

    def alimentar(self):
        super().alimentar(20)

    def hablar(self):
        print(self.rugido)

    def gritar(self):
        print('¡' + self.rugido.upper() + '!')


class Perro(Animal):
    def __init__(self, nombre, edad=0, salud=50, felicidad=70):
        super().__init__(nombre, edad, salud, felicidad)
        self.ladrido = 'guau'

    def alimentar(self):
        super().alimentar(15)

    def hablar(self):
        print(self.ladrido)

    def gritar(self):
        print('¡' + self.ladrido.upper() + '!')

class Gato(Animal):
    def __init__(self, nombre, edad=0, salud=80, felicidad=30):
        super().__init__(nombre, edad, salud, felicidad)
        self.maullido = 'miau'

    def alimentar(self):
        super().alimentar(5)

    def hablar(self):
        print(self.maullido)

    def gritar(self):
        print('¡' + self.maullido.upper() + '!')


##En al menos una de las clases de Animal child que ha creado,
##agregue al menos un atributo único. Dele a cada animal
##diferentes niveles predeterminados de salud y felicidad.
##Los animales también deben responder al método de alimentación
##con diferentes niveles de cambios en la salud y la felicidad.

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def añadir(self, animal):
        self.animals.append(animal)
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

    def hablen_todos(self):
        for i in self.animals:
            i.hablar()

    def griten_todos(self):
        for i in self.animals:
            i.gritar()

    def alimentar_todos(self):
        for i in self.animals:
            i.alimentar()

    def añadir_león(self, name):
        self.añadir(León(name))

    def añadir_perro(self, name):
        self.añadir(Perro(name))

    def añadir_gato(self, name):
        self.añadir(Gato(name))

            
if __name__ == '__main__':
    zoo1 = Zoo("John's Zoo")
    zoo1.añadir_león("Nala")
    zoo1.añadir_león("Simba")
    zoo1.añadir_perro("Rajah")
    zoo1.añadir_gato("Shere Khan")
    zoo1.print_all_info()
    zoo1.hablen_todos()
    zoo1.griten_todos()
    zoo1.alimentar_todos()
    zoo1.print_all_info()
