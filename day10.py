def next_iteration(item: str):
    str_build = ""
    current = item[0]
    count = 1
    for char in item[1:]:
        if char != current:
            str_build += f"{count}{current}"
            current = char
            count = 1
        else:
            count += 1
            
    str_build += f"{count}{current}"
    return str_build
        

if __name__ == "__main__":
    val = "1321131112"
    for i in range(50):
        val = next_iteration(val)
    print(len(val))