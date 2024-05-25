import pandas as pd
import numpy as np
import sys
import os


def split (input_file: str) -> None:
    data = pd.read_csv(input_file, sep=" ", header=None)

    total_size = len(data)
    sizes = {
        'L': int(0.75 * total_size),
        'M': int(0.5 * total_size),
        'S': int(0.25 * total_size)
    }
    print("XL", total_size)

    data_shuffled = data.sample(frac=1, random_state=42).reset_index(drop=True)

    for fraction, size in sizes.items():
        fraction_data = data_shuffled.iloc[:size]

        fraction_file_name = f"{os.path.splitext(input_file)[0]}_{fraction}.dat"
        fraction_data.to_csv(fraction_file_name, sep=" ", index=False, header=False)
        print(fraction, size)

def main() -> None:
    if len(sys.argv) != 2:
        print("python split_data.py input_file.dat")
        sys.exit(1)
    input_file = sys.argv[1]
    split(input_file)

if __name__ == "__main__":
    main()