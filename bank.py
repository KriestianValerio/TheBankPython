

balance = 0

def deposit(money) :
    global balance
    balance = balance + money
    return balance

    
    # Input : (Integer) The amount of money that a user wants to deposit
    # Output : (None) No Output
    
    # Add the money to the current balance
    
    #################
    ### implement ###
    #################
    # Do something on here !
    #################

def withdrawal(money) :
    global balance
    balance = balance - money
    return balance

    
    # Input : (Integer) The amount of money that a user wants to withdraw
    # Output : (None) No Output
    
    # Withdraw the money from the current balance

    #################
    ### implement ###
    #################
    # Do something on here !
    #################


def bank() :
    # Input : (None) No Input
    # Output : (None) No Output
    global balance
    while True:
        process = input("Deposit(d) or withdrawal(w) or balance check(c)? ")
        
        if process == ' ':
            return
        if process == 'd':
            moneyinput = int(input("how much money do you want to deposit? "))
            balance = deposit(moneyinput)
            print("You have deposited", moneyinput,"won")
        if process == 'w':
            moneywithdraw = int(input("how much money do you want to withdraw? "))
            if moneywithdraw > balance:
                print(f"You've withdrawn {moneywithdraw} won \n but you only have {balance} won")
            else:
                balance = withdrawal(moneywithdraw)
                print("You have withdraw", moneywithdraw,"won")
        if process == 'c':
            print("Your current balance is ", balance,"won")
        

        # If a user's input is empty string (''), then quit this function.
        # If a user's input is 'd', then ask the amount of money to deposit and deposit it.
        # If a user's input is 'w', then ask the amount of money to withdraw and withdraw it.
        # If a user's input is 'c', then check the current balance.

        #################
        ### implement ###
        #################
        # Do something on here !
        #################

bank()
