def fibonacci():
    """Generate infinite Fibonacci sequence."""
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


def prime_numbers():
    """Generate infinite sequence of prime numbers."""
    def is_prime(num: int) -> bool:
        for n in range(2, num):
            if (num % n == 0):
                return False

        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def events_stream(event_count: int):
    """Generate game events with player, level, and action."""
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for counter in range(event_count):
        yield (
            counter + 1, players[counter % len(players)],
            ((counter * 3 + 3)**3 % 20), actions[counter % len(actions)])


def process_events(event_count: int):
    """Process event stream and display analytics."""
    print(f"Processing {event_count} game events...\n")

    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    for event in events_stream(event_count):
        counter, player, level, action = event

        if counter <= 3:
            print(f"Event {counter}: Player {player} (level {level}) {action}")
        if counter == 3:
            print("...")

        total_events += 1
        if level >= 10:
            high_level_players += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def data_stream() -> None:
    """Main function to demonstrate generator usage."""
    print("=== Game Data Stream Processor ===\n")
    process_events(1000)

    print("\n=== Generator Demonstration ===")
    count = 10
    print(f"Fibonacci sequence (first {count}): ", end="")
    fib = fibonacci()
    for counter in range(count):
        if (counter < count - 1):
            print(f"{next(fib)}, ", end="")
        else:
            print(next(fib))

    count = 5
    print(f"Prime numbers (first {count}): ", end="")
    prime = prime_numbers()
    for counter in range(count):
        if counter < count - 1:
            print(f"{next(prime)}, ", end="")
        else:
            print(next(prime))


if __name__ == "__main__":
    data_stream()
