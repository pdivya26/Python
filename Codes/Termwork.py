termwork = {}
issues = []

while(1):
    user = int(input("Who are you ?\n1. Faculty\n2. Student\n3. Exit\n"))
    if (user == 1):
        while(1):
            op = int(input("\nMenu:\n1. Enter Heads\n2. Display Records\n3. Calculate Total Marks\n4. Exit\n"))
            if(op == 4):
                break
            elif(op == 1):
                hd =  int(input("Enter no of heads here : "))        
                for i in range(hd):
                    hnm = input("\nEnter name of head here : ")
                    maxmk = int(input("Enter maximum marks here : "))
                    ent = int(input("\nEnter no. of entries here : "))
                    hmk = []
                    termwork[hnm] = hmk
                    for i in range(ent):
                        m = int(input("Enter mark here : "))
                        if(m <= maxmk and m > -1):
                            termwork[hnm].append(m)
                        else:
                            print("Marks Invalid!")
                            m = int(input("Enter mark here : "))
                            if(m <= maxmk and m > -1):
                                termwork[hnm].append(m)
            

            elif(op == 2):
                for i in termwork:
                    print("Head :",i)
                    print("Marks :",termwork[i])
            
            elif(op == 3):
                total = 0
                maxtot = 0
                for i in termwork:
                    total += sum(termwork[i])
                    maxtot += max(termwork[i]) * len(termwork[i])
                print("Total Marks :",total)
                print("Percentage :",(total/maxtot)*100)

    elif(user == 2):
        while(1):
            op = int(input("\nMenu:\n1. Display Records\n2. Calculate Total Marks\n3. Raise Issue\n4. Display Issues Raised\n5. Exit\n"))
    
            if(op == 5):
                break
            elif(op == 1):
                for i in termwork:
                    print("Head :",i)
                    print("Marks :",termwork[i])
            elif(op == 2):
                total = 0
                maxtot = 0
                for i in termwork:
                    total += sum(termwork[i])
                    maxtot += max(termwork[i]) * len(termwork[i])
                print("Total Marks :",total)
                print("Percentage :",(total/maxtot)*100)
            elif(op == 3):
                print("Select issue :\n1. Incorrect Entry of Marks\n2. Incorrect Calculation of Marks\n3. Marks not Awarded\n4. Exit\n")
                iss = int(input("Enter your choice here :"))
                
                if(iss == 1):
                    prob = ['''Incorrect Entry of Marks''']
                    issues.append(prob)
                    print("Issue Raised Successfully")
                elif(iss == 2):
                    prob = ["Incorrect Calculation of Marks"]
                    issues.append(prob)
                    print("Issue Raised Successfully")
                elif(iss == 3 ):
                    prob = ["Marks not Awarded"]
                    issues.append(prob)
                    print("Issue Raised Successfully")
                elif(iss == 4):
                    break
                else:
                    print("Invalid Choice!")
            elif(op == 4):
                for i in issues:
                    print(i)

    elif(user == 3):
            break
    else:
        print("Invalid Choice!")

