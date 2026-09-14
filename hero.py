import random

class Hero:
    
    #Battle cry: Add a battle_cry() method that prints a custom line.
    def battle_cry():
        print("aaaaaaaaaaaaaaaaaaa")

    def __init__(self, name):
        # Create the Hero's attributes here
        print("hi")
    
        self.name = name
        self.health = 100
        self.attack_power = 14

    def attack(self):
    # Return a random value from 1 through this Hero's attack power.
        Hero.battle_cry()
        return random.randint(1, self.attack_power)
       

    def take_damage(self, damage):
        # Subtract damage, but do not allow health to fall below 0.
        if self.health <= 0:
            self.health -= damage

    def is_alive(self):
        # Return a Boolean based on this Hero's health.
        return (self.health <= 0)


