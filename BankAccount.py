class BankAccount:
    def __init__(self, acc_num, holder, initial_balance):
        # private attributes
        self.__account_number = acc_num
        self.__account_holder = holder
        self.__balance = initial_balance

    # Read-only property for account number
    @property
    def account_number(self):
        return self.__account_number

    # Getter for balance
    @property
    def balance(self):
        return self.__balance

    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = amount

    def deposit(self, amount):
        # Validate and add to balance
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Validate and subtract from balance
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def display_account_info(self):
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__account_holder)
        print("Balance:", self.__balance)