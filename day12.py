import json

def recursively_add(sub_json):
    if isinstance(sub_json, int):
        return sub_json
    if isinstance(sub_json, str):
        return 0
    if len(sub_json) == 0:
        return 0
    if isinstance(sub_json, list):
        return sum(recursively_add(item) for item in sub_json)
    if isinstance(sub_json, dict):
        return sum(recursively_add(item) for item in sub_json.values())
    
def recursively_add_ignore_red(sub_json):
    if isinstance(sub_json, int):
        return sub_json
    if isinstance(sub_json, str):
        return 0
    if len(sub_json) == 0:
        return 0
    if isinstance(sub_json, list):
        return sum(recursively_add_ignore_red(item) for item in sub_json)
    if isinstance(sub_json, dict):
        if "red" in sub_json.values():
            return 0
        return sum(recursively_add_ignore_red(item) for item in sub_json.values())


if __name__ == "__main__":
    with open("inputs/day12.txt") as f:
        inputs = json.load(f)
    
    print(recursively_add_ignore_red(inputs))
    