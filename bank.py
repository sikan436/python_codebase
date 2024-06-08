balance=0
def main():

    print("balance",balance)
    deposit(100)
    withdraw(50)
    print("balance",balance)
    
def deposit(n):
    global balance
    balance=balance+n

def withdraw(n):
    global balance
    balance=balance-n

if __name__=="__main__":
    main()



    