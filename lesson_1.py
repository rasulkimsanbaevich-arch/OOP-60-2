#class
class Herro:
    # конструктор класса
    def __init__(self, nick_name, lvl, hp):
        # Атрибуты класса
        self.nick_name = nick_name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return (f"{self.nick_name} hi this my base action!")
#object
kirito = Herro("Kirito", 100, 1000)
asuna = Herro("Asuna", 100, 1000)
print(kirito.action())
print(asuna.action())
