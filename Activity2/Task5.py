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


employee = Employee("Ryan Reynolds", "Assassin", 40000)
employee.display_employee()

g_r = int(input("\nEnter Amount of raise: "))
employee.give_raise(g_r) 

employee.display_employee()