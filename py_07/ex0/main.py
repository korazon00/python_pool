from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    card = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)

    print("CreatureCard Info:")
    card_info = card.get_card_info()
    print(card_info)

    print("\nPlaying Fire Dragon with 6 mana available:")
    card_info["mana"] = 6
    print("Playable:", card.is_playable(card_info["mana"]))
    print(card_info)
    print("Play result:", card.play(card_info))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", card.attack_target("Goblin Warrior"))

    print(f"\nTesting insufficient mana ({card_info['mana']} available):")
    print("Playable:", card.is_playable(card_info["mana"]))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
