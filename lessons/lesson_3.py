# инкапсуляция
import random
import string
class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name # открытая атрибута
        self._balance = balance # Защищенная атрибута
        self.__password = password #Приватная атрибута

    def login(self, password):
        if self.__password == password:
            print("Вы вошли!")
        else:
            print("Не верный пароль!!")

    def get_balance(self, password):
        if self.__password ==password:
            return self._balance
        else:
            return "Не верный пароль!!"

    def __random_pass(self):
        chart = string.ascii_letters + string.digits
        password = ''.join(random.choice(chart) for _ in range(6))
        return password

    def get_new_pass(self):
        return self.__random_pass()

john = BankAccount("John", 10000, "123qwerty")

# john.login("12qwerty")
# print(john.get_balance("123qwerty"))
# print(john.get_new_pass())

# Абстракция
# from abc import ABC, abstractmethod
#
# # Абстрактный класс
# class Animal(ABC):
#     # @abstractmethod
#     def make_sound(self):
#         pass
#     @abstractmethod
#     def move(self):
#         pass
# class Dog(Animal):
#     # def make_sound(self):
#     #     return "Gaf Gaf"
#     def move(self):
#         return "Step"
#
#
# # gufi = Dog()
# # print(gufi.make_sound())
#
# class SmsSend(ABC):
#     @abstractmethod
#     def send_sms(self):
#         pass
# class KgSms(SmsSend):
#     def send_sms(self):
#         text = "<text>1234</text>"
#         phone = "<phone>+996779</phone>"
#         # self.send(text,phone)
# class RUSms(SmsSend):
#     def send_sms(self):
#         data = {
#             "text": "1234",
#             "phone": "+7925"
#         }
#         # self.send_sms(data)
#