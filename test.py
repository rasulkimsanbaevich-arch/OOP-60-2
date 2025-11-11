
from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

class BankAccount:
    bank_name = "Simba"  # атрибут класса

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance      # защищённый
        self.__password = password   # приватный

    def login(self, password):
        if password == self.__password:
            return f"Добро пожаловать, {self.hero.name}!"
        else:
            return "Неверный пароль!"

    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Баланс: {self._balance} монет"

    @classmethod
    def get_bank_name(cls):
        return f"Банк: {cls.bank_name}"

    @staticmethod
    def bonus_for_level(lvl):
        return lvl * 10
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            total = self._balance + other._balance
            return f"Сумма балансов: {total} SOM"
        else:
            return "Ошибка: герои разных типов!"

    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl

class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": f"{phone}"}

if __name__ == "__main__":
    mage = MageHero("Merlin", 40, 100, 150)
    warrior = WarriorHero("Conan", 50, 200, 0)

    print(mage.action())
    print(warrior.action())

    acc1 = BankAccount(mage, 5000, "pass1")
    acc2 = BankAccount(warrior, 3000, "pass2")

    print(acc1)
    print(acc2)
    print(BankAccount.get_bank_name())
    print(f"Бонус за {warrior.lvl} уровень: {BankAccount.bonus_for_level(warrior.lvl)} SOM")

    sms = KGSms()
    print(sms.send_otp("+996777123456"))
