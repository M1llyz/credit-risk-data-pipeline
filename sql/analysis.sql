-- Total por tipo de crédito
SELECT target, COUNT(*) 
FROM german_credit
GROUP BY target;

-- Média de idade por tipo de crédito
SELECT target, AVG(age) 
FROM german_credit
GROUP BY target;

-- Distribuição por emprego
SELECT employment_since, COUNT(*) 
FROM german_credit
GROUP BY employment_since;

-- Distribuição de risco por finalidade do crédito
SELECT purpose, target, COUNT(*) AS total
FROM german_credit
GROUP BY purpose, target
ORDER BY purpose, target;

-- Crédito por faixa etária
SELECT
    CASE
        WHEN age <= 25 THEN 'até 25'
        WHEN age <= 35 THEN '26-35'
        WHEN age <= 45 THEN '36-45'
        WHEN age <= 55 THEN '46-55'
        ELSE '56+'
    END AS faixa_etaria,
    target,
    COUNT(*) AS total
FROM german_credit
GROUP BY
    CASE
        WHEN age <= 25 THEN 'até 25'
        WHEN age <= 35 THEN '26-35'
        WHEN age <= 45 THEN '36-45'
        WHEN age <= 55 THEN '46-55'
        ELSE '56+'
    END,
    target
ORDER BY faixa_etaria;

-- Finalidades mais comuns
SELECT
    purpose,
    COUNT(*) AS total
FROM german_credit
GROUP BY purpose
ORDER BY total DESC;

-- Ticket medio por tipo de crédito
SELECT
    target,
    AVG(credit_amount) AS ticket_medio
FROM german_credit
GROUP BY target;