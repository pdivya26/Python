'''class Sparrow:
    def chirp(self):
        print("Chirp, Chirp")

class Cat:
    def meow(self):
        print("Meow, Meow")
        
class Girl:
    def talk(self):
        print("Hello, I'm Monica!")
        
class Boy:
    def talk(self):
        print("Hello, I'm Chandler!")
        
def call_talk(o):
    if hasattr(o,'talk'):
        o.talk()
    elif hasattr(o,'chirp'):
        o.chirp()
    else:
        print("Has Neither Talk nor Chirp")
        
x = Sparrow()
call_talk(x)

x = Girl()
call_talk(x)

x = Boy()
call_talk(x)

x = Cat()
call_talk(x)'''

class Add:
    def sum(self, a = 0, b = 0, c = 0):
        if a!=0 and b!=0 and c!=0:
            print("Sum =", a+b+c)
        elif a!=0 and b!=0:
            print("Sum =", a+b)
        else:
            print("Invalid Input!")
            
a = Add()

a.sum(12, 26, 88)

a.sum(15.2, 6.2)

a.sum(85)
