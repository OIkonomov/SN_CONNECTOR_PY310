TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''

SELECT
    REALM,
    FED_ID,
    PROGRESS_INDEX01 AS "PLAYER_LEVEL",
    MIN(CLIENT_TIME) AS "FROM_",
    MAX(CLIENT_TIME) AS "TO_",
    RESOURCE_INT,
    ITEM_NAME,
    ITEM_LEVEL,
    SUM(ITEM_EARNED) AS "RECEIVED",
    SUM(ITEM_LOST) AS "LOST",
    MAX(ITEM_LIMIT) AS "LIMIT"
    
FROM "ELEPHANT_DB"."AOV"."RESOURCES_REWARDS"

WHERE
    CLIENT_TIME >= '{st_date}'
    AND CLIENT_TIME < '{end_date}'
    AND FED_ID = '{account}'
    AND (RESOURCE_INT = 'Receive from IAP Bundle' OR RESOURCE_INT = 'Receive from IAP Bundle - First Purchase')

GROUP BY
    REALM,
    FED_ID,
    PLAYER_LEVEL,
    RESOURCE_INT,
    ITEM_NAME,
    ITEM_LEVEL

ORDER BY FROM_ ASC

LIMIT 10000
;
'''