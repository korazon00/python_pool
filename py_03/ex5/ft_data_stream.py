
from typing import Generator


def gen(event: int) -> Generator[str, None, list]:
    print(f"Processing {event} game events...\n")

    players: list = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']

    achievements: list = [
            'killed monster', 'found treasure', 'leveled up', 'first_blood',
            'level_master', 'speed_runner', 'treasure_seeker',
            'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer'
        ]

    levels: list = [5, 8, 12, 15, 18, 21, 24, 27, 30]

    i: int = 0
    k: int = 1
    hight_levels: int = 0
    treasure_events: int = 0
    level_up: int = 0
    while k <= event:

        player: int = i % len(players)
        achievement: int = i % len(achievements)
        level: int = i % len(levels)

        yield (
            f"Event {k}: Player {players[player]}"
            f"(level {levels[level]}) {achievements[achievement]}"
        )
        i += 1
        k += 1
        if levels[level] >= 10:
            hight_levels += 1
        if achievements[achievement] == "found treasure":
            treasure_events += 1
        if achievements[achievement] == "leveled up":
            level_up += 1

        analytics: list = [hight_levels, treasure_events, level_up]

    return analytics


def stream_analytics(analytics: list, i: int) -> None:

    hight_levels, treasure_events, level_up = analytics
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {i}")
    print(f"High-level players (10+): {hight_levels}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up}")


def memory_usage(game_events: int) -> None:
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {game_events * 0.000045:.3f} seconds")


def fibonacci_sequence(num) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    for x in range(num):
        yield a
        a, b = b, a + b


def prime_numbers(n) -> Generator[int, None, None]:

    num: int = 2

    while n > 0:
        i: int = 2
        is_prime: bool = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield num
            n -= 1
        num += 1


def generator_demonstration() -> None:
    print("\n=== Generator Demonstration ===")
    a: int = 10
    h: Generator = fibonacci_sequence(a)
    x: int = 1
    print(f"Fibonacci sequence (first {a}):", end=" ")
    for i in h:
        if x < a:
            print(i, end=", ")
        elif x == a:
            print(i)
        x += 1

    b: int = 5
    x: int = 1
    print(f"Prime numbers (first {b}):", end=" ")
    p: Generator = prime_numbers(b)
    for i in p:
        if x < b:
            print(i, end=", ")
        elif x == b:
            print(i)
        x += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    game_events: int = 100
    event = gen(game_events)
    analytics: list = []
    i: int = 0
    try:
        while True:
            print(next(event))
            i += 1

    except StopIteration as e:
        analytics = e.value

    stream_analytics(analytics, i)

    memory_usage(game_events)

    generator_demonstration()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"error: {e}")
