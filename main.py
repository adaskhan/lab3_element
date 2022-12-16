from enum import Enum


class Currency(Enum):
    USD = 1
    RUB = 2
    KZT = 3
    EUR = 4


class BankAccount:
    def __init__(self, name, surname, account):
        self.name = name
        self.surname = surname
        self.account = account

    def add_to_bank_account(self, amount):
        self.account += amount

    def subtract_from_bank_account(self, amount):
        self.account -= amount

    def money_conversion(self, currency, rate):
        self.account = self.account * rate
        self.currency = currency

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Account: {self.account} {self.currency.name}"


def main():
    bank_accounts = {}

    while True:
        print("Choose your action:")
        print("1. Creating a user")
        print("2. Select a user")
        print("3. Exit")

        choice = input()

        if choice == "1":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            account = float(input("Enter account balance: "))
            currency = input("Enter currency (USD, RUB, KZT, EUR): ")
            currency = Currency[currency]
            bank_account = BankAccount(name, surname, account)
            bank_account.currency = currency
            bank_accounts[name] = bank_account
        elif choice == "2":
            name = input("Enter name: ")
            bank_account = bank_accounts.get(name)
            if bank_account is None:
                print("User not found")
            else:
                while True:
                    print("Choose your action:")
                    print("1. Add to bank account")
                    print("2. Substract from bank account")
                    print("3. Money conversion")
                    print("4. Exit")

                    action = input()

                    if action == "1":
                        amount = float(input("Enter amount to add: "))
                        bank_account.add_to_bank_account(amount)
                        print(f'Your amount is {bank_account.account} {bank_account.currency}')
                    elif action == "2":
                        amount = float(input("Enter amount to subtract: "))
                        bank_account.subtract_from_bank_account(amount)
                        print(f'Your amount is {bank_account.account} {bank_account.currency}')
                    elif action == "3":
                        currency = input("Enter currency to convert to (USD, RUB, KZT, EUR): ")
                        currency = Currency[currency]
                        rate = float(input("Enter conversion rate: "))
                        bank_account.money_conversion(currency, rate)
                        print(f'Your amount is {bank_account.account} {bank_account.currency}')
                    elif action == "4":
                        break
                    else:
                        print("Invalid choice")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
