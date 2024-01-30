price = {}
stock = {}

while(1):
        op = int(input("Menu\n1. Add Fruit\n2. Buy Fruit\n3. View Inventory\n4. Update Price\n5. Update Stock\n6. Total Valuation\n7. Exit\n"))
        if(op == 7):
                break
        elif(op == 1):
                fnm = input("Enter name of the fruit here : ")
                fpr = int(input("Enter price per kg here : "))
                fst = int(input("Enter stock of the fruit (in kg) here : "))

                price[fnm] = fpr
                stock[fnm] = fst
                print("Fruit Added Successfully!")		
        
        elif(op == 2):
                buy = input("Enter name of the fruit here : ")
                qnt = int(input("Enter quantity here : "))
                if buy in stock and stock[buy] >= qnt:
                        print("Total Price :", qnt*price[buy])
                        cnfm = int(input("Do you want to proceed ?\n1. Yes\n2. No\n"))
                        if(cnfm == 1):
                                stock[buy] -= qnt
                                #print("Updated Stock:", stock[buy])
                                print("Fruit Bought Successfully")
                        else:
                                continue
                else:
                        print("Insufficient Quantity")
                                
        elif(op == 3):
                for i in stock:
                        if i in stock:
                                print("Fruit Name :",i)
                                print("Price :", price[i])
                                print("Stock :",stock[i])
                        else:
                                print("No Information Available")
        elif(op == 4):
                fnm = input("Enter name of the fruit here : ")
                npr = int(input("Enter new price here : "))
                if fnm in price:
                        price[fnm] = npr
                        print("Price Updated Successfully")
                else:
                        print("Sorry, Fruit Unavailable!")
                        
        elif(op == 5):
                fnm = input("Enter name of the fruit here : ")
                nst = int(input("Enter quantity to be added here : "))

                if fnm in stock:
                        stock[fnm] += nst
                        print("Stock Updated Successfully")
                        print("Updated Stock:", stock[fnm])
                else:
                        print("Fruit Unavailable")
                        
        elif(op == 6):
                total = 0
                for i in price:
                      cost = price[i]*stock[i]
                      print(cost)
                      total += cost
                      
                print("Total Valuation :", total)
                
        else:
                print("Invalid Choice")
