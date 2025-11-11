import random
import string
class BankAccount:
   def __init__(self, name, balance, password):
       self.name = name                 # открытый
       self._balance = balance          # защищённый
       self.__password = password       # приватный

   def deposit(self, amount, password):
       if self.__password == password:
           self._balance += amount
           return self._balance
       else:
           return "Неверный пароль!"

   def withdraw(self, amount, password):
       if password != self.__password:
           return "Неверный пароль!"
       elif amount > self._balance:
           return "Недостаточно средств!"
       else:
           self._balance -= amount
           return self._balance

   def change_password(self, old_password, new_password):
       if self.__password == old_password:
           self.__password = new_password
           return "Пароль изменён!"
       else:
           return "Старый пароль неверный!"

   def get_balance(self, password):
       if self.__password == password:
           return self._balance
       else:
           return "Пароль неыерный!"

   def reset_pin(self, password):
       if password != self.__password:
           return "Неверный пароль!"
       new_pin = self.__generate_pin()
       self.__password = new_pin
       return new_pin

   def __generate_pin(self):
       return ''.join(random.choice(string.digits) for _ in range(4))


john = BankAccount("John", 100, "123qwerty")

print(john.deposit(50, "123qwerty"))  # 150
print(john.withdraw(200, "123qwerty"))  # "Недостаточно средств!"
print(john.get_balance("123qwerty"))  # 150
print(john.change_password("wrong", "new"))  # "Старый пароль неверный"
print(john.reset_pin("123qwerty"))  # например "7291"
print(john.get_balance("7291"))  # 150 (новый пароль работает)

#2
from abc import ABC, abstractmethod

class NotificationSender(ABC):
   @abstractmethod
   def send(self, message, recipient):
       pass

class EmailSender(NotificationSender):
    def __init__(self):
        self._service = "Gmail"
    def send(self, message, recipient):
        return f"Email sent to {recipient}"
    def get_service(self):
        return f"Сервис: {self._service}"

class SmsSender(NotificationSender):
    def __init__(self):
        self._service = "Twilio"
    def send(self, message, recipient):
        return f"SMS sent to {recipient}"
    def get_service(self):
        return f"Сервис: {self._service}"

class PushSender(NotificationSender):
    def __init__(self):
        self._service = "Firebase"
    def send(self, message, recipient):
        return f"Push sent to {recipient}"
    def get_service(self):
        return f"Сервис: {self._service}"
email = EmailSender()
print(email.send("Привет", "john@mail.ru"))
# Email sent to john@mail.ru
print(email.get_service())  # Сервис: Gmail

class UserAuth:
    def __init__(self, username, account: BankAccount, notifier: NotificationSender):
        self.username = username
        self.account = account
        self.notifier = notifier

    def login(self, password):
        result = self.account.get_balance(password)
        if isinstance(result, (int, float)):
            print(self.notifier.send(f"Успешный вход: {self.username}", "system"))
            return True
        return False

    def transfer(self, amount, password, recipient_account: BankAccount):
        withdraw_result = self.account.withdraw(amount, password)
        if isinstance(withdraw_result, str):
            print(withdraw_result)
            return withdraw_result

        recipient_account._balance += amount

        # Отправляем уведомления (и выводим их на экран)
        print(self.notifier.send(f"Перевод {amount} отправлен", "system"))
        print(self.notifier.send(f"Получено {amount} от {self.username}", "system"))

        print(f"Перевод успешен. Новый баланс: {self.account._balance}")
        return "Перевод выполнен успешно!"


john = BankAccount("John", 200, "secret")
alice = BankAccount("Alice", 50, "pass123")
notifier = SmsSender()

auth = UserAuth("john_doe", john, notifier)
auth.login("secret")
auth.transfer(70, "secret", alice)

print(f"John balance: {john._balance}")
print(f"Alice balance: {alice._balance}")











