# Amy Schaeffer
# A program creates a bank account utilizing parent classes and class attributes, passing hard coded money amounts into the objects.

class BankAccount: #Creating parent class
    def __init__(self, initial_balance, account_number): #identifying class attributes
        self.balance = initial_balance #initializing initial_balance 
        self.account_number = account_number #initializing account_number
    def withdrawl(self, withdrawl_amt): #defining withdrawl function
        self.balance = self.balance - withdrawl_amount
    def deposit(deposit_amt): #defining deposit function
        self.balance = self.balance + deposit_amt
    def getBalance(): #defining get balance function
        return(self.balance)
           
class CheckingAccount(BankAccount):
    def __init__(self, initial_balance, fees, minimum_balance): #identifying class attributes
        self.balance = initial_balance #initializing initial_balance
        self.fees = fees #initializing fees
        self.minimum_balance = minimum_balance #initializing minimum_balance    
    def deductFees(self): #definging fee deduction funtion
        self.balance = self.balance - self.fees
    def checkMinimumBalance(self): #idefining function to compare against minimum balance
        if self.balance < self.minimum_balance:
            raise ValueError("The balance is below the minimum balance") #raising the ValueError exception
        #I hope I used this right!
    
class SavingsAccount(BankAccount): 
    def __init__(self, initial_balance, interest_rate): #identifying class attributes
        self.balance = initial_balance #initializing account balance attribute
        self.interest_rate = interest_rate # initializing interest rate attribute 
    def addInterest(self): # definiing function to add interest
        self.balance = self.balance + (self.balance * self.interest_rate)
        
def accountInfo(balance): #function to retreive and process account information
    savings_account = SavingsAccount(balance, .02) #passing values into savings class
    checking_account = CheckingAccount(balance, 5, 50) #passing values into checking account class
    try:
        checking_account.checkMinimumBalance() #checking minimum balance
    except ValueError as exception: #handling exception
        checking_account.deductFees() #taking out fees if balance is below minimum
        print(exception) #print reason for exception
        print(f"A fee of $ {checking_account.fees} has been charged to the account") #notify user balance is too low and a fee is being charged
    print(f"Current savings account balance : {savings_account.balance}") #prints current savings balance
    print(f"Current checking account balance: {checking_account.balance}") #prints current checking balance
 
accountInfo(100) #calling a function and passing value of 100 into the accounts
accountInfo(25) #calling function and passing value of 25 into the accounts