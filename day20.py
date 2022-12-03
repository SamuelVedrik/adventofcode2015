import numpy as np
from functools import reduce
from tqdm import tqdm

def get_factors(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if not n % i)))

    
def part1():
    for i in tqdm(range(500000, 8000000)):
        if sum(get_factors(i)) > 3600000:
            print(i)
            break
        
def condition(x):
    factors = get_factors(x)
    factors = set(fct for fct in factors if fct * 50 >= x)
    return sum(factors) > (36000000 / 11)

def part2():
    l = 831600
    r = 1250004
    for i in tqdm(range(l , r)):
        if condition(i):
            print(i)
            factors = get_factors(i)
            print(set(fct for fct in factors if fct * 50 >= i))
            break
        
        
    
    
    
if __name__ == '__main__':
    #1,750,000 - 1,750,000
    print(part2())
