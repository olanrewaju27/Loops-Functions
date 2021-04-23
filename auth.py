
database = {

    8190748418:  ["ren", "len", "hjsdfy", "rtt", 0]


}
import random
def init():

    isValidOptionSelected = False
    print("welcome to bank")

    

    haveAccount = int(input("Do you have an account with us: 1(Yes) 2(No)\n"))

    if(haveAccount == 1):
            
        login()
    elif(haveAccount == 2):
           
        register()
    else:
        print("Please select a valid function")
        init()

def login():


    print("Welcome to the login page")

    
    accountNumberUser = int(input("Please input your account number\n"))
    password = input("Enter your password\n")

    for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberUser):
                if(userDetails[3]== password):
                     bankOperation(userDetails)

    else:       
        print("invalid login details")


     
    
    


def register():
    print("*****Register*****")
    email = input("What is your email address? \n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = input("Create a password \n")

    account_balance = 0

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password, account_balance]

    print("Your account has been createdd")
    print("Your Account number is %d" %accountNumber)
    print("Thank you for choosing Bank")
    login()



def bankOperation(user):
    print("Welcome %s %s" %(user[0], user[1]))
    
    selectedOption =int(input("What would you like to do today: (1)Deposit (2)Withdrawal (3)Logout (4) Exit\n"))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("invalid option selected")

        bankOperation()



def depositOperation():

    account_balance = 0

    x = int(input("how much do you want to deposit? \n"))

    account_balance = 0 + x

    account_balance = userDetails[4]



    print("your new account balance is %d" %account_balance)

    withdrawalOperation()





def withdrawalOperation():
    y = int(input("How much do you want to withdraw? \n"))

    account_balance = userDetails[4]

    if account_balance > y:
        print("Please wait ...")
        print("Thank you for using bank")

    else: 
        print("Insufficient funds")

    

    login()


def logout():
    login()


def generateAccountNumber():
    
    return random.randrange(1111111111, 9999999999)


init()



