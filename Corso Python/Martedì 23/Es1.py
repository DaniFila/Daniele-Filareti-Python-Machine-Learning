import numpy as np


def main():
    arr = np.random.randint(1,1001,50)
    print(f"Array iniziale:\n{arr}")
    media = np.mean(arr)
    deviazione_standard = np.std(arr)
    print(f"Media: {media}\nDeviazione Standard: {deviazione_standard}")
    arr = arr.reshape(5,10)
    print(f"Array dopo Reshape:\n{arr}")



main()

