# ----------------------
# Made by Brady Hodge
# Status: Graded
# Assignment 12A; 2/2
# Script
# ----------------------

import bank
bank_accounts = bank.get_accounts()
# program runs until the user quits
keep_going = True
while keep_going:
    # asks user what they would like to do
    user_option = input(
        'What would you like to do?\n    (d)eposit into an account.\n    (w)ithdaw from an account.\n    '
        'e(x)it the application.\n    ')
    # if the user wants to deposit
    if user_option == 'd':
        this_account = bank.get_account(bank_accounts)
        print('Your current balance is: ${}'.format(this_account.balance))
        deposit_float = float(input('How much do you want to deposit? '))
        try:
            this_account.deposit(deposit_float)
        except:
            break

        print('Your new balance is: ${}'.format(this_account.balance))
        print('')
    # if the user wants to withdraw
    elif user_option == 'w':
        this_account = bank.get_account(bank_accounts)
        print('Your current balance is: ${}'.format(this_account.balance))
        withdraw_float = float(input('How much do you want to withdraw? '))
        try:
            this_account.withdraw(withdraw_float)
        except:
            break

        print('Your new balance is: ${}'.format(this_account.balance))
        print('')
    # if the user wants to exit
    elif user_option == 'x':
        print('Goodbye,\nHave a wonderful day.')
        break
    # if input invalid
    else:
        print('There was a problem, please try using a valid input.\n')
