import random
from typing import List, Dict
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty")
        return self.cards[0]

    def get_deck_stats(self) -> Dict:
        stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0
        }
        if not self.cards:
            return stats

        costs = 0
        for card in self.cards:
            costs += card.cost

            name = card.__class__.__name__

            if "Creature" in name:
                stats["creatures"] += 1
            elif "Spell" in name:
                stats["spells"] += 1
            elif "Artifact" in name:
                stats["artifacts"] += 1

        stats["avg_cost"] = float(f"{costs / len(self.cards):.1f}")
        return stats
