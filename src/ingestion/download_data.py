import os
import requests

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"

OUTPUT_DIR = "data/bronze"
OUTPUT_FILE = "german.data"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, OUTPUT_FILE)


def download_file(url: str, output_path: str) -> None:
    # fazendo o download do arquivo e salvando localmente
    response = requests.get(url, timeout=30)
    response.raise_for_status()  # erro se falhar

    with open(output_path, "wb") as file:
        file.write(response.content)


def main():
    # cria a pasta se não existir
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # chama o download
    download_file(URL, OUTPUT_PATH)

    print(f"Arquivo salvo em: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()