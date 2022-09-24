from random import randint, random
import os
from winreg import CreateKeyEx
import time


def createAccount():
    os.system('cls')
    createAccount.accountName = input("Enter Name : ")
    createAccount.accountNumber = randint(2314555594594, 9212151515151)
    createAccount.accountBalance = input("Enter Amount to Deposit : ")


def displayAccount():
    if (hasattr(createAccount, 'accountName')):
        os.system('cls')
        print('Account Holder : {}' .format(createAccount.accountName))
        print('Account Number : {}' .format(createAccount.accountNumber))
        print('Account Balance : {}' .format(createAccount.accountBalance))
        input('Press Enter to Continue ')
        time.sleep(0.1)
        os.system('cls')
    else:
        print('-----No Account Exists------')
        time.sleep(0.1)
        os.system('cls')


def Deposit():
    os.system('cls')
    dep = int(input('Enter Amount to Deposit : '))
    createAccount.accountBalance = int(createAccount.accountBalance) + int(dep)
    print('Deposit in Progress.....')
    time.sleep(0.1)
    os.system('cls')


def Withdrawal():
    os.system('cls')
    withdraw = int(input('Enter Amount to Withdraw : '))
    if withdraw <= int(createAccount.accountBalance):
        createAccount.accountBalance = int(
            createAccount.accountBalance) - int(withdraw)
        print('Withdrawal Success !')

    else:
        print('Insufficient Balance')

    print('Clearing....')
    time.sleep(0.2)
    os.system('cls')


while(True):
    print('\n*** Dragon Bank ***\n')
    print('1. Create Account')
    print('2. Display Account')
    print('3. Deposit')
    print('4. Withdrawal')
    print('5. Exit')
    choice = input("Enter Choice : ")
    if choice == str(1):
        createAccount()
        print("Account Created !\nConnecting To Database.....")
        time.sleep(1)
        os.system('cls')
    elif choice == str(2):
        displayAccount()
    elif choice == str(3):
        Deposit()
    elif choice == str(4):
        Withdrawal()
    elif choice == str(5):
        exit(1)
