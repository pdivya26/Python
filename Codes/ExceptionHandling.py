#Division by Zero Exception

a = int(input("Enter first number here : "))
b = int(input("Enter second number here : "))

try:
    c=a/b
    
except Exception as e:
    print("Error :",e)
    
else:
    print("Quotient =",c)
    
finally:
    print("Executed Completed!")

#Multiple Exception Handling

def avg(l):
    avg = sum(l)/len(l)
    print("Average =",avg)

try:  
    l = [0, 2, 4, 6, 8]
    print("\nList :",l)
    avg(l)
    m = [1, 0.5, "a"]
    n = []
    print("List :",m,"and",n)
    avg(m)
    avg(n)
except TypeError:
    print("Please check elements in the list!\n")
    
except ZeroDivisionError:
    print("Please do not provide empty list!\n")


#Using Assert Statement

try:
    a = int(input("Enter your age here : "))
    assert a >= 18, "You're a Minor!\n"
    print("You're an Adult!\n")
    
except AssertionError as obj:
    print(obj)
    
#Handling User-Defined Exceptions
class InvalidAgeException(Exception):
    def __init__(self, m):
        self.msg = m

def check(age):
    if(age < 18):
        raise InvalidAgeException("You're a Minor!\n")
    else:
        print("You're an Adult!\n")
 
a = int(input("Enter your age here : "))

try:
    check(a)
except InvalidAgeException as e:
    print(e)
