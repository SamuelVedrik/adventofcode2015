from itertools import product, permutations
import math

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armors = [
    (0, 0, 0),
    (13, 0,  1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3)
]

boss_hp = 109
boss_attack = 8
boss_armor = 2

my_hp = 100

def calculate_turns_to_kil(enemy_hp, attack, enemy_armor):
    return math.ceil(enemy_hp / max((attack - enemy_armor), 1))
    

if __name__ == "__main__":
    
    max_ = 0
    for weapon, armor in product(weapons, armors):
        for ring1, ring2 in product(rings, rings):
            if ring1 == ring2:
                continue
            total_cost = weapon[0] + armor[0] + ring1[0] + ring2[0]
            total_attack = weapon[1] + ring1[1] + ring2[1]
            total_armor = armor[2] + ring1[2] + ring2[2]
            turns_to_kill = calculate_turns_to_kil(boss_hp, total_attack, boss_armor)
            turns_to_die = calculate_turns_to_kil(my_hp, boss_attack, total_armor)
            if turns_to_kill > turns_to_die:
                max_ = max(max_, total_cost)
    
    print(max_)