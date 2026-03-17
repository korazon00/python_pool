from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")

    deck = Deck()

    spell_card = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    creature_card = CreatureCard("Fire Dragon", 5, "legendary", 7, 5)
    artifact_card = ArtifactCard("Mana Crystal", 2, "Common", 3,
                                 "+1 mana per turn")

    cards = [spell_card, creature_card, artifact_card]
    for card in cards:
        deck.add_card(card)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:\n")

    deck.shuffle()

    while True:
        try:
            card = deck.draw_card()
            deck.remove_card(card.name)
            print(f"Drew: {card.name} ({card.__class__.__name__})")
            print("Play result:", card.play({}))
            print()
        except IndexError:
            break
        except ValueError as e:
            print(e)
            print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR", e)
