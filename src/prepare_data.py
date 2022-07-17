import os

import pandas as pd
from sklearn import datasets


if __name__ == '__main__':

    digits = datasets.load_digits()

    df = pd.DataFrame(digits.data)
    df.to_csv("../data/digit_data.csv", header=False, index=False)

    df = pd.DataFrame(digits.target)
    df.to_csv("../data/digit_target.csv", header=False, index=False)

