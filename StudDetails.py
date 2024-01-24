nm = input("Enter your name here : ")
rn = input("Enter your roll no here : ")

print("Enter your marks here : ")
phy = int(input("Enter Physics marks here : "))
chem = int(input("Enter Chemistry marks here : "))
mat = int(input("Enter Maths marks here : "))
if(phy >100) | (chem > 100) | (mat > 100):
    print("Invalid Marks")
else:
    if(phy < 35) | (chem < 35) | (mat < 35):
        print("Sorry! You're not eligible")
    else:
        prct = ((phy + chem + mat) / 300)*100
        print(prct)
        if prct >= 35:
            print("Congratulations! You're eligible")
        else:
            print("Sorry! You're not eligible")