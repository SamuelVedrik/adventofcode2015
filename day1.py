def load_inputs(path): 
    with open(path) as f:
        input_ = f.read()
    return input_

def part_one():
    inputs = load_inputs("inputs/day1.txt")
    print(sum((1 if i == "(" else -1) for i in list(inputs)))
    
def part_two():
    inputs = load_inputs("inputs/day1.txt")
    values = [(1 if i == "(" else -1) for i in list(inputs)]
    sum_ = 0
    for i, val in enumerate(values):
        sum_ += val
        if sum_ == -1:
            print(i+1)
            break

if __name__ == "__main__":
    part_one()
    part_two()
    
            
        

