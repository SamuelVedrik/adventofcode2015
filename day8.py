def part1():
    with open("inputs/day8.txt") as f:
        inputs = f.read()
        inputs = inputs.split("\n")
    
    total_code = 0
    total_mem = 0
    for input_ in inputs:
        total_code += len(input_)
        total_mem += len(eval(input_))
    
    print(total_code - total_mem)
    
def part2():
    with open("inputs/day8.txt") as f:
        inputs = f.read()
        inputs = inputs.split("\n")
    
    total_code = 0
    total_encode = 0
    for input_ in inputs:
        total_code += len(input_)
        input_ = input_.replace('"', '*"')
        input_ = input_.replace("\\", "*\\")
        total_encode += len(input_) + 2
    print(total_encode - total_code)

if __name__ == "__main__":
    part1()
    part2()