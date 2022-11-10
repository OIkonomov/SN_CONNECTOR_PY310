TYPE = "Alliance"
CREDENTIAL = "NO"
FILTER = "NO"
SILO = "YES"
REALM = "NO"
DATE = "YES"

SQL_REQ = '''

SELECT DISTINCT
    DATA_CENTER_ID AS "SILO",
    DATE(CLIENT_TIME) AS "DATE",
    PLATFORM AS "PLATFORM",
    COUNTRY AS "COUNTRY",
    COUNTRY_CODE AS "COUNTRY_CODE",
    CURRENCY AS "CURRENCY",
    COUNT(TRANSACTION_ID) AS "TOTAL_TRRANSACTIONS"
FROM
    "ELEPHANT_DB"."MOE"."IAP"
WHERE
    CLIENT_TIME >= '{st_date}'
    AND CLIENT_TIME < '{end_date}'
    AND IAP_ACTION = 'New Purchase'
    AND SILO LIKE '{silo}'
GROUP BY SILO, DATE, PLATFORM, COUNTRY, COUNTRY_CODE, CURRENCY
ORDER BY DATE
LIMIT 100000
;
'''