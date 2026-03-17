
import sys

arguments: int = len(sys.argv)

print("=== Player Score Analytics ===")

if arguments < 2:
    print("No scores provided. Usage: python3", end=" ")
    print("ft_score_analytics.py <score1> <score2> ...")
else:
    scores: list = []
    try:
        x = 1
        while x < arguments:
            scores += [int(sys.argv[x])]
            x += 1

        print(f"Scores processed: {scores}")

        total = sum(scores)
        max = max(scores)
        min = min(scores)

        print(f"Total players: {arguments - 1}")
        print(f"Total score: {total}")
        print(f"Average score: {total / (arguments - 1)}")
        print(f"High score: {max}")
        print(f"Low score: {min}")
        print(f"Score range: {max - min}\n")

    except ValueError:
        print(f"sorry, the {sys.argv[x]} is invalide score")

    except Exception as e:
        print(e)
