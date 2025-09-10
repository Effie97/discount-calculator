# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power         # Encapsulated attribute
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}, and I wield the power of {self._power}!")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass: FlyingHero
class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.name} soars through the sky with {self._power}!")

# Subclass: TechHero
class TechHero(Superhero):
    def use_power(self):
        print(f"{self.name} activates high-tech gear powered by {self._power}!")

# Create instances
hero1 = FlyingHero("Skyblade", "wind manipulation", "Cloud City")
hero2 = TechHero("Circuit", "AI-enhanced armor", "Neo-Tokyo")

# Demonstrate polymorphism
for hero in [hero1, hero2]:
    hero.introduce()
    hero.use_power()