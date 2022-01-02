import re

first_rule = r".*[aeiou].*[aeiou].*[aeiou].*"
second_rule = r".*([a-z])(\1).*"
third_rule_r = r".*(ab|cd|pq|xy).*"


p2_first = r".*([a-z]{2}).*(\1).*"
p2_second = r".*([a-z])[a-z](\1).*"

def load_inputs(path): 
    with open(path) as f:
        inputs = f.readlines()
    return inputs

def check_nice(string):
    match1 = re.match(first_rule, string) is not None
    match2 = re.match(second_rule, string) is not None
    match3 = re.match(third_rule_r, string) is None
    
    return match1 and match2 and match3

def check_nicep2(string): 
    match1 = re.match(p2_first, string) is not None
    match2 = re.match(p2_second, string) is not None
    
    return match1 and match2 

if __name__ == "__main__":
    
    inputs = load_inputs("inputs/day5.txt")
    num_nice = 0
    for input_ in inputs:
        if check_nicep2(input_):
            num_nice += 1
    
    print(num_nice)
    
    
    