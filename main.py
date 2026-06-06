from src.ingestion.download_data import main as download_main
from src.processing.transform_data import main as transform_main
from src.processing.generate_gold import main as gold_main
from src.loading.load_to_sqlserver import main as load_main

def main():
    download_main()
    transform_main()
    gold_main()
    load_main()

if __name__ == "__main__":
    main()
