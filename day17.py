import numpy as np

def convert_ints_to_binary(ints, max_bits):
    int_matrix = (((ints[:,None] & (1 << np.arange(max_bits)[::-1]))) > 0).astype(int)
    return int_matrix

if __name__ == "__main__":
    with open("inputs/day17.txt") as f:
        inputs = f.read().splitlines()
        inputs = [int(item) for item in inputs]
    
    input_vector = np.array(inputs).reshape(-1, 1)
    target = 150
    num_bits = len(inputs)
    vals = convert_ints_to_binary(np.arange(2**(len(inputs))), num_bits)
    valid_combinations = ((vals @ input_vector) == target).reshape(-1)
    print("part 1: ", valid_combinations.sum())
    
    min_amount = vals[valid_combinations].sum(axis=1).min()
    print((vals[valid_combinations].sum(axis=1) == min_amount).sum())
    