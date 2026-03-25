import pandas as pd

FILE_PATH = "data/bronze/german.data"


def main():
    # le o arquivo
    df = pd.read_csv(FILE_PATH, sep=" ", header=None)

    print("\nPrimeiras linhas:")
    print(df.head())

    print("\nQuantidade de linhas e colunas:")
    print(df.shape)

    print("\nTipos de dados:")
    print(df.dtypes)


if __name__ == "__main__":
    main()