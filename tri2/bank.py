# ----------------------
# Made by Brady Hodge
# Status: Graded
# Assignment 12A ; 1/2
# Module
# ----------------------
class Account:
    def __init__(self, account_name, account_number):
        """stores account information"""
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0

    def deposit(self, deposit_float):
        """deposits into an account"""
        if deposit_float > 0:
            self.balance += deposit_float

    def withdraw(self, withdraw_float):
        """withdraws into an account"""
        if self.balance - withdraw_float > 0:
            self.balance -= withdraw_float


def get_accounts():
    """gets and returns the accounts"""
    savings = Account('Savings', 801234)
    savings.balance = 100.00
    checking = Account('Checking', 801232)
    checking.balance = 153.28
    emergency_fund = Account('Emergency Fund', 801237)
    emergency_fund.balance = 652.94
    return [savings, checking, emergency_fund]


def get_account(accounts_list):
    """asks user what account they would like to use"""
    valid_input = False
    while not valid_input:
        print('--- List of Accounts ---')
        account_list_number = 0
        for item in accounts_list:
            account_list_number += 1
            print('{}-({})-{:<15}{:>5}{:>7.2f}'.format(account_list_number, item.account_number, item.account_name, '$',
                                                       item.balance))
        what_account = int(input('What account would you like to use? '))
        valid_input = True
        try:
            return accounts_list[(what_account - 1)]
        except:
            print('')
            print('There was a problem, please try using a valid input.')
            print('')
            valid_input = False
