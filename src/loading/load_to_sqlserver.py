import pandas as pd
import pyodbc

SILVER_FILE_PATH = "data/silver/german_credit_silver.parquet"
SERVER = r"localhost\SQLEXPRESS"
DATABASE = "CreditRiskDB"
TABLE_NAME = "german_credit"


def get_connection(database: str = DATABASE):
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connection_string)

def create_database_if_not_exists():
    conn = get_connection("master")
    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute(f"""
    IF DB_ID('{DATABASE}') IS NULL
        CREATE DATABASE {DATABASE};
    """)

    cursor.close()
    conn.close()

def create_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
    IF OBJECT_ID('{TABLE_NAME}', 'U') IS NULL
    CREATE TABLE {TABLE_NAME} (
        checking_account VARCHAR(100),
        duration INT,
        credit_history VARCHAR(100),
        purpose VARCHAR(100),
        credit_amount INT,
        savings_account VARCHAR(100),
        employment_since VARCHAR(100),
        installment_rate INT,
        personal_status_sex VARCHAR(100),
        other_debtors VARCHAR(100),
        residence_since INT,
        property VARCHAR(100),
        age INT,
        other_installment_plans VARCHAR(100),
        housing VARCHAR(100),
        existing_credits INT,
        job VARCHAR(100),
        num_dependents INT,
        telephone VARCHAR(100),
        foreign_worker VARCHAR(100),
        target VARCHAR(50)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def extract_silver_data(file_path: str) -> pd.DataFrame:
    df = pd.read_parquet(file_path)
    return df

def truncate_table(cursor) -> None:
    cursor.execute(f"DELETE FROM {TABLE_NAME};")

def load_data_to_sqlserver(df: pd.DataFrame) -> None:
    create_database_if_not_exists()
    create_table_if_not_exists()

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

    validate_load()

def validate_load():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    
    total_registros = cursor.fetchone()[0]

    print(f"Total de registros carregados no SQL Server: {total_registros}")
    
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