import random
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict
from enum import Enum


class Type(Enum):
    TYPE = "Tournament"


class TournamentCard (Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, damage, healt, defence_power, id):
        self.damage = damage
        self.health = healt
        self.id = id
        self.defence_power = defence_power
        self.type = Type.TYPE.value
        self.wins = 0
        self.losses = 0
        self.rating = self.calculate_rating()
        super().__init__(name, cost, rarity)

    def play(self, game_state: Dict) -> Dict:
        game = {}
        if self.is_playable(game_state["mana_used"]):
            game_state["mana_used"] -= self.cost
            game = {
                "Card_played": self.name,
                "Mana_used": self.cost,
                "Effect": "Creature summoned to battlefield"
            }
            game_state["battlefield"] += [self.name]
        else:
            game = {
                "Card_name": self.name,
                "Status": "not playable card"
            }
        return game

    def attack(self, target: Card) -> Dict:
        if self.damage > target.health:
            target.health = 0
            result = {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": target.health,
                "combat_resolved": True
            }
        else:
            target.health -= self.attack
            result = {
                "attacker": self.name,
                "target": target.name,
                "damage_dealt": self.attack,
                "combat_resolved": False
            }
        return result

    def calculate_rating(self) -> int:
        return random.randint(1100, 1200)

    def get_tournament_stats(self) -> Dict:
        return {
            "card name": self.name,
            "total wins": self.wins,
            "total losses": self.losses,
            "rating": self.rating
        }

    def defend(self, incoming_damage: int) -> Dict:
        damage = incoming_damage - self.defence_power
        if damage > 0:
            self.health -= damage
        result = {
            "defender": self.name,
            "damage_taken": (damage if damage > 0 else 0),
            "damage_blocked": (self.defence_power
                               if damage > 0 else incoming_damage),
            "still_alive": (self.health > 0)
        }
        return result

    def get_combat_stats(self) -> Dict:
        return {
            "card name": self.name,
            "card type": self.type,
            "rarity": self.rarity,
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "Interfaces": "[Card, Combatable, Rankable]",
            "Rating": self.rating,
            "Record": f"{self.wins}-{self.losses}"
        }
