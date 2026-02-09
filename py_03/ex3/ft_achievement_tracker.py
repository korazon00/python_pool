

if __name__ == "__main__":

    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10',
               'treasure_hunter',
               'boss_slayer',
               'speed_demon',
               'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    set_tmp = alice.union(bob)
    set_tmp = set_tmp.union(charlie)

    print(f"All unique achievements: {set_tmp}")
    print(f"Total unique achievements: {len(set_tmp)}")

    set_tmp = alice.intersection(bob)
    set_tmp = set_tmp.intersection(charlie)

    print(f"\nCommon to all players: {set_tmp}")
    s1 = alice.difference(bob, charlie)
    s2 = bob.difference(alice, charlie)
    s3 = charlie.difference(alice, bob)

    set_tmp = s1.union(s2, s3)

    print(f"Rare achievements (1 player): {set_tmp}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
