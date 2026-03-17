from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:

    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    strategy = AggressiveStrategy()
    factory = FantasyCardFactory()

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    turn_dict = engine.simulate_turn()

    hand_display = [f"{c.name} ({c.cost})" for c in turn_dict["hand"]]
    print(f"Hand: [{', '.join(hand_display)}]")

    print("\nTurn execution:")
    turn_results = turn_dict["turn_result"]
    print("Strategy:", engine.strategy.get_strategy_name())
    print("Actions:", turn_results)

    print("\nGame Report:", engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum"
          " flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
