while(1):
        ty = int(input("\nMenu\n1. Multiplication Table\n2. Factorial\n3. Fibonacci Sequence\n4. Exit\n"))
        if(ty == 1):
            n = int(input("Enter number here :"))
            for i in range(1, 11):
                print(n,"x",i,"=",n*i)
        elif(ty == 2):
                while(1):
                    fact = 1
                    n = int(input("Enter number here :"))
                    if(n == 0):
                        print("Factorial = 1")
                    else:
                        for i in range(1, n+1):
                            fact = fact*i
                        print("Factorial =",fact)
                        break
        elif(ty == 3):
                while(1):
                        t1 = 0
                        t2 = 1
                        k = int(input("Enter kth term here :"))
                        print("0\t1", end="\t")
                        for i in range(k+1):
                                t3 = t1 + t2
                                print(t3, end="\t")
                                t1 = t2
                                t2 = t3
                        break
        elif(ty == 4):
                break
        else:
                print("Invalid Operator")
