# 📊Credit Risk Data Pipeline

![Status](https://img.shields.io/badge/Status-Em_andamento-darkorange?style=for-the-badge)
![Tecnologias](https://img.shields.io/badge/Tecnologias-Python%20%7C%20SQL%20%7C%20Pandas-blue?style=for-the-badge)
![Tipo de Projeto](https://img.shields.io/badge/Tipo-Data%20Engineering%20Pipeline-darkgreen?style=for-the-badge)


Este projeto tem como objetivo construir um pipeline de engenharia de dados end-to-end utilizando o dataset **German Credit**, disponibilizado pela UCI Machine Learning Repository. A proposta é simular, na prática, como dados brutos podem ser coletados, tratados e preparados para uso em análises ou sistemas de dados.


## 📌 Sobre o Projeto

O dataset usado contém informações sobre clientes e seu histórico de crédito, sendo amplamente usado em estudos de risco de crédito. Porém, os dados originais vêm em um formato pouco intuitivo, codificado como `A11`, `A34`, `A43`, entre outros, que precisam ser interpretados antes de qualquer uso.

Então o foco desse projeto é justamente transformar esses dados brutos em dados compreensíveis, estruturados e prontos para etapas futuras do pipeline.


## ⚙️ O que já foi implementado

pipeline end-to-end capaz de:

- Ingestão automática de dados direto da fonte original (UCI)
- Armazenar dados brutos na camada bronze
- Transformar e padronizar os dados (conversão de atributos categóricos codificados em valores legíveis)
- Validação da camada Silver (dados tratados)
- Exportação da Silver em formato Parquet
- Criação da camada Gold em **SQL Server**
- Carga dos dados tratados no banco relacional
- Validação da carga via consulta SQL
- Preparar os dados para consumo analítico

## 🏗️ Arquitetura do Pipeline

O projeto segue o padrão **Medallion Architecture**:

### 🥉 Bronze Layer

- Dados armazenados exatamente como vieram da fonte
- Nenhuma transformação aplicada
- Base bruta do pipeline

### 🥈 Silver Layer

- Tratamento e padronização dos dados
- Os códigos categóricos do dataset são convertidos em valores compreensíveis nessa camada
- Estruturação dos dados para facilitar análise e uso posterior
- Armazenamento em formato Parquet

### 🥇 Gold Layer (em desenvolvimento)

- Dados armazenados em banco relacional (SQL Server)
- Modelagem dos dados para consumo analítico
- Preparação para uso em SQL, BI e outras aplicações

## 🔄 Fluxo do Pipeline

```text
Fonte (UCI)
   ↓
Bronze (dados brutos)
   ↓
Silver (dados tratados e validados)
   ↓
Gold (SQL Server)
   ↓
Consumo via SQL
```

## 🛠️ Tecnologias Utilizadas

### Processamento de dados

- Python
- Pandas
- PyArrow

### Armazenamento e banco

- Parquet
- SQL Server
- SQL
- PostgreSQL / Supabase (em andamento)

## 📂 Estrutura do Projeto

```text
credit-risk-data-pipeline/
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── src/
│   ├── ingestion/
│   │   └── download_data.py
│   ├── processing/
│   │   ├── inspect_data.py
│   │   ├── mappings.py
│   │   └── transform_data.py
│   └── loading/
│       └── load_to_sqlserver.py
│
├── sql/
│   └── analysis.sql
├── docs/
├── notebooks/
├── tests/
│
├── README.md
├── requirements.txt
└── main.py
