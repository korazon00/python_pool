from typing import Dict


class GameEngine ():
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def get_engine_status(self) -> Dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }

    def simulate_turn(self) -> Dict:
        card_dict = self.factory.create_themed_deck(3)
        hand = (
            card_dict["spells"]
            + card_dict["creatures"]
            + card_dict["artifacts"]
        )
        self.cards_created += len(hand)

        strategy_dict = self.strategy.execute_turn(hand, [])
        self.turns_simulated += 1
        self.total_damage += strategy_dict["damage_dealt"]

        return {
            "hand": hand,
            "turn_result": strategy_dict,
            "engine_status": self.get_engine_status()
        }
