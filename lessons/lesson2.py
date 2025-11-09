# наследования

#Родительский класс
class Hero:
    def __init__(self, nick_name, lvl, hp):
        #атрибуты класса
        self.nick_name = nick_name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return self.nick_name
# Дочерный класс
class MageHero(Hero):
    def __init__(self, nick_name, lvl, hp, mp):
        super().__init__(nick_name, lvl, hp)
        self.mp =mp


    def action(self):
        return f"Я потомок {self.nick_name}"



obj_1 = Hero("Олег", 100, 1000)
obj_2 = MageHero("Ardager", 10, 100, 50)



# print(obj_1.action())
# print(obj_2.action())

# class A:
#     def action(self):
#         return"A"
#
# class B(A):
#     def action(self):
#         return "B"
# class C(A):
#     def action(self):
#         print(super().action())
#         return "C"
# class D(C, B):
#     ...
#     # def action(self):
#     #     return "D"
# obj_4 = D()
# print(D.__mro__)


class Animal:
    def action(self):
        return "Animal"
class Fly(Animal):
    def action(self):
        return "Fly"
class Swim(Animal):
    def action(self):
        return "Swim"
class Duck(Swim, Fly):
    ...
duck = Duck()
print(duck.action())

#43