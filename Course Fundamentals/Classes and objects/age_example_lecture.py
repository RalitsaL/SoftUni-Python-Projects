class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age_counter(self, number):
        for year in range(2024, 2024 + number):
            self.age += 1
            print(f"year -> {year} -> {self.age}")

person = Person("Ivan", 33)
person.age += 10 # външно модифициране
person.age_counter(20)