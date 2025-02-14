class Car:
  def __init__(self, brnd, mdl, yr):
    self.brnd = brnd
    self.mdl = mdl
    self.yr = yr

  def display_info(self):
    print(f"Brand: {self.brnd}")
    print(f"Model: {self.mdl}")
    print(f"Year: {self.yr}")

m1 = Car("Honda", "Civic 11th gen", 2021)
m2 = Car("Volkswagen", "Jetta", 2025)

print("Car 1: ")
m1.display_info()
print("\nCar 2: ")
m2.display_info()