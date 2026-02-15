
players: dict = {

    "alice": {
        "score": 2300,
        "status": "active",
        "achievements": ['first_blood', 'level_master', 'speed_runner',
                         'treasure_seeker', 'boss_hunter'],
        "region": "north"
    },

    "bob": {
        "score": 1800,
        "status": "active",
        "achievements": ['first_blood', 'level_master', 'speed_runner'],
        "region": "central"
    },

    "charlie": {
        "score": 2150,
        "status": "active",
        "achievements": ['first_blood', 'level_master', 'speed_runner',
                         'treasure_seeker', 'boss_hunter', 'pixel_perfect',
                         'combo_king'],
        "region": "east"
    },

    "diana": {
        "score": 2050,
        "status": "inactive",
        "achievements": ['first_blood', 'level_master', 'speed_runner'],
        "region": "west"
    }
}


def list_comp(players: dict) -> None:
    print("=== List Comprehension Examples ===")

    hight_scores: list = [
        player
        for player in players
        if players[player]["score"] > 2000]
    scores_doubled: list = [players[player]["score"] * 2 for player in players]
    active_players: list = [
        player
        for player in players
        if players[player]["status"] == "active"]

    print(f"High scores: {hight_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


def dict_comp(players: dict) -> None:
    print("\n=== Dict Comprehension Examples ===")

    player_scores: dict = {
        player:
        players[player]["score"] for player in players}

    def score_categories(score: int) -> str:
        return (
            "high" if score > 2000 else
            "medium" if score > 1000 else
            "low"
        )
    score_categories: dict = {
        level: sum(1 for player in players
                   if score_categories(players[player]["score"]) == level)
        for level in ["high", "medium", "low"]
        }
    achievement_counts: dict = {player:
                                len(players[player]["achievements"])
                                for player in players}

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")


def set_comp(players: dict, flage: int) -> int:
    if flage == 1:
        print("\n=== Set Comprehension Examples ===")

    unique_players: set = {player for player in players}
    ach_list: list = []
    for player in players:
        for ach in players[player]["achievements"]:
            ach_list += [ach]

    unique_achievements: set = {ach for ach in ach_list}
    active_regions: set = {players[player]["region"]
                           for player in players
                           if players[player]["status"] == "active"}

    if flage == 1:
        print(f"Unique players: {unique_players}")
        print(f"Unique achievements: {unique_achievements}")
        print(f"Active regions: {active_regions}")

    len_unique_ach: int = len(unique_achievements)
    return (len_unique_ach)


def combined_analysis(players: dict) -> None:
    print("\n=== Combined Analysis ===")

    num_players: int = len(players)
    print(f"Total players: {num_players}")
    print(f"Total unique achievements: {set_comp(players, 0)}")

    average: int = sum(players[player]["score"] for player in players)
    print(f"Average score: {average / num_players}")

    scores: list = [players[player]["score"] for player in players]
    for player in players:
        if players[player]["score"] == max(scores):
            top_performer = player
    print(
        f"Top performer: {top_performer} ({players[top_performer]["score"]} "
        f"pionts, {len(players[top_performer]["achievements"])} achievements)")


if __name__ == "__main__":
    try:
        print("=== Game Analytics Dashboard ===\n")
        list_comp(players)
        dict_comp(players)
        set_comp(players, 1)
        combined_analysis(players)
    except Exception as e:
        print("Error: ", e)
