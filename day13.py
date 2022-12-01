from itertools import permutations
from tqdm import tqdm

def calculate_happiness(connections, guest_order):
    return sum(connections[left, right] + connections[right, left] for left, right in zip(guest_order, guest_order[1:]))

def parse_inputs():
    with open("inputs/day13.txt") as f:
        inputs = f.read().splitlines()
    connections = {}
    guests = []
    for input in inputs:
        input = input.replace("would ", "")
        input = input.replace("happiness units by sitting next to ", "")
        input = input.replace(".", "")
        left, sign, num, right = input.split(" ")
        if sign == "gain":
            connections[left, right] = int(num)
        elif sign == "lose":
            connections[left, right] = -int(num)
        else:
            raise ValueError("Invalid Sign")
        guests.append(left)
        guests.append(right)
        
    return connections, set(guests)

def update_connections(connections, guests):
    for guest in guests:
        connections["hahamelol", guest] = 0
        connections[guest, "hahamelol"] = 0

if __name__ == "__main__":
    
    connections, guests = parse_inputs()
    update_connections(connections, guests)
    guests = guests.union({"hahamelol"})
    max_ = 0
    for perm in tqdm(permutations(guests)):
        perm = perm + perm[0:1]
        max_ = max(max_, calculate_happiness(connections, perm))
    print(max_)
    