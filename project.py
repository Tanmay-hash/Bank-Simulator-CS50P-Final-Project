import random
import datetime
import requests
import json
import sys

class Account:
    #initiating an account object
    def __init__(self):
        self.number = account_number()
        self.amount = 0
        self.account_opened = False

    #method to get input from the user
    def get_input(self):
        if self.account_opened == False:
            while True:
                print("Welcome to Bank of Australia\nHow can I help you today?\nChoose one of the following (1,2,3,4,5):\n1. To open a bank account\n2. To deposit\n3. To withdraw\n4. To get Information about a stock\n5. To Quit ")
                try:
                    user_input = int(input())
                except ValueError:
                    print("Invalid Input")
                    sys.exit()
                if user_input != 1:
                    print("You need to open an account first")
                    continue
                else:
                    break
            self.account_opened = True
            while user_input not in [1,2,3,4,5]:
                try:
                    user_input = int(input("Enter a valid input "))
                except ValueError:
                    print("Invalid Input")
        else:
            print("Choose one of the following (2,3,4,5):\n2. To deposit\n3. To withdraw\n4. To get Information about a stock\n5. To Quit ")
            user_input = int(input())
            while user_input not in [2,3,4,5]:
                try:
                    user_input = int(input("Enter a valid input "))
                except ValueError:
                    print("Invalid Input")

        account_number = self.number
        #gets input from the user

        #using match/case for control flow
        match user_input:
            case 1:
                print("Thank you for opening an account with us. Your account number is",account_number)
                self.get_input()
            case 2:
                try:
                    amount = int(input("Enter the deposit amount: "))
                    self.deposit(amount)
                    self.get_input()
                except ValueError:
                    print("Invalid Amount")
            case 3:
                try:
                    amount = int(input("Enter the withdrawal amount: "))
                    self.withdraw(amount)
                    self.get_input()
                except ValueError:
                    print("Invalid Amount")
            case 4:
                print(stocks())
                self.get_input()
            case 5:
                sys.exit("Thank you for using Bank of Australia")

    #deposit method for getting a deposit from the user
    def deposit(self, deposit):
        #deposits if the amount is greater than 0
        while deposit <= 0:
            try:
                deposit = int(input("Enter a valid deposit amount (greater than 0): "))
            except ValueError:
                print("Please enter a valid amount")
                continue
        self.amount += deposit
        with open(f"summary_{self.number}.txt", 'a') as file:
            file.write(f'{datetime.datetime.now()} \n' + 'Credit: $' + str(deposit) + '\n')
        self.update()

    def withdraw(self, withdraw):
        #withdraws only if the balance is greater than the withdrawl amount
        while withdraw <= 0:
            withdraw = int(input("Enter a valid withdrawal amount (greater than 0): "))
        if withdraw <= self.amount:
            self.amount -= withdraw
            with open(f"summary_{self.number}.txt", 'a') as file:
                file.write(f'{datetime.datetime.now()} \n' + 'Debit: $' + str(withdraw) + '\n')
        else:
            print("You don't have sufficient funds")
            print('Available Balance:',self.amount)
        self.update()

    def update(self):
        #updates the current balance
        with open(f"summary_{self.number}.txt", 'a') as file:
            file.write('Current Balance: $' + str(self.amount) + '\n')

def stocks():
    stock = input("Enter stock name ")
    #gets stock information from twelvedata api
    response = requests.get(f"https://api.twelvedata.com/time_series?symbol={stock}&interval=1min&apikey=c40218737cdd4e89bd95049fd4701efb")
    info = json.dumps(response.json(), indent=2)
    return info

#generating a random account number
def account_number():
    number = random.randint(1000000000,999999999999)
    return number


def main():
    account1 = Account()
    account1.get_input()
if __name__ == "__main__":
    main()
