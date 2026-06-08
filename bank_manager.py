balance = 100.00

def deposit(amount):
  balance += amount
  print(f"Deposited {amount} successfully")
def withdraw(amount):
  if balance > amount:
    balance -= amount
    print(f"")
def check_balance():
  print(f"Available balance: {balance}\n")

while True:
  print("1. Deposit money")
  print("2. Withdraw money")
  print("3. Check balance")
  print("4. Exit")
  choice = input("Choose an option: ")
  
  if choice == "1":
    amount = input("Enter amount to deposit: ")
    deposit(amount)
  elif choice == "2":
    amount = input("Enter amount to withdraw: ")
    withdraw(amount)
  elif choice == "3":
    check_balance(amount)
  elif choice == "4":
    print("Thanks for using our service")
    break
  else:
    print("Invalid option!")