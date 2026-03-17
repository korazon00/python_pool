from ex0.Card import Card
from typing import Dict
from enum import Enum


class Tmp(Enum):
    TYPE = "Creature"


class CreatureCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        if not isinstance(cost, int) or cost <= 0:
            raise ValueError("cost must be a positive integer")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        if game_state:
            game_state["mana"] -= self.cost
        return result

    def attack_target(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info["type"] = Tmp.TYPE.value
        info["attack"] = self.attack
        info["health"] = self.health
        return info
