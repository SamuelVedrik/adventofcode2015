from collections import defaultdict
import heapq
from tqdm import tqdm
from random import shuffle
from itertools import permutations

ORI_STRING = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
# ORI_STRING = "HOHOHO"

def parse_inputs(inputs):
    replacements = []
    for item in inputs:
        key, val = item.split(" => ")
        replacements.append((key, val))
    return replacements

def get_all_molecules(string, replacements):
    molecules = set()
    for key, val in replacements:
        for i in range(len(string)):
            new_str = string[:i] + string[i:].replace(key, val, 1)
            molecules.add(new_str)
    molecules.remove(string)
    return molecules


def part_one():
    with open("inputs/day19.txt") as f:
        inputs = f.read().splitlines()
    replacements = parse_inputs(inputs)
    molecules = get_all_molecules(ORI_STRING, replacements)
    print(len(molecules))


# TAKES TOO LONG :(
    
def bfs(start, replacements, end):
    heap = []
    node_costs = defaultdict(lambda: float("inf"))
    heapq.heappush(heap, (0, start))
    with tqdm() as pbar:
        while heap:
            pbar.update(1)
            curr_cost, current = heapq.heappop(heap)
            if curr_cost > node_costs[current]:
                print("skipping")
                continue
            if current == end:
                return curr_cost
            new_nodes = get_all_molecules(current, replacements)
            for item in new_nodes:
                if curr_cost + 1 < node_costs[item]:
                    heapq.heappush(heap, (curr_cost + 1, item))
                    node_costs[item] = curr_cost + 1
                    
def probabilistic_guessing(start, replacements, end):
    
    target = start
    part2 = 0

    with tqdm() as pbar:
        while target != end:
            tmp = target
            for a, b in replacements:
                if a not in target:
                    continue

                target = target.replace(a, b, 1)
                part2 += 1
            
            if tmp == target:
                target = start
                part2 = 0
                shuffle(replacements)
            pbar.update(1)

    return part2
         
if __name__ == "__main__":
    with open("inputs/day19.txt") as f:
        inputs = f.read().splitlines()
    replacements = parse_inputs(inputs)
    replacements_r = [(val, key) for key, val in replacements]
    # print(bfs(ORI_STRING, replacements_r, "e"))
    print(probabilistic_guessing(ORI_STRING, replacements_r, "e"))

        
    
    
    