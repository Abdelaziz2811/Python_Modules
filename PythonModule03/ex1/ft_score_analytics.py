import sys


def process_scores() -> None:
    """Parse scores from arguments and display statistics."""
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return
    else:
        scores = []
        try:
            for arg in sys.argv[1:]:
                score = int(arg)
                scores.append(score)
        except Exception as e:
            print(f"Error: {e}")
            return

        total_players = len(scores)
        total_score = sum(scores)
        high_score = max(scores)
        low_scores = min(scores)
        range = high_score - low_scores

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score / total_players}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_scores}")
        print(f"Score range: {range}")


if __name__ == "__main__":
    process_scores()
