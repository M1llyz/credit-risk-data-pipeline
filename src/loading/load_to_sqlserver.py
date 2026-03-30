import pandas as pd
import pyodbc

SILVER_FILE_PATH = "data/silver/german_credit_silver.parquet"
SERVER = r"localhost\SQLEXPRESS"
DATABASE = "CreditRiskDB"
TABLE_NAME = "german_credit"


def get_connection():
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connection_string)


def extract_silver_data(file_path: str) -> pd.DataFrame:
    df = pd.read_parquet(file_path)
    return df


def truncate_table(cursor) -> None:
    cursor.execute(f"DELETE FROM {TABLE_NAME};")


def load_data_to_sqlserver(df: pd.DataFrame) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    truncate_table(cursor)

    insert_query = f"""
    INSERT INTO {TABLE_NAME} (
        checking_account,
        duration,
        credit_history,
        purpose,
        credit_amount,
        savings_account,
        employment_since,
        installment_rate,
        personal_status_sex,
        other_debtors,
        residence_since,
        property,
        age,
        other_installment_plans,
        housing,
        existing_credits,
        job,
        num_dependents,
        telephone,
        foreign_worker,
        target
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    for _, row in df.iterrows():
        cursor.execute(
            insert_query,
            row["checking_account"],
            int(row["duration"]),
            row["credit_history"],
            row["purpose"],
            int(row["credit_amount"]),
            row["savings_account"],
            row["employment_since"],
            int(row["installment_rate"]),
            row["personal_status_sex"],
            row["other_debtors"],
            int(row["residence_since"]),
            row["property"],
            int(row["age"]),
            row["other_installment_plans"],
            row["housing"],
            int(row["existing_credits"]),
            row["job"],
            int(row["num_dependents"]),
            row["telephone"],
            row["foreign_worker"],
            row["target"]
        )

    conn.commit()
    cursor.close()
    conn.close()


def main():
    print("Lendo dados da camada Silver...")
    df = extract_silver_data(SILVER_FILE_PATH)

    print(f"Total de linhas para carregar: {len(df)}")

    print("Carregando dados no SQL Server...")
    load_data_to_sqlserver(df)

    print("Carga concluída com sucesso.")


if __name__ == "__main__":
    main()