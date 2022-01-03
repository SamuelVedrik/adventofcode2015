import numpy as np
import re

def load_inputs(path): 
    with open(path) as f: 
        inputs = f.readlines()
    
    parsed = []
    digits = r"([\d]+,[\d]+)"
    for line in inputs:
        action = None
        if "on" in line: 
            action = "on"
        elif "toggle" in line: 
            action = "toggle"
        else: 
            action = "off"
        
        start, end = re.findall(digits, line)
        
        start = [int(x) for x in start.split(",")]
        end = [int(x) for x in end.split(",")]
        
        parsed.append((action, start, end))
    
    return parsed 

def action(grid, line): 
    action, tl, br = line
    x = np.arange(tl[0], br[0]+1)
    y = np.arange(tl[1], br[1]+1)
    xx, yy = np.meshgrid(x, y)
    
    ids = np.c_[xx.flatten(), yy.flatten()]
    grid = grid.copy()
    if action == "on": 
        grid[ids[:, 0], ids[:, 1]] = True
    elif action == "off":
        grid[ids[:, 0], ids[:, 1]] = False
    else:
        grid[ids[:, 0], ids[:, 1]] = ~grid[ids[:, 0], ids[:, 1]]
    return grid

def action_p2(grid, line): 
    action, tl, br = line
    x = np.arange(tl[0], br[0]+1)
    y = np.arange(tl[1], br[1]+1)
    xx, yy = np.meshgrid(x, y)
    
    ids = np.c_[xx.flatten(), yy.flatten()]
    grid = grid.copy()
    if action == "on": 
        grid[ids[:, 0], ids[:, 1]] += 1
    elif action == "off":
        vals = np.maximum(0, grid[ids[:, 0], ids[:, 1]] - 1)
        grid[ids[:, 0], ids[:, 1]] = vals
    else:
        grid[ids[:, 0], ids[:, 1]] += 2
    return grid

def part_one():
    grid = np.zeros((1000, 1000)).astype(bool)
    inputs = load_inputs("inputs/day6.txt")
    for line in inputs: 
        grid = action(grid, line)
    
    print(grid.sum())
    
def part_two():
    grid = np.zeros((1000, 1000))
    inputs = load_inputs("inputs/day6.txt")
    for line in inputs: 
        grid = action_p2(grid, line)
    
    print(grid.sum())
    
if __name__ == "__main__": 
    part_one()
    part_two()
        