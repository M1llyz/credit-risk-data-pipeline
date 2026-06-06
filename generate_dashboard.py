import os
import pandas as pd
import matplotlib.pyplot as plt

CREDIT_RISK_FILE = "data/gold/credit_risk_summary.parquet"
PURPOSE_RISK_FILE = "data/gold/purpose_risk_summary.parquet"
AGE_RISK_FILE = "data/gold/age_risk_summary.parquet"

OUTPUT_DIR = "images"
DASHBOARD_PATH = "images/credit_risk_dashboard.png"

def load_data():
    credit_risk = pd.read_parquet(CREDIT_RISK_FILE)
    purpose_risk = pd.read_parquet(PURPOSE_RISK_FILE)
    age_risk = pd.read_parquet(AGE_RISK_FILE)

    return credit_risk, purpose_risk, age_risk

def generate_dashboard():
    credit_risk, purpose_risk, age_risk = load_data()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plt.style.use("dark_background")

    fig = plt.figure(figsize=(14, 8))
    fig.patch.set_facecolor("#111827")

    fig.suptitle(
        "Credit Risk Dashboard",
        fontsize=22,
        fontweight="bold",
        color="white"
    )

    ax1 = fig.add_subplot(2, 2, 1)

    ax1.bar(
        credit_risk["target"],
        credit_risk["percentual"],
        color=["#22c55e", "#ef4444"]
    )

    ax1.set_title("Distribuição geral de crédito", fontsize=13, fontweight="bold")
    ax1.set_ylabel("Percentual (%)")
    ax1.set_ylim(0, 100)

    ax2 = fig.add_subplot(2, 2, 2)

    age_bad_credit = age_risk[age_risk["target"] == "mau crédito"]

    ax2.barh(
        age_bad_credit["age_group"].astype(str),
        age_bad_credit["percentual"],
        color="#f97316"
    )

    ax2.set_title("Mau crédito por faixa etária", fontsize=13, fontweight="bold")
    ax2.set_xlabel("Percentual (%)")
    ax2.set_xlim(0, 100)

    ax3 = fig.add_subplot(2, 1, 2)

    purpose_bad_credit = purpose_risk[
        purpose_risk["target"] == "mau crédito"
    ].sort_values("percentual", ascending=False)

    ax3.bar(
        purpose_bad_credit["purpose"],
        purpose_bad_credit["percentual"],
        color="#3b82f6"
    )

    ax3.set_title(
        "Percentual de mau crédito por finalidade",
        fontsize=13,
        fontweight="bold"
    )

    ax3.set_ylabel("Percentual (%)")

    plt.setp(
        ax3.get_xticklabels(),
        rotation=30,
        ha="right"
    )

    plt.tight_layout(rect=[0, 0, 1, 0.94])

    plt.savefig(
        DASHBOARD_PATH,
        dpi=300,
        bbox_inches="tight",
        facecolor=fig.get_facecolor()
    )

    plt.close()

    print(f"Dashboard salvo com sucesso em: {DASHBOARD_PATH}")

if __name__ == "__main__":
    generate_dashboard()
