def achievement_tracker() -> None:
    """Analyze achievements across multiple players using set operations"""
    print("=== Achievement Tracker System ===")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    print(f"\nPlayer alice achievements: {alice}")

    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    print(f"Player bob achievements: {bob}")

    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    unique_achievements = set.union(alice, bob, charlie)
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")

    common_achievements = set.intersection(alice, bob, charlie)
    print(f"\nCommon to all players: {common_achievements}")

    alice_unique_achievements = alice.difference(bob).difference(charlie)
    bob_unique_achievements = bob.difference(alice).difference(charlie)
    charlie_unique_achievements = charlie.difference(alice).difference(bob)

    rare_achievements = set.union(
                        alice_unique_achievements,
                        bob_unique_achievements, charlie_unique_achievements
                        )
    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_vs_bob_common = set.intersection(alice, bob)
    print(f"\nAlice vs Bob common: {alice_vs_bob_common}")

    alice_vs_bob_unique = set.difference(alice, bob)
    print(f"Alice unique: {alice_vs_bob_unique}")

    bob_vs_alice_unique = set.difference(bob, alice)
    print(f"Bob unique: {bob_vs_alice_unique}")


if __name__ == "__main__":
    achievement_tracker()
