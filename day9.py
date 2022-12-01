from collections import defaultdict
from itertools import permutations
from tqdm import tqdm

def parse_inputs(inputs):
    connections = defaultdict(lambda: float("inf"))
    nodes_set = []
    for input_ in inputs:
        nodes, value = input_.split(" = ")
        left, right = nodes.split(" to ")
        nodes_set.append(left)
        nodes_set.append(right)
        connections[left, right] = int(value)
        connections[right, left] = int(value)
        
    return connections, set(nodes_set)

def brute_force(connections, nodes):
    min_ = float("inf")
    for perm in tqdm(permutations(nodes)):
        cost = 0
        for left, right in zip(perm, perm[1:]):
            cost += connections[left, right]
        min_ = min(min_, cost)
    return min_

def brute_force2(connections, nodes):
    max_ = 0
    for perm in tqdm(permutations(nodes)):
        cost = 0
        for left, right in zip(perm, perm[1:]):
            cost += connections[left, right]
        max_ = max(max_, cost)
    return max_
    

if __name__ == "__main__":
    
    with open("inputs/day9.txt") as f:
        inputs = f.read()
        
    inputs = inputs.split("\n")
    connections, nodes = parse_inputs(inputs)
    print(brute_force2(connections, nodes))
    

    