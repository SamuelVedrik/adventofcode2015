import math

def parse_input():
    with open('inputs/day14.txt') as f:
        inputs = f.read().splitlines()
    descs = []
    for input in inputs:
        var = input.split(" ")
        # char, flight, seconds, rest
        descs.append((var[0], int(var[3]), int(var[6]), int(var[-2])))
    return descs

def calculate_distance(flight, flight_time, rest, total_time):
    per_flight = flight_time + rest
    complete_sprints = math.floor(total_time / per_flight) * (flight * flight_time)
    left_over =  (total_time % per_flight)
    left_over_dist = min(flight * flight_time, left_over * flight)

    return complete_sprints + left_over_dist

def part1():
    descs = parse_input()
    total_time = 2503
    dists = [calculate_distance(flight, flight_time, rest, total_time) for char, flight, flight_time, rest in descs]
    print(max(dists))

def is_going(flight_time, rest, current_time):
    remainder = current_time % (rest + flight_time)
    return remainder < flight_time

if __name__ == "__main__":
    descs = parse_input()
    distance = {char: 0 for char, *_ in descs}
    points = {char: 0 for char, *_ in descs}
    for i in range(2503):
        for char, flight, flight_time, rest in descs:
            if is_going(flight_time, rest, i):
                distance[char] += flight
        lead = []
        for char, dist in distance.items():
            if all(dist > distance[other] for other in lead) or len(lead) == 0:
                lead = [char]
            elif dist == distance[lead[0]]:
                lead.append(char)
        for char in lead:
            points[char] += 1
    
    print(max(points.values()))
            
    
    