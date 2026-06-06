import os
import pandas as pd

SILVER_FILE_PATH = "data/silver/german_credit_silver.parquet"

GOLD_DIR = "data/gold"

GOLD_FILE_PATH = "data/gold/credit_risk_summary.parquet"

PURPOSE_RISK_FILE_PATH = "data/gold/purpose_risk_summary.parquet"

AGE_RISK_FILE_PATH = "data/gold/age_risk_summary.parquet"

def extract_silver_data(file_path: str) -> pd.DataFrame:
    df = pd.read_parquet(file_path)
    return df

def generate_credit_risk_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("target")
        .size()
        .reset_index(name="quantidade")
    )

    summary["percentual"] = (
        summary["quantidade"] / summary["quantidade"].sum()
    ) * 100

    return summary

def generate_purpose_risk_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["purpose", "target"])
        .size()
        .reset_index(name="quantidade")
    )

    summary["percentual"] = (
        summary["quantidade"] /
        summary.groupby("purpose")["quantidade"].transform("sum")
    ) * 100

    return summary

def generate_age_risk_summary(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 25, 35, 45, 55, 100],
        labels=["até 25", "26-35", "36-45", "46-55", "56+"]
    )

    summary = (
        df.groupby(["age_group", "target"], observed=True)
        .size()
        .reset_index(name="quantidade")
    )

    summary["percentual"] = (
        summary["quantidade"] /
        summary.groupby("age_group")["quantidade"].transform("sum")
    ) * 100

    return summary

def save_gold_data(df: pd.DataFrame, file_path: str) -> None:
    os.makedirs(GOLD_DIR, exist_ok=True)
    df.to_parquet(file_path, index=False)



def main():
    print("Lendo dados da camada Silver...")
    df_silver = extract_silver_data(SILVER_FILE_PATH)

    print("Gerando resumo da camada Gold...")
    df_gold = generate_credit_risk_summary(df_silver)

    df_purpose_risk = generate_purpose_risk_summary(df_silver)

    df_age_risk = generate_age_risk_summary(df_silver)

    print("\nResumo por finalidade do empréstimo:")
    print(df_purpose_risk.head(20))

    print("\nResumo por faixa etária:")
    print(df_age_risk)

    print(df_gold)

    print("Salvando dados na camada Gold...")
    save_gold_data(df_gold, GOLD_FILE_PATH)
    save_gold_data(df_purpose_risk, PURPOSE_RISK_FILE_PATH)
    save_gold_data(df_age_risk, AGE_RISK_FILE_PATH)

    print(f"Arquivo salvo com sucesso em: {GOLD_FILE_PATH}")


if __name__ == "__main__":
    main()

