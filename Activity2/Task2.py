class Stdnt:
  def __init__(self, n, a, c):
    self.n = n
    self.a = a
    self.c = c

  def introduce(self):
    print(f"hello my name is {self.n}, I am {self.a} years old, and my course is {self.c}")
    
st1 = Stdnt("Ramy Justine Fabi", 20, "DIP-IT")
st2 = Stdnt("Christian Q. Alvarado", 21, "DIP-SA")
st3= Stdnt("Mark P. Piñero", 23, "Foreman")

st1.introduce()
st2.introduce()
st3.introduce()