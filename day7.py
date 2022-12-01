from copy import deepcopy

def parse_input(inputs):
    parsed_input = []
    for input_ in inputs:
        operation, variable = input_.strip().split(" -> ")
        operation = operation.split(" ")
        parsed_input.append((operation, variable))
    return parsed_input

def check_value(variable, values):
    if not(variable.isnumeric() or variable in values):
        return None
    return int(variable) if variable.isnumeric() else values[variable]
    

def parse_assignment(new_value, variable, values):
    value = check_value(new_value, values)
    if value is None:
        return False
    values[variable] = value
    return True

def parse_not(new_value, variable, values):
    value = check_value(new_value, values)
    if value is None:
        return False
    values[variable] = ~value
    return True

def parse_bitwise(operation, variable, values):
    lop, op, rop = operation
    if not (lop in values and rop in values) and not (lop in values and rop.isnumeric()) and not (lop.isnumeric() and rop in values):
        return False
    lop = int(lop) if lop.isnumeric() else values[lop]
    rop = int(rop) if rop.isnumeric() else values[rop]
    if op == "AND":
        values[variable] = lop & rop
    if op == "RSHIFT":
        values[variable] = lop >> rop
    if op == "LSHIFT":
        values[variable] = lop << rop
    if op == "OR":
        values[variable] = lop | rop
    return True
    
        
def parse_operation(operation, variable, values):
    if len(operation) == 1:
       return parse_assignment(operation[0], variable, values)
    
    if len(operation) == 2: # NOT
        return parse_not(operation[1], variable, values)
        
    if len(operation) == 3:
        return parse_bitwise(operation, variable, values)
    
if __name__ == "__main__":
    with open("inputs/day7.txt") as f:
        inputs = f.readlines()
    inputs = parse_input(inputs)
    unperformed_commands = deepcopy(inputs)
    values = {}
    while len(unperformed_commands) != 0:
        current_unperformed_commands = []
        for operation, variable in unperformed_commands:
            success = parse_operation(operation, variable, values)
            if not success:
                current_unperformed_commands.append((operation, variable))
        unperformed_commands = current_unperformed_commands
        # print(len(unperformed_commands))
        
    print(values["a"])
            
        
        

    
    