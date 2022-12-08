from enum import Enum
from typing import List


class Account(Enum):
    usd = 'USD'
    rub = 'RUB'
    kzt = 'KZT'
    eur = 'EUR'


class BankAccount:
    def __init__(self, name, surname, account=Account.kzt, balance=0):
        self.name = name
        self.surname = surname
        self.account = account
        self.balance = balance

    def get_balance(self):
        print(f'Ваш баланс {round(self.balance, 2)} {self.account.value}')

    def money_conversion(self, amount, valuta):
        current_wallet_type = self.account.value
        if current_wallet_type == 'KZT':
            if valuta == 'KZT':
                return amount
            elif valuta == 'RUB':
                return amount*7.63
            elif valuta == 'USD':
                return amount*473.25
            elif valuta == 'EUR':
                return amount*497.76
        elif current_wallet_type == 'RUB':
            if valuta == 'KZT':
                return amount*0.13
            elif valuta == 'RUB':
                return amount
            elif valuta == 'USD':
                return amount*62
            elif valuta == 'EUR':
                return amount*65.21
        elif current_wallet_type == 'EUR':
            if valuta == 'KZT':
                return amount*0.002
            elif valuta == 'RUB':
                return amount*0.015
            elif valuta == 'USD':
                return amount*0.95
            elif valuta == 'EUR':
                return amount
        elif current_wallet_type == 'USD':
            if valuta == 'KZT':
                return amount*0.0021
            elif valuta == 'RUB':
                return amount*0.016
            elif valuta == 'USD':
                return amount
            elif valuta == 'EUR':
                return amount*1.05

    def get_account(self):
        print(f'Тип счета {self.name} {self.surname} - {self.account.value}')

    def add_to_bank_account(self, amount, valuta):
        self.balance += self.money_conversion(amount, valuta)
        print(f'Счет {self.name} {self.surname} пополнен на {amount} {valuta}')
        self.get_balance()

    def subtract_from_bank_account(self, amount, valuta):
        self.balance -= self.money_conversion(amount, valuta)
        print(f'Вы сняли деньги банкомате на сумму {amount} {valuta}')
        self.get_balance()

    def set_balance(self, valuta):
        current_balance = self.balance
        current_wallet_type = self.account.value
        if current_wallet_type == 'KZT':
            if valuta == 'KZT':
                return current_balance
            elif valuta == 'RUB':
                return current_balance / 7.63
            elif valuta == 'USD':
                return current_balance / 473.25
            elif valuta == 'EUR':
                return current_balance / 497.76
        elif current_wallet_type == 'RUB':
            if valuta == 'KZT':
                return current_balance / 0.13
            elif valuta == 'RUB':
                return current_balance
            elif valuta == 'USD':
                return current_balance / 62
            elif valuta == 'EUR':
                return current_balance / 65.21
        elif current_wallet_type == 'EUR':
            if valuta == 'KZT':
                return current_balance / 0.002
            elif valuta == 'RUB':
                return current_balance / 0.015
            elif valuta == 'USD':
                return current_balance / 0.95
            elif valuta == 'EUR':
                return current_balance
        elif current_wallet_type == 'USD':
            if valuta == 'KZT':
                return current_balance / 0.0021
            elif valuta == 'RUB':
                return current_balance / 0.016
            elif valuta == 'USD':
                return current_balance
            elif valuta == 'EUR':
                return current_balance / 1.05

    def set_account(self, valuta):
        self.balance = self.set_balance(valuta)
        for acc in Account:
            if acc.value == valuta:
                self.account = acc
        print(f'\nТип счета {self.name} {self.surname} изменен!')
        print(f'Тип счета {self.name} {self.surname} - {self.account.value}')
        self.get_balance()

    def __del__(self):
        print(f'Банк аккаунт {self.name} {self.surname} удален!')


users: List[BankAccount] = []


def choose_user():
    print()
    print('Выбрать пользователь...')
    name = input('name: ')
    surname = input('surname: ')
    current_user = BankAccount('user', 'user')
    wallet_type = Account

    for user in users:
        if user.name == name and user.surname == surname:
            current_user = user
            break
    else:
        print('\nПользователь не найден!')
        return

    while True:
        print("\n1. Пополнить баланс")
        print("2. Снять деньги")
        print("3. Изменить тип счета")
        print("4. Мой баланс")
        print("5. Выйти")
        action = int(input("Выберите ваше действие: "))
        match action:
            case 1:
                amount = int(input("\nСумма: "))
                valuta = input("Валюта: ")
                current_user.add_to_bank_account(amount, valuta)
            case 2:
                amount = int(input("Сумма: "))
                valuta = input("Валюта: ")
                current_user.subtract_from_bank_account(amount, valuta)
            case 3:
                print(f'Ваш текущий счет {current_user.account.value}')
                valuta = input('Валюта: KZT, USD, RUB, EUR: ')
                current_user.set_account(valuta)
            case 4:
                print()
                current_user.get_balance()
            case 5:
                print()
                main()


def create_user():
    name = input('name: ')
    surname = input('surname: ')
    new_user = BankAccount(name, surname)
    users.append(new_user)
    choose_user()


def main():
    print("1. Создание пользователя")
    print("2. Выбрать пользователя")
    print("3. Выйти")
    action = int(input("Выберите ваше действие: "))
    if action == 1:
        create_user()
    elif action == 2:
        choose_user()
    elif action == 3:
        print('Не выбрали пользователя!')


if __name__ == '__main__':
    main()
