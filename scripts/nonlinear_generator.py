from sklearn.datasets import make_swiss_roll
import numpy as np
import matplotlib.pyplot as plt


FILENAME = "nonlinear.dat"

def save_dataset(points, labels, filename) -> None:
    assert len(points) == len(labels)

    with open(filename, "w") as file:
        for point, label in zip(points, labels):
            file.write(" ".join(map(str, point)) + " " + str(label) + "\n")


def generate_swiss(size=400):
    x, t = make_swiss_roll(n_samples=size, random_state=1234)
    labels = np.where(t < np.mean(t), 1, -1)    # values below mean of t are a class
    return x, labels


def plot_swiss(x, labels):
        # Crear la figura y el eje 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficar los puntos del dataset
    ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=labels, cmap=plt.cm.Spectral)

    # Añadir etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Mostrar el gráfico
    plt.show()


def main():
    inp = input("Enter size of dataset: ")
    if len(inp) == 0:
        x, labels = generate_swiss()
    else:
        x, labels = generate_swiss(int(inp))

    #plot_swiss(x, labels)
    save_dataset(x, labels, FILENAME)
        

if __name__ == "__main__":
    main()