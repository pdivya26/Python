while(1):
        type = int(input("Menu\n1. Arithmetic\n2. Logical\n3. Bitwise\n4. Exit\n"))
        if(type == 4):
                break
        elif(type == 1):
                while(1):
                        op = int(input("Menu\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n"))
                        if(op == 5):
                                break
                        
                        a = int(input("Enter first number here :"))
                        b = int(input("Enter second number here :"))
                        
                        if op == 1:
                                print("Sum = ", a+b)
                        elif(op == 2):
                                print("Difference = ", a-b)
                        elif(op == 3):
                                print("Product = ", a*b)
                        elif(op == 4):
                                if b != 0:
                                    print("Quotient =", a/b)
                                else:
                                    print("Error")
                                    break
                        else:
                                print("Invalid Operator")
        elif(type == 2):
                while(1):
                        op = int(input("Menu\n1. Logical AND \n2. Logical OR\n3. Logical NOT\n4. Exit\n"))
                        if(op == 4):
                                break
                        
                        a = int(input("Enter first number here :"))
                        b = int(input("Enter second number here :"))
                        c = int(input("Enter third number here :"))
                        
                        if(op == 1):
                                print("Result = ", a>b and a>c)
                        elif(op == 2):
                                print("Result = ", a<b or a<c)
                        elif(op == 3):
                                print("Result = ", not (a>b and a<c))
                        else:
                                print("Invalid Operator")
        elif(type == 3):
                while(1):
                        op = int(input("Menu\n1. Bitwise AND\n2. Bitwise OR\n3. Bitwise XOR\n4. Exit\n"))
                        if(op == 4):
                                break
                        
                        a = int(input("Enter first number here :"))
                        b = int(input("Enter second number here :"))
                        
                        if(op == 1):
                                print("AND = ", a&b)
                        elif(op == 2):
                                print("OR = ", a|b)
                        elif(op == 3):
                                print("XOR = ", a^b)
                        else:
                                print("Invalid Operator")
        
        else:
                print("Invalid Operator")
