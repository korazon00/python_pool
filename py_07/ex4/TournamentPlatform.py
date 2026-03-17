from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self):
        self.match_played = 0
        self.card_registred = []

    def register_card(self, card: TournamentCard) -> str:
        self.card_registred += [card]
        return (f"{card.name} (ID: {card.id}):\n"
                f"- Interfaces: [Card, Combatable, Rankable]\n"
                f"- Rating: {card.rating}\n"
                f"- Record: {card.wins}-{card.losses}")

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self. match_played += 1
        list1 = [c for c in self.card_registred if c.id == card1_id]
        list2 = [c for c in self.card_registred if c.id == card2_id]
        if list1 and list2:
            card1 = list1[0]
            card2 = list2[0]
            if card1.rating > card2.rating:
                winner = card1
                loser = card2
            else:
                winner = card2
                loser = card1
        else:
            raise ValueError("invalide cards")
        winner.rating += 16
        winner.wins += 1
        loser.rating -= 16
        loser.losses += 1
        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        leaderboard = []
        added = []
        leader = None
        n = 1
        while len(leaderboard) < len(self.card_registred):
            for card in self.card_registred:
                if card not in added:
                    if not leader or leader.rating < card.rating:
                        leader = card
            added += [leader]
            leaderboard += [f"{n}. {leader.name} "
                            f"- Rating: {leader.rating} "
                            f"({leader.wins}-{leader.losses})"]
            leader = None
            n += 1
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating = sum([c.rating for c in self.card_registred])
        return {
            "total_cards": len(self.card_registred),
            "matches_played": self.match_played,
            "avg_rating": total_rating // len(self.card_registred),
            "platform_status": "active"
        }
