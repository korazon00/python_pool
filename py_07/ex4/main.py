from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    tournament = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    fire_dragon = TournamentCard("Fire Dragon", 4,
                                 "Legendary", 8, 12, 5, "dragon_001")
    ice_wizard = TournamentCard("Ice_wizard", 4,
                                "Legendary", 7, 13, 6, "wizard_001")
    print(tournament.register_card(fire_dragon))
    print()
    print(tournament.register_card(ice_wizard))

    print("\nCreating tournament match...")
    print("Match result: ",
          tournament.create_match(fire_dragon.id, ice_wizard.id))

    print("\nTournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for leader in leaderboard:
        print(leader)

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
