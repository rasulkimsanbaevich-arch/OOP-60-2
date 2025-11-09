class ChessFigure:

    def __init__(self, name, nick, value=" "):
        self.name = name
        self.nick = nick
        self.value = value

    def first(self):
        return f"{self.name} e4"
    def second(self):
        return f"{self.nick} c4"


pawn = ChessFigure("Pawn", "P", 1)
knight = ChessFigure("Knight", "N", 3)
bishop = ChessFigure("Bishop", "B", 3)
rook = ChessFigure("Rook", "R", 5)
quen = ChessFigure("Quen", "Q", 9)
king = ChessFigure("King", "K")

print(pawn.first())
print(bishop.second())