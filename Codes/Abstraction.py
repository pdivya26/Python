from abc import *
import math

class abcls(ABC):
    @abstractmethod
    def trigno(self, x):
        pass
     
class sn(abcls):
    def trigno(self, x):
        radx = math.radians(x)
        print("Sine value =",math.sin(radx))
       
class cs(abcls):
    def trigno(self, x):
        radx = math.radians(x)
        print("Cosine value =",math.cos(radx))
        
class tn(abcls):
    def trigno(self, x):
        radx = math.radians(x)
        print("Tangent value =",math.tan(radx))
        
#a = abcls() error
s = sn()
s.trigno(1)

c = cs()
c.trigno(1)

t = tn()
t.trigno(1)

print()

from abc import *
class abclass(ABC):
    @abstractmethod
    def abm1(self):
        pass

    def abm2(self):
        print("This is abstract method 2 in abstract class")

class concclass(abclass):
    def abm1(self):
       print("This is abstract class method 1 in concrete class")

    def abm2(self):
        print("This is abstract class method 2 in concrete class")
      
c = concclass()
c.abm1()
c.abm2()
