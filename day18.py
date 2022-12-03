import numpy as np 
from scipy.signal import correlate2d

def parse_inputs(inputs):
    parsed_inputs = []
    for item in inputs:
        item = item.replace(".", "0")
        item = item.replace("#", "1")
        parsed_input = list(map(int, list(item)))
        parsed_inputs.append(parsed_input)
    return parsed_inputs
    
def update_lights(inputs, neighbors_matrix):
    
    num_neighbors = correlate2d(inputs, neighbors_matrix, mode="same")
    new_inputs = np.zeros_like(inputs)
    new_inputs[((num_neighbors == 2) | (num_neighbors == 3)) & (inputs == 1)] = 1
    new_inputs[(num_neighbors == 3) & (inputs == 0)] = 1
    
    new_inputs[0, 0] = 1
    new_inputs[0, 99] = 1
    new_inputs[99, 0] = 1
    new_inputs[99, 99] = 1
    return new_inputs
    
if __name__ == "__main__":
    
    with open("inputs/day18.txt") as f:
        inputs = f.read().splitlines()
    
    inputs = np.array(parse_inputs(inputs))
    inputs[0, 0] = 1
    inputs[0, 99] = 1
    inputs[99, 0] = 1
    inputs[99, 99] = 1
    neighbors_matrix = np.array([[1, 1, 1],
                                 [1, 0, 1], 
                                 [1, 1, 1]])

    for i in range(100):
        inputs = update_lights(inputs, neighbors_matrix)
    
    print(inputs.sum())