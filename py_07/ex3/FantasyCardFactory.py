from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory
from typing import Dict
from enum import Enum
import random


class Rarity(Enum):
    rarity = "Legendary"


class FantasyCardFactory(CardFactory):
    def create_creature(self,
                        name_or_power: str | int | None = None) -> Card:
        creatures = [
            ("Fire Dragon", 5, Rarity.rarity.value, 7, 5),
            ("Goblin Warrior", 2, "Common", 3, 2),
        ]
        if isinstance(name_or_power, str):
            for c in creatures:
                if name_or_power.lower() in c[0].lower():
                    return CreatureCard(*c)
        if isinstance(name_or_power, int):
            return CreatureCard("fire Dragon", name_or_power,
                                "Common", name_or_power, name_or_power)
        name, cost, rarity, attack, health = random.choice(creatures)
        return CreatureCard(name, cost, rarity, attack, health)

    def create_spell(self, name_or_power: str | None = None) -> Card:
        spells = [
            ("Fireball", 3, "Rare", "damage"),
            ("Curse", 2, "Uncommon", "debuff")
        ]
        if isinstance(name_or_power, str):
            for spell in spells:
                if name_or_power.lower() in spell[0].lower():
                    return SpellCard(*spell)
        if isinstance(name_or_power, int):
            return SpellCard("ice", name_or_power,
                             "Common", "heal")
        name, cost, rarity, effect_type = random.choice(spells)
        return SpellCard(name, cost, rarity, effect_type)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts = [
            ("Mana Ring", 2, "Rare", 3, "mana_boost"),
            ("Iron Shield", 1, "Common", 5, "defense")
        ]
        if isinstance(name_or_power, str):
            for artifact in artifacts:
                if name_or_power.lower() in artifact[0].lower():
                    return ArtifactCard(*artifact)
        if isinstance(name_or_power, int):
            return ArtifactCard("Custom Artifact", name_or_power,
                                "Common", 3, "generic")
        name, cost, rarity, durability, effect = random.choice(artifacts)
        return ArtifactCard(name, cost, rarity, durability, effect)

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }

    def create_themed_deck(self, size: int) -> Dict:
        spells = []
        creatures = []
        artifacts = []
        for i in range(size // 3):
            spells.append(self.create_spell())
            creatures.append(self.create_creature())
            artifacts.append(self.create_artifact())

        return {
            "total_cards": size,
            "spells": spells,
            "creatures": creatures,
            "artifacts": artifacts
        }
