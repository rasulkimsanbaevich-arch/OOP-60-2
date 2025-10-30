class FootballPlayer:
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position
        self.rating = rating

    def action(self):
        return (f"Hi my name is {self.name} i'm {self.position}. My rating is {self.rating}")
    def prime_rating(self):
        self.rating += 6
        return (f"{self.name}'s prime rating was {self.rating}")


messi = FootballPlayer("Messi", "Forward", 88)
ronaldo = FootballPlayer("Ronaldo", "Forward", 85)

print(messi.action())
print(ronaldo.action())
print(messi.prime_rating())