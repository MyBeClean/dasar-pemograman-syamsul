class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, " + self.name

    def greets(self):
        return f"Your age is {self.age}"

    def welcome(self):
        message = self.greet()
        age_message = self.greets()
        print(message + "! Welcome to our website.")
        print(age_message)
        print(message + "! Hope you enjoy.")

# input data
name = input("Masukkan nama: ")
age = input("Masukkan umur: ")

p1 = Person(name, age)
p1.welcome()
