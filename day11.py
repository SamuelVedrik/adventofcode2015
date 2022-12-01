from tqdm import tqdm

alphabet = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]
pairs = [f"{a}{a}" for a in alphabet]
consecutive_three = [f"{a}{b}{c}" for a, b, c in zip(alphabet, alphabet[1:], alphabet[2:])]

def increment(password):
    left = password[:-1]
    value = alphabet[(alphabet.index(password[-1]) + 1) % len(alphabet)]
    if value == "a":
        left = increment(left)
    return left + value

def check_valid(password):
    if "i" in password or "l" in password or "o" in password:
        return False
    if sum([pair in password for pair in pairs]) < 2:
        return False
    if all([pair not in password for pair in consecutive_three]):
        return False
    return True

if __name__ == "__main__":
    current = "hxbxwxba"
    with tqdm() as pbar:
        while not check_valid(current):
            current = increment(current)
            pbar.update(1)
    print(current)
    