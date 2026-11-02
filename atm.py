balance = 9000

print("Welcome to ATM")
print("1. Check balance")
print("2. Deposit amount")
print("3. Withdraw amount")
print("4. Quit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance amount:", balance)

elif choice == 2:
    deposit = int(input("Enter deposit amount: "))

    if deposit > 0:
        balance = balance + deposit
        print("Deposit successful")
        print("Updated balance:", balance)
    else:
        print("Invalid deposit amount")

elif choice == 3:
    withdraw = int(input("Enter withdraw amount: "))

    if withdraw <= 0:
        print("Invalid withdrawal amount")
    elif withdraw > balance:
        print("Insufficient balance")
    else:
        balance = balance - withdraw
        print("Withdrawal successful")
        print("Updated balance:", balance)

elif choice == 4:
    print("Thank you for using ATM")

else:
    print("Invalid transaction")