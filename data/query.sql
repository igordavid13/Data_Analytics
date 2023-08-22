WITH AccountClassTotals AS (
  SELECT
    account_code,
	account_suitability,
    class_name,
    SUM(position_value) AS total_class_value
  FROM
    postgres
  GROUP BY
    account_code, class_name, account_suitability
),

AccountComputedRatios AS (
  SELECT
    act.account_code,
    act.class_name,
	act.account_suitability,
    SUM(act.total_class_value) AS total_account_value,
    SUM(act.total_class_value) / t.total_account_value AS ratio
  FROM
    AccountClassTotals act
  JOIN (
    SELECT
      account_code,
      SUM(total_class_value) AS total_account_value
    FROM
      AccountClassTotals
    GROUP BY
      account_code
  ) t ON act.account_code = t.account_code
  GROUP BY
    act.account_code, act.class_name, t.total_account_value, act.account_suitability
)

SELECT
  account_code,
  account_suitability,
  class_name,
  total_account_value,
  ratio
FROM
  AccountComputedRatios
ORDER BY
  account_code




 CREATE TABLE ratio (
    classe VARCHAR(50),
    conservador DECIMAL(5,2),
    moderado_conservador DECIMAL(5,2),
    moderado DECIMAL(5,2),
    moderado_agressivo DECIMAL(5,2),
    agressivo DECIMAL(5,2)
);

INSERT INTO ratio (classe, conservador, moderado_conservador, moderado, moderado_agressivo, agressivo)
VALUES
    ('Renda Fixa Pós-Fixada', 0.70, 0.46, 0.30, 0.15, 0.05),
    ('Renda Fixa Inflação', 0.12, 0.16, 0.24, 0.20, 0.19),
    ('Renda Fixa Pré-Fixada', 0.05, 0.08, 0.10, 0.11, 0.10),
    ('Renda Variável', 0.02, 0.04, 0.07, 0.14, 0.20),
    ('Multimercado', 0.09, 0.21, 0.22, 0.30, 0.31),
    ('Alternativos', 0.00, 0.00, 0.00, 0.00, 0.00),
    ('Internacional', 0.02, 0.05, 0.07, 0.10, 0.15),
    ('Saldo em Conta', 0.00, 0.00, 0.00, 0.00, 0.00);


SELECT
  acr.account_code,
  acr.account_suitability,
  acr.ratio,
  r.classe,
  CASE
    WHEN acr.account_suitability = 'conservador' THEN r.conservador
    WHEN acr.account_suitability = 'moderado-conservador' THEN r.moderado_conservador
    WHEN acr.account_suitability = 'moderado' THEN r.moderado
    WHEN acr.account_suitability = 'moderado-agressivo' THEN r.moderado_agressivo
    WHEN acr.account_suitability = 'agressivo' THEN r.agressivo
  END AS ratio_value
FROM
  AccountComputedRatios acr
FULL JOIN
  ratios r ON acr.class_name = r.classe
ORDER BY
  acr.account_code, acr.account_suitability;











