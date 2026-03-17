from ex0.Card import Card
from typing import Dict, List
from enum import Enum


class Effects(Enum):
    debuff = "Debuff target"


class SpellCard(Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)

        valid_effects = ["damage", "heal", "buff", "debuff"]
        if effect_type not in valid_effects:
            raise ValueError(f"effect_type must be one of {valid_effects}")

        self.effect_type = effect_type
        self.used_flag = False

    effects = {
            "damage": "Deal 3 damage to target",
            "heal": "Heal 3 to target",
            "buff": "Buff target",
            "debuff": Effects.debuff
        }

    def play(self, game_state: Dict) -> Dict:
        if self.used_flag:
            raise ValueError("this spell_card already used")
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effects[self.effect_type]
        }
        self.used_flag = True
        return result

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }
