import re

tape = {
    "children": 3,
    "cats": 7,
    "pomeranians": 3,
    "samoyeds": 2,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}
def parse_inputs(inputs):
    sues = []
    for item in inputs:
        item = re.sub(r"Sue \d+: ", "", item)
        vals = item.split(", ")
        val_dict = {}
        for kv_pairs in vals:
            key, val = kv_pairs.split(": ")
            val_dict[key] = int(val)
        sues.append(val_dict)
    return sues

def part1_check(sue):
    return all(tape[key] == val for key, val in sue.items())

def part2_check(sue):
    if "cats" in sue and sue["cats"] <= tape["cats"]:
        return False
    if "trees" in sue and sue["trees"] <= tape["trees"]:
        return False
    if "pomeranians" in sue and sue["pomeranians"] >= tape["pomeranians"]:
        return False
    if "goldfish" in sue and sue["goldfish"] >= tape["goldfish"]:
        return False
    return all(tape[key] == val for key, val in sue.items() if key not in {"cats", "trees", "pomeranians", "goldfish"})
        
if __name__ == "__main__":
    with open("inputs/day16.txt") as f:
        inputs = f.read().splitlines()
    
    sues = parse_inputs(inputs)
    for i, sue in enumerate(sues):
        if part2_check(sue):
            print(i+1)
            break
