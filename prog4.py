
# Create a class that accepts two numbers. Create another class that fetches the last digit of those two numbers. 
# Create a third class that multiplayer that last two digits.
# Example: Class A: Accept two numbers.
# 		    Class B: Fetches the last digits of the numbers
# 		    Class C: Multiplay the last two digits.
class a:
    def __init__(self, x,y):
        self.x=x
        self.y=y
class b(a):
    def __init__(self):
        m1=a.x//10
        m2=a.y//10
class c(b):
    def __init__(self):
        result=b.m1*b.m2
p1=a(25,24)
print(p1)