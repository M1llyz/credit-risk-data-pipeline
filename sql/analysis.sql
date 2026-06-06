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