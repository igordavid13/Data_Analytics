WITH AccountClassTotals AS (
  SELECT
    account_code,
    class_name,
    SUM(position_value) AS total_class_value
  FROM
    postgres
  GROUP BY
    account_code, class_name
),

AccountComputedRatios AS (
  SELECT
    act.account_code,
    act.class_name,
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
    act.account_code, act.class_name, t.total_account_value
)

SELECT
  account_code,
  class_name,
  total_account_value,
  ratio
FROM
  AccountComputedRatios
ORDER BY
  account_code





