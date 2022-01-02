import hashlib
from tqdm.auto import tqdm

if __name__ == "__main__":
    input_ = "ckczppom"
    # input_ = "abcdef"
    num = 0
    with tqdm() as pbar:
        while True:
            test = input_ + str(num)
            hash_ = hashlib.md5(test.encode())
            hex_ = hash_.hexdigest()
            if hex_[:6] == "000000": 
                print(num)
                break
            num += 1
            pbar.update(1)