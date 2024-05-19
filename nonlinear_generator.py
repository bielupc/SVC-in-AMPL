from sklearn.datasets import make_swiss_roll
import numpy as np


FILENAME = "nonlinear.dat"

def save_dataset(points, labels, filename) -> None:
    assert len(points) == len(labels)

    with open(filename, "w") as file:
        for point, label in zip(points, labels):
            file.write(" ".join(map(str, point)) + " " + str(label) + "\n")


def generate_swiss(size=400):
    x, t = make_swiss_roll(n_samples=size)
    labels = np.where(t < np.mean(t), 1, -1)    # values below mean of t are a class
    return x, labels


def main():
    inp = input("Enter size of dataset: ")
    if len(inp) == 0:
        x, labels = generate_swiss()
    else:
        x, labels = generate_swiss(int(inp))

    save_dataset(x, labels, FILENAME)
        

if __name__ == "__main__":
    main()