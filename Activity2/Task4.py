class Book:
  def __init__(self, title, author, year_attributes):
    self.title = title
    self.author = author
    self.year_attributes = year_attributes

  def describe(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"Year_attributes: {self.year_attributes}")

b1 = Book("The Sympathizer", "Viet Thanh Nguyen", 2015)
b2 = Book("An American Marriage", "Tayari Jones", 2018)
b3 = Book("The House on Mango Street", "Sandra Cisneros", 1983)


print("book1: ")
b1.describe()
print("book2: ")
b2.describe()
print("book3: ")
b3.describe()