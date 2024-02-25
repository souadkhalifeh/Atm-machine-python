class ATM:
    def __init__(self, balance=0, pin=0000):
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        print(f"Available Balance: {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"You have {self.balance} in your balance")
            print("Please try smaller amount")
        else:
            self.balance -= self.amount
            print(f"{self.amount} has been drawn successfully from your balance.")
            print(f"Current Balance: {self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"{self.amount} has been added to your balance.")
        print(f"Current Balance: {self.balance}")

    def change_pin(self, new_pin):
        self.pin = new_pin
        print(f"Your PIN has been changed to {self.pin}")


def main():
    atm = ATM(1000, 1234)
    trials = 3
    print("Welcome to the ATM machine ")
    exit_flag = False  # Introduce an exit flag
    while True:
        pin = int(input("Please enter your 4 digits PIN: "))
        if pin != atm.pin:
            trials -= 1 
            print(f"Wrong pin, You have {trials} trials") 
            if trials == 0:
                print("You have exceeded the maximum number of trials. Please try again later.")
                break
        else:
            while True:
                print(''' Menu:
                    1-Check Balance
                    2-Withdraw
                    3-Deposit
                    4-Change Pin
                    5-Exit
                    ''')
                option = int(input("Please enter your choice: "))

                if option == 1:
                    atm.check_balance()
                elif option == 2:
                    amount = float(input("Enter the amount to withdraw: "))
                    atm.withdraw(amount)
                elif option == 3:
                    amount = float(input("Enter the amount to deposit: "))
                    atm.deposit(amount)
                elif option == 4:
                    new_pin = int(input("Enter your new PIN: "))
                    atm.change_pin(new_pin)
                elif option == 5:
                    print("Thank you for using the ATM machine.")
                    exit_flag = True  # Set the exit flag to True
                    break  # Exit the inner while loop
                else:
                    print("Invalid option. Please check the menu and try again.")
                    continue
                
                more = input("Do you want to perform another transaction? (yes/no)").lower()
                if more != "yes":
                    print("Thank you for using the ATM machine.")
                    exit_flag = True
                    break

            if exit_flag:  
                break  

if __name__ == "__main__":
    main()

