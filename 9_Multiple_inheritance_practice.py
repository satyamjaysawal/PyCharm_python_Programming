class Calculation1:
    def summation(self,x,y):
        return x+y;
class Calculation2:
    def multiply(self,x,y):
        return x*y;
class Derived(Calculation1,Calculation2):
    def Devide(self,x,y):
        return x/y;
d = Derived()
print(d.summation(10,20))
print(d.multiply(10,20))
print(d.Devide(10,20))

# Check subclass is or not!
print()
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))