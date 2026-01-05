def list_comprehension() -> None:
    """Demonstrate list comprehensions for filtering and transforming."""
    print("\n=== List Comprehension Examples ===")

    scores = {"alice": 2300, "bob": 1800, "charlie": 2050, "diana": 2150}
    high_scores = [player for player, score in scores.items() if score >= 2000]
    print(f"High scorers (>2000): {high_scores}")

    scores_doubled = [scores[player] * 2 for player in scores]
    print(f"Scores doubled: {scores_doubled}")

    status = {"alice": "active", "bob": "active",
              "charlie": "active", "diana": "inactive"}
    active_players = [p for p, status in status.items() if status == "active"]
    print(f"Active players: {active_players}")


def dict_comprehension() -> None:
    """Demonstrate dict comprehensions for mapping."""
    print("\n=== Dict Comprehension Examples ===")

    players = [("alice", 2300, 5), ("bob", 1800, 3), ("charlie", 2150, 7)]
    players_scores = {player: score for player, score, _ in players}
    print(f"Player scores: {players_scores}")

    categories = [("high", 3), ("medium", 2), ("low", 1)]
    category_scores = {category: score for category, score in categories}
    print(f"Score categories: {category_scores}")

    players_achievements_count = {
        player: achievements for player, _, achievements in players}
    print(f"Achievement counts: {players_achievements_count}")


def set_comprehension() -> None:
    """Demonstrate set comprehensions for unique value extraction."""
    print("\n=== Set Comprehension Examples ===")

    players = ["alice", "bob", "charlie", "diana", "bob", "charlie", "alice"]
    unique_players = {player for player in players}
    print(f"Unique players: {unique_players}")

    achievements = ["first_kill", "level_10", "boss_slayer", "level_10"]
    unique_achievements = {achievement for achievement in achievements}
    print(f"Unique achievements: {unique_achievements}")

    regions = {"north": "active", "east": "active",
               "central": "active", "south": "inactive"}
    active_regions = {
        region for region in regions if regions[region] == "active"}
    print(f"Active regions: {active_regions}")


def combined_analytics() -> None:
    """Combine comprehensions"""
    print("\n=== Combined Analysis ===")
    players = {
        "alice": {
            "score": 2500,
            "achievements": ['first_kill', 'level_10', 'boss_slayer']
        },
        "bob": {
            "score": 1800,
            "achievements": ['first_kill', 'level_15', 'boss_slayer']
        },
        "dianna": {
            "score": 2300,
            "achievements": ['first_kill', 'level_19', 'boss_slayer']
        }
    }

    print(f"Total players: {len(players)}")
    total_unique_achievements = {
        achievement for player in players
        for achievement in players[player]["achievements"]}

    print(f"Total unique achievements: {len(total_unique_achievements)}")
    scores = [player["score"] for player in players.values()]
    print(f"Average score: {sum(scores) / len(scores)}")
    max_score = max(scores)
    for player in players:
        if players[player]["score"] == max_score:
            top_performer = player
    performer_score = players[top_performer]["score"]
    performer_achievements_count = len(players[top_performer]["achievements"])
    print(f"Top performer: {top_performer} ({performer_score} points,"
          f" {performer_achievements_count} achievements)")


def analytics_dashboard() -> None:
    """Main function to run all comprehension demonstrations"""
    print("=== Game Analytics Dashboard ===")
    list_comprehension()
    dict_comprehension()
    set_comprehension()
    combined_analytics()


if __name__ == "__main__":
    analytics_dashboard()
