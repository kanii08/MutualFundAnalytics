SELECT * FROM 03_aum_by_fund_house
ORDER BY aum_crore DESC
LIMIT 5;

SELECT AVG(nav)
FROM 02_nav_history;

SELECT state,
COUNT(*)
FROM 08_investor_transactions
GROUP BY state;

SELECT *
FROM 07_scheme_performance
WHERE expense_ratio_pct < 1;

SELECT fund_house,
SUM(aum_crore)
FROM 03_aum_by_fund_house
GROUP BY fund_house;