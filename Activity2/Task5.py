class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by ${amount}. New salary: ${self.salary}")

    def display_employee(self):
        print(f"Name: {self.name}\nPosition: {self.position}\nSalary: ${self.salary}")


employee = Employee("Ako", "Technician", 90000)

employee.give_raise(60000)
employee.display_employee()