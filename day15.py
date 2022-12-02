import numpy as np

matrix = np.array([[5, -1, 0, 0, 5],
                   [-1, 3, 0, 0, 1],
                   [0, -1, 4, 0, 6], 
                   [-1, 0, 0, 2, 8]])


def get_combinations(sum_total):
    combs = [
        (i, j, k, sum_total-i-j-k)
        for i in range(0, sum_total)
        for j in range(0, sum_total - i)
        for k in range(0, sum_total - i - j)
    ]
    return np.array(combs)

def part1():
    combs = get_combinations(100)
    vals = (combs @ matrix[:, :4])
    vals[vals < 0] = 0
    vals = vals[(vals != 0).all(axis=1)]
    best = np.log(vals).sum(axis=1).max()
    print(np.exp(best))
    
def part2():
    combs = get_combinations(100)
    vals = (combs @ matrix)
    vals = vals[vals[:, 4] == 500][:, :4]
    vals[vals < 0] = 0
    vals = vals[(vals != 0).all(axis=1)]
    best = np.log(vals).sum(axis=1).max()
    print(np.exp(best))

if __name__ == "__main__":
    part1()
    part2()
    
