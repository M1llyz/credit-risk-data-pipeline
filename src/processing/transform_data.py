import os
import pandas as pd

from mappings import (
    checking_account_map,
    credit_history_map,
    purpose_map,
    savings_account_map,
    employment_since_map,
    personal_status_sex_map,
    other_debtors_map,
    property_map,
    housing_map,
    job_map,
    target_map,
    other_installment_plans_map,
    telephone_map,
    foreign_worker_map
)

BRONZE_FILE_PATH = "data/bronze/german.data"
SILVER_DIR = "data/silver"
SILVER_FILE_PATH = "data/silver/german_credit_silver.parquet"

COLUMN_NAMES = [
    "checking_account",
    "duration",
    "credit_history",
    "purpose",
    "credit_amount",
    "savings_account",
    "employment_since",
    "installment_rate",
    "personal_status_sex",
    "other_debtors",
    "residence_since",
    "property",
    "age",
    "other_installment_plans",
    "housing",
    "existing_credits",
    "job",
    "num_dependents",
    "telephone",
    "foreign_worker",
    "target"
]


def extract_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep=" ", header=None)
    df.columns = COLUMN_NAMES
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["checking_account"] = df["checking_account"].map(checking_account_map)
    df["credit_history"] = df["credit_history"].map(credit_history_map)
    df["purpose"] = df["purpose"].map(purpose_map)
    df["savings_account"] = df["savings_account"].map(savings_account_map)
    df["employment_since"] = df["employment_since"].map(employment_since_map)
    df["personal_status_sex"] = df["personal_status_sex"].map(personal_status_sex_map)
    df["other_debtors"] = df["other_debtors"].map(other_debtors_map)
    df["property"] = df["property"].map(property_map)
    df["housing"] = df["housing"].map(housing_map)
    df["job"] = df["job"].map(job_map)
    df["target"] = df["target"].map(target_map)
    df["other_installment_plans"] = df["other_installment_plans"].map(other_installment_plans_map)
    df["telephone"] = df["telephone"].map(telephone_map)
    df["foreign_worker"] = df["foreign_worker"].map(foreign_worker_map)

    return df

def validate_data(df: pd.DataFrame) -> None:
    print("\nIniciando validação dos dados...")

    print("\n1. Verificando dimensões do dataset:")
    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")

    print("\n2. Verificando valores nulos por coluna:")
    print(df.isnull().sum())

    print("\n3. Verificando tipos de dados:")
    print(df.dtypes)

    print("\n4. Verificando se ainda existem códigos do tipo A:")

    columns_to_check = [
        "checking_account",
        "credit_history",
        "purpose",
        "savings_account",
        "employment_since",
        "personal_status_sex",
        "other_debtors",
        "property",
        "housing",
        "job",
        "other_installment_plans",
        "telephone",
        "foreign_worker"
    ]

    for column in columns_to_check:
        remaining_codes = df[column].astype(str).str.startswith("A").sum()
        print(f"{column}: {remaining_codes} valores ainda codificados")

    print("\nValidação concluída.")


def load_silver_data(df: pd.DataFrame, output_path: str) -> None:
    os.makedirs(SILVER_DIR, exist_ok=True)
    df.to_parquet(output_path, index=False)


def main():
    print("Lendo dados da camada Bronze...")
    df_bronze = extract_data(BRONZE_FILE_PATH)

    print("Transformando dados...")
    df_silver = transform_data(df_bronze)

    print("Visualizando resultado...")
    print(df_silver.head())

    validate_data(df_silver)

    print("\nSalvando dados na camada Silver...")
    load_silver_data(df_silver, SILVER_FILE_PATH)

    print(f"Arquivo salvo com sucesso em: {SILVER_FILE_PATH}")

if __name__ == "__main__":
    main()
    