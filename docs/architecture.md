# Arquitetura do Projeto

## Fluxo de Dados

German Credit Dataset (.data)
        │
        ▼
Bronze Layer
        │
        ▼
Transformação dos Dados
(transform_data.py)
        │
        ▼
Silver Layer
(german_credit_silver.parquet)
        │
        ├──────────────► SQL Server
        │
        ▼
Gold Layer
        │
        ├─ credit_risk_summary.parquet
        ├─ purpose_risk_summary.parquet
        └─ age_risk_summary.parquet

## Camadas

### Bronze
Pra armazenar os dados brutos obtidos do dataset original.

### Silver
Contém os dados tratados, traduzidos e validados.

### Gold
Contém dados agregados e preparados para análise de negócio.

## Tecnologias Utilizadas

- Python
- Pandas
- PyArrow
- SQL
- PyODBC
- Git
- GitHub