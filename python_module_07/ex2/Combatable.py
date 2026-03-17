from abc import ABC, abstractmethod
from typing import Dict


class Combatable(ABC):

    def attack(self, target) -> Dict:
        pass
    attack = abstractmethod(attack)

    def defend(self, incoming_damage: int) -> Dict:
        pass
    defend = abstractmethod(defend)

    def get_combat_stats(self) -> Dict:
        pass
    get_combat_stats = abstractmethod(get_combat_stats)
