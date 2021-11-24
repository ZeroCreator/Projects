class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        if len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        if not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        if self.currency != other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.balance

    def __add__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, self.balance - other.balance)

wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
# wallet2 + 45  # ValueError('Данная операция запрещена')

###
import operator

class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        if len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        if not currency.isupper():
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f"Wallet не поддерживает сравнение с {other}")
        if self.currency != other.currency:
            raise ValueError("Нельзя сравнить разные валюты")
        return self.balance == other.balance

    def _operation(self, other, operation):
        if not isinstance(other, Wallet) or self.currency != other.currency:
            raise ValueError("Данная операция запрещена")
        return Wallet(self.currency, operation(self.balance, other.balance))

    def __add__(self, other):
        return self._operation(other, operator.add)

    def __sub__(self, other):
        return self._operation(other, operator.sub)


###
import operator as op

class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError("Неверный тип валюты")
        if len(currency) != 3:
            raise NameError("Неверная длина названия валюты")
        if currency.upper() != currency:
            raise ValueError("Название должно состоять только из заглавных букв")
        self.currency = currency
        self.balance = balance

    def operator(self, other, func, error_1, error_2):
        if not isinstance(other, Wallet):
            raise error_1
        if self.currency != other.currency:
            raise error_2
        return func(self.balance, other.balance)

    def __eq__(self, other):
        return Wallet.operator(self, other, func=op.eq,
                               error_1=TypeError(f'Wallet не поддерживает сравнение с {other}'),
                               error_2=ValueError("Нельзя сравнить разные валюты")
                               )

    def __add__(self, other):
        return Wallet(self.currency, Wallet.operator(self, other, func=op.add,
                                                     error_1=ValueError('Данная операция запрещена'),
                                                     error_2=ValueError('Данная операция запрещена')
                                                     ))

    def __sub__(self, other):
        return Wallet(self.currency, Wallet.operator(self, other, func=op.sub,
                                                     error_1=ValueError('Данная операция запрещена'),
                                                     error_2=ValueError('Данная операция запрещена')
                                                     ))


