CREATE DATABASE CreditRiskDB;
GO

USE CreditRiskDB;
GO

CREATE TABLE german_credit (
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
);