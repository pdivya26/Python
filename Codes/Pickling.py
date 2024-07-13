#Pickling
import pickle

class Employee:
    def __init__(self, id, nm, sal):
        self.id=id
        self.nm = nm
        self.sal = sal
    def display(self):
        print("\n",self.id,"\n",self.nm,"\n",self.sal,"\n")

f = open("Pickling.txt", "ab")
n = int(input("Enter no. of employees here : "))
for i in range(n):
    id = int(input("\nEnter Employee ID here : "))
    nm = input("Enter Employee Name here : ")
    sal = int(input("Enter Salary here : "))
    e = Employee(id, nm, sal)
    pickle.dump(e, f)
f.close()

#Unpickling

f = open("Pickling.txt", "rb")
print("Employee Details : ")
while True:
    try:
        o = pickle.load(f)
        o.display()
        
    except EOFError:
        print("End of the File!")
        break
f.close()
