-- Test Query 1: Count all funds
SELECT COUNT(*) as total_funds FROM fund_master;

-- Test Query 2: List all fund houses
SELECT DISTINCT fund_house FROM fund_master;

-- Test Query 3: Latest NAV for each scheme
SELECT scheme_name, date, nav 
FROM nav_history 
ORDER BY date DESC 
LIMIT 10;

-- Test Query 4: Average NAV per scheme
SELECT scheme_name, ROUND(AVG(nav), 2) as avg_nav
FROM nav_history
GROUP BY scheme_name;