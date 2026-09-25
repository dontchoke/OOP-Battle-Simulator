from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Oracle Forest"
def battle(hero: Hero, enemy: Goblin):
    print("hi")
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        print(f"{hero.name} attacks {enemy.name}, landing {hero_damage} damage!")

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)
            print(f"{enemy.name} attacks {hero.name}, landing {enemy_damage} damage!")

    if hero.is_alive():
        print(f"{hero.name} won the battle!")

    else:
        print(f"{enemy.name} won the battle!")


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
    battle(hero, goblin)

    #heroFirstAttack = hero.attack()
    #print(f"{hero.name} attacks {goblin.name}, landing {heroFirstAttack} damage!")
    #goblin.take_damage(heroFirstAttack)
 

    #if(goblin.is_alive):
    #    anotherAttack = hero.attack()
    #    print(f"{hero.name} attacks {goblin.name}, landing {anotherAttack} damage!")
    #    goblin.take_damage(anotherAttack)
    

    

if __name__ == "__main__":
    main()
