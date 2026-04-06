class BankAccount:
    def __init__(self, acc_num, holder, initial_balance=0.0):
        # Private attributes
        self._account_number = acc_num
        self._account_holder = holder
        self._balance = initial_balance
        self._transactions = []  # bonus: transaction history

    # Read-only account number
    @property
    def account_number(self):
        return self._account_number

    # Balance getter
    @property
    def balance(self):
        return self._balance

    # Balance setter with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero.")
            return

        self._balance += amount
        self._transactions.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance: {self._balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
            return

        if amount > self._balance:
            print("Insufficient funds.")
            return

        self._balance -= amount
        self._transactions.append(f"Withdrew {amount}")
        print(f"Withdrew {amount}. New balance: {self._balance}")

    # Display account info
    def display_account_info(self):
        print("---- Account Details ----")
        print(f"Holder: {self._account_holder}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self._balance}")

    # Bonus: show transaction history
    def show_transactions(self):
        print("---- Transaction History ----")
        for t in self._transactions:
            print(t)

account = BankAccount("123456", "Samuel", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # should fail

account.display_account_info()
account.show_transactions()