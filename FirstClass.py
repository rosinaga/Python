lname = []
lclass = []
lage = []
class Student:
    def _init_(self, name, class, age):
        self.name = str(name)
        self.class = str(class)
        self.age = int(age)

    def present(self):
        presentation = self.name + self.class + self.age
        return presentation

    def change_age(self):
        old = self.age + 1
