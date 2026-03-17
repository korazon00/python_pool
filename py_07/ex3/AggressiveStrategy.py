from ex3.GameStrategy import GameStrategy
from typing import Dict, List
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        targets = [t for t in available_targets if isinstance(t, CreatureCard)]
        if targets:
            return targets
        else:
            return ["Enemy player"]

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        played = []
        mana_used = 0

        for card in hand:
            if card.cost <= 5 and isinstance(card, CreatureCard):
                played.append(card.name)
                mana_used += card.cost

        return {
            "cards_played": played,
            "mana_used": mana_used,
            "targets_attacked": self.prioritize_targets([battlefield]),
            "damage_dealt": mana_used
        }
