from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict
from enum import Enum


class Tmp(Enum):
    combat_type = "melee"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int,
                 mana: int) -> None:
        super().__init__(name, cost, rarity)

        self.elite_attack = attack
        self.health = health
        self.mana = mana

    def play(self, game_state: Dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card enters battlefield"
        }

    def attack(self, target: str) -> Dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.elite_attack,
            "combat_type": Tmp.combat_type.value
        }

    def defend(self, incoming_damage: int) -> Dict:
        blocked = min(incoming_damage, self.health)
        taken = incoming_damage - blocked
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack": self.elite_attack,
            "health": self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> Dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:
        return {
            "mana": self.mana,
            "cost": self.cost
        }
