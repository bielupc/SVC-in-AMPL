import numpy as np
import pandas as pd
from scipy.io.arff import loadarff 


def main() -> None:
    data = pd.DataFrame(loadarff('diabetes.arff')[0])
    data["class"] = data["class"].map({b'tested_positive': 1., b'tested_negative': -1.})
    data.to_csv('diabetes.dat', sep=' ', index=False, header=False)
    

if __name__ == "__main__":
    main()