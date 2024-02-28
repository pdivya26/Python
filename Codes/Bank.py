class Bank:
    def __init__(self):
        self.bal = 50000
        self.wd = 0
        self.dt = 0
        
    def withdraw(self):
        self.wd = int(input("Enter amount to be withdrawn here : "))
        if(self.wd > 0 and self.wd <= self.bal):
            print(self.wd,"will be debited from your account\nDo you want to proceed ?")
            d = int(input("\nMenu :\n1. Yes\n2. No\n"))
            if(d == 1):
                self.bal -= self.wd
                print("Amount Withdrawn Successfully\nBalance after withdrawal =",self.bal)
        elif(self.wd >= self.bal):
            print("Insufficient Balance!")
        elif(self.wd <= 0):
            print("Amount Invalid!")
            
    def deposit(self):
        self.dt = int(input("Enter amount to be deposited here : "))
        if(self.dt > 0):
            print(self.dt,"will be credited into your account\nDo you want to proceed ?")
            d = int(input("\nMenu :\n1. Yes\n2. No\n"))
            if(d == 1):
                self.bal += self.dt
                print("Amount Deposited Successfully\nBalance after deposition =",self.bal)
        elif(self.dt <= 0):
            print("Amount Invalid!")
            
    def balance(self):
        self.bal
        print("Your current balance is",self.bal)

b1 = Bank()

while(1):
    ch = int(input("\nMenu :\n1. Withdraw Money\n2. Deposit Money\n3. View Balance\n4. Exit\nEnter your choice here : "))
    
    if(ch == 4):
        break
    elif(ch == 1):
        b1.withdraw()
    elif(ch == 2):
        b1.deposit()
    elif(ch == 3):
        b1.balance()
    else:
        print("Invalid Choice!")
