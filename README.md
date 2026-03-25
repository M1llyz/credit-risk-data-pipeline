# 📊Credit Risk Data Pipeline

![Status](https://img.shields.io/badge/Status-Em_andamento-darkorange?style=for-the-badge)
![Tecnologias](https://img.shields.io/badge/Tecnologias-Python%20%7C%20SQL%20%7C%20Pandas-blue?style=for-the-badge)
![Tipo de Projeto](https://img.shields.io/badge/Tipo-Data%20Engineering%20Pipeline-darkgreen?style=for-the-badge)


Este projeto tem como objetivo construir um pipeline de engenharia de dados utilizando o dataset **German Credit**, disponibilizado pela UCI. A proposta é simular, na prática, como dados brutos podem ser coletados, tratados e preparados para uso em análises ou sistemas de dados.


## 📌 Sobre o Projeto

O dataset usado contém informações sobre clientes e seu histórico de crédito, sendo amplamente usado em estudos de risco de crédito. Porém, os dados originais vêm em um formato pouco intuitivo, codificado como `A11`, `A34`, `A43`, entre outros, que precisam ser interpretados antes de qualquer uso.

Então o foco desse projeto é justamente transformar esses dados brutos em dados compreensíveis, estruturados e prontos para etapas futuras do pipeline.


## ⚙️ O que já foi implementado até o momento

- Ingestão automática dos dados diretamente da fonte original (UCI)
- Armazenamento dos dados brutos na camada Bronze
- Leitura e estruturação do dataset com definição de colunas
- Conversão de variáveis categóricas codificadas em valores legíveis
- Geração de uma versão tratada dos dados na camada Silver
- Exportação dos dados em formato Parquet


## 🏗️ Arquitetura do Pipeline

O projeto segue uma arquitetura em camadas (medalhão)

### 🥉 Bronze Layer

- Armazenando os dados exatamente como foram obtidos da fonte
- Nenhuma transformação de conteúdo é aplicada
- Base bruta do pipeline

### 🥈 Silver Layer

- Tratamento e padronização dos dados
- Os códigos categóricos do dataset são convertidos em valores compreensíveis nessa camada
- Estruturação dos dados para facilitar análise e uso posterior

### 🥇 Gold Layer (em desenvolvimento)

- Armazenamento dos dados em banco de dados relacional
- Modelagem dos dados para consumo analítico
- Preparação para uso em SQL, BI e outras aplicações

📌 Planejamento atual:
- SQL Server (ambiente local)
- Possível disponibilização em PostgreSQL (Supabase) para acesso remoto


## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- PyArrow (Parquet)
- SQL (em andamento)
- SQL Server (em andamento)
- PostgreSQL / Supabase (em andamento)
- Git/GitHub


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
│
├── sql/
├── docs/
├── notebooks/
├── tests/
│
├── README.md
├── requirements.txt
└── main.py
