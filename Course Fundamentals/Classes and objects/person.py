class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self, id):
        return f"My name is {self.name} and I am {self.age} years old. My id is {id}"

person_1 = Person("Ivan", 33)

print(person_1.introduce(1))