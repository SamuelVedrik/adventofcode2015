from collections import defaultdict

def load_inputs(path): 
    with open(path) as f:
        inputs = f.read()
    return inputs

def part_one():
    inputs = load_inputs("inputs/day3.txt")
    houses = defaultdict(int)
    houses[0, 0] = 1
    starti, startj = 0, 0
    for char in inputs:
        if char == "<": 
            starti -= 1
        elif char == ">": 
            starti += 1
        elif char == "v":
            startj -= 1
        elif char == "^": 
            startj += 1
        houses[starti, startj] += 1
    
    print(len(houses))

if __name__ == "__main__":
    inputs = load_inputs("inputs/day3.txt")
    houses_s = defaultdict(int)
    houses_r = defaultdict(int)
    houses_s[0, 0] = 1
    houses_r[0, 0] = 1
    
    sstarti, sstartj = 0, 0
    rstarti, rstartj = 0, 0
    for i, char in enumerate(inputs):
        if i % 2 == 0:
            if char == "<": 
                sstarti -= 1
            elif char == ">": 
                sstarti += 1
            elif char == "v":
                sstartj -= 1
            elif char == "^": 
                sstartj += 1
            houses_s[sstarti, sstartj] += 1
        else:
            if char == "<": 
                rstarti -= 1
            elif char == ">": 
                rstarti += 1
            elif char == "v":
                rstartj -= 1
            elif char == "^": 
                rstartj += 1
            houses_r[rstarti, rstartj] += 1
            
    print(len(set(houses_r.keys()) | set(houses_s.keys())))
    