from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Oracle Forest"



def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("oooopen the gates.................................................. or die")

    goblin2 = Goblin("gooblin")
    goblin = Goblin("goog")
    hero = Hero("guy")
    
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print(f"the hero: {hero.name} enters the arena with {hero.health} health.")

    heroFirstAttack = hero.attack()
    print(f"{hero.name} attacks {goblin.name}, landing {heroFirstAttack} damage!")
    goblin.take_damage(heroFirstAttack)
 

    if(goblin.is_alive):
        anotherAttack = hero.attack()
        print(f"{hero.name} attacks {goblin.name}, landing {anotherAttack} damage!")
        goblin.take_damage(anotherAttack)
    

    

if __name__ == "__main__":
    main()
