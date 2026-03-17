from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")

    elite = EliteCard('Arcane Warrior', 4, "Legendary", 5, 3, 4)

    meth_card = [k for k, v in Card.__dict__.items() if not k.startswith("_")]
    meth_combatable = [k for k, v in Combatable.__dict__.items()
                       if not k.startswith("_")]
    meth_magical = [k for k, v in Magical.__dict__.items()
                    if not k.startswith("_")]

    print("- Card:", meth_card)
    print("- Combatable:", meth_combatable)
    print("- Magical:", meth_magical)

    print("\nPlaying Arcane Warrior (Elite Card):")
    print("\nCombat phase:")

    print("Attack result:", elite.attack("Enemy"))
    print("Defense result:", elite.defend(5))

    print("\nMagic phase:")
    print("Spell cast:", elite.cast_spell('Fireball', ['Enemy1', 'Enemy2']))
    print("Mana channel:", elite.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
