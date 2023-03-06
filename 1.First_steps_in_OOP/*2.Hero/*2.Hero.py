class Hero:
    def __init__(self, name, health):
        self.name = str(name)
        self.health = int(health)

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, energy):
        self.health += energy


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))


"""
------------------------------------ Problem to resolve --------------------------------

Create a class called Hero. Upon initialization, it should receive a name (string) and health 
(number). Create two additional methods:
⦁	defend(damage) - reduce the given damage from the hero's health:
⦁	if the health become 0 or less, set it to 0 and return "{name} was defeated"
⦁	heal(amount) - increase the health of the hero with the given amount
-------------------------------------- Example inputs ----------------------------------
Test Code	
hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))	
Output
None
None
Peter was defeated

"""
