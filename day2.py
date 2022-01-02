import numpy as np

def load_inputs(path): 
    with open(path) as f:
        inputs = f.readlines()
    
    return [[int(val) for val in input_.strip().split("x") ]for input_ in inputs]

def part_one():
    inputs = load_inputs("inputs/day2.txt")
    inputs = np.array(inputs)
    first = (inputs[:, 0] * inputs[:, 1])
    second = (inputs[:, 0] * inputs[:, 2]) 
    third = (inputs[:, 1] * inputs[:, 2])
    
    mins = np.c_[first, second, third].min(axis=1)
    total = 2*(first + second + third) + mins
    print(total.sum())
    
def part_two():
    inputs = load_inputs("inputs/day2.txt")
    inputs = np.array(inputs)
    
    first = (2*inputs[:, 0]) + (2 *inputs[:, 1])
    second = (2* inputs[:, 0]) + (2* inputs[:, 2]) 
    third = (2* inputs[:, 1]) + (2*inputs[:, 2])
    
    ribbons = (inputs[:, 0] * inputs[:, 1] * inputs[:, 2])
    
    total = (np.c_[first, second, third]).min(axis=1) + ribbons
    print(total.sum())
    
    
if __name__ == "__main__": 
    part_one()
    part_two()