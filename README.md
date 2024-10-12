# Bank Simulator
#### Video Demo: https://youtu.be/1kdiuzP4Pwk
#### Description:
A bank simulator developed during CS50P with account management and stock price retrieval using the Twelve Data API.

## Account Class
The project has a class "Account" that simulates a bank account. The __init__ method initialises a bank account with self.number which calls the account_number() function and generates an account number between 1000000000 and 999999999999.

## Functions
The Account class has serveral methods that mimic the functions of a bank account.
1. get_input(self)
The get_input() method greets the user and prompts the user to choose one of the following (1,2,3,4,5):1. To open a bank account 2. To deposit 3. To withdraw 4. To get Information about a stock 5. To Quit
To avoid user from accidently opening multiple account inititally self.account_opened is set to False. After the account is opened self.account_opened is set to True. Since the self.account_opened is set to True, it triggers the else block which prompts the user to choose one of the following (2,3,4,5):2. To deposit 3. To withdraw 4. To get Information about a stock 5. To Quit. Which avoids the user from opening account again.
In case of invalid input, try and except block is implemented to catch them.

2. deposit(self, deposit)
The deposit method allows the user to deposit money into their account. If the deposit amount is less than or equal to 0, it prompts the user to enter a valid deposit amount. Once a valid amount is entered, it adds the deposit to the account balance and updates the transaction summary file with a timestamp of the deposit.
3. withdraw(self, withdraw)
This method enables the user to withdraw money from their account. It checks if the withdrawal amount is valid and ensures the user has sufficient funds. If the withdrawal amount exceeds the available balance, it informs the user and displays the current balance. If the withdrawal is successful, the account balance is updated, and the transaction is recorded with a timestamp.
4. update(self)
The update method writes the current balance of the account to the summary file, keeping track of all transactions. Each time a deposit or withdrawal is made, this method ensures the account balance is recorded.
5. stocks()
This function allows the user to get real-time stock price information using the Twelve Data API. The user inputs a stock symbol (e.g., AAPL for Apple), and the function sends a GET request to the Twelve Data API. The JSON response is formatted and returned, showing the price of the stock per minute. This feature adds a real-world financial aspect to the project.

Key Functionalities

Account Creation: The program ensures the user can open only one account and prevents multiple account creations by using the self.account_opened flag.
Deposits and Withdrawals: Users can deposit or withdraw funds, with error handling to manage invalid inputs and insufficient funds.
Transaction Summary: Every transaction (deposit or withdrawal) is recorded with a timestamp in a text file specific to the user’s account number. The current balance is also regularly updated in this file.
Stock Information: Users can check real-time stock prices using the Twelve Data API, which provides up-to-date information for any stock symbol they enter.
Error Handling: The program uses try-except blocks to catch invalid inputs (such as entering non-numeric values for amounts) and prompts users to enter valid data.

This bank simulator project showcases basic banking operations like account creation, deposits, withdrawals, and fetching stock information via an API. It’s a great foundation that can be expanded with more advanced features and a better user interface.
