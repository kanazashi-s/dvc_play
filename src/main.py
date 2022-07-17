import csv


def load_data(X_path, y_path):
    with open(X_path) as input_file:
        csv_reader = csv.reader(input_file, quoting=csv.QUOTE_NONNUMERIC)
        X = list(csv_reader)

    with open(y_path) as input_file:
        csv_reader = csv.reader(input_file, quoting=csv.QUOTE_NONNUMERIC)
        y = [row[0] for row in csv_reader]

    return X, y


def main():
    X, y = load_data("../data/digit_data.csv", "../data/digit_target.csv")
    print(X)


if __name__ == '__main__':
    main()