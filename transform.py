import sys
from typing import TypeAlias 

Point: TypeAlias = tuple[tuple[float, float, float, float], float]

def read_points(input_: str) -> list[Point]:
    points = []
    with open(input_, 'r') as file:
        for line in file:
            data = line.strip().split()
            features = tuple(float(x) for x in data[:-1])
            label = float(data[-1].replace('*', ''))
            points.append((features, label))
    return points


def write_ampl(output: str, points: list[Point]) -> None:
    with open(output, 'w') as file:
        file.write("\n")
        file.write("# Samples and dimension \n")
        file.write("param m := {};\n".format(len(points)))
        file.write("param n := {};\n".format(len(points[0][0])))
        file.write("\n")
        file.write("# Hyperparam\n")
        file.write("param nu := 30;\n")
        file.write("\n")
        file.write("# Points\n")
        file.write("param A : " + ' '.join(map(str, range(1, len(points[0][0]) + 1))) + " :=\n")
        for i, (features, label) in enumerate(points, start=1):
            file.write("{} {}\n".format(i, ' '.join(map(str, features))))
        file.write(";\n")
        file.write("\n")
        file.write("# Labels\n")
        file.write("param y :=\n")
        for i, (_, label) in enumerate(points, start=1):
            file.write("{} {}\n".format(i, label))
        file.write(";\n")


def write_normal(output: str, points: list[Point]) -> None:
    with open(output, 'w') as file:
        for features, label in points:
            file.write(' '.join(map(str, features)) + f" {label}\n")


def split_data(points: list[Point], test_ratio: float) -> tuple[list[Point], list[Point]]:
    split_index = int(len(points) * (1 - test_ratio))
    train_points = points[:split_index]
    test_points = points[split_index:]
    return train_points, test_points


def main(input_: str, output: str, test_ratio: float) -> None:
    points = read_points(input_)
    train_set, test_set = split_data(points, test_ratio)
    write_ampl(output+"_train_AMPL.dat", train_set)
    write_normal(output+"_train_PLAIN.dat", train_set)
    write_normal(output+"_test_PLAIN.dat", test_set)
    print("OK")
    

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("python transform.py input output_name test_ratio")
        sys.exit(1)
    
    input_= sys.argv[1]
    output= sys.argv[2]
    test_ratio = float(sys.argv[3])
    main(input_, output, test_ratio)