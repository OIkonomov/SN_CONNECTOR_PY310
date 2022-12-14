TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''
SELECT
    DATE(CLIENT_TIME) AS "DATE",
    CLIENT_TIME AS "TIME",
    DATA_CENTER_ID AS "SILO",
    REALM,
    USER_ID AS "DEVICE_ID",
    PLATFORM,
    ABOUT_ID AS "PL_ID",
    FED_ID,
    INGAME_NICKNAME_ACTIVE AS "NAME",
    ALL_ID,
    PROGRESS_INDEX01 AS "THRONE_LEVEL",
    PLAYER_POWER,
    SOFT_CURRENCY1_BALANCE AS "GOLD_BALANCE",
    SOFT_CURRENCY2_BALANCE AS "MOONDUST_BALANCE"

FROM "ELEPHANT_DB"."AOV"."PLAYER_CONNECTION_REPORT"

WHERE
    CLIENT_TIME >= '{st_date}'
    AND CLIENT_TIME < '{end_date}'
    AND FED_ID = '{account}'
    
ORDER BY
    CLIENT_TIME ASC

LIMIT 10000
;
'''
