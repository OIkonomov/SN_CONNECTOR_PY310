TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''

SELECT
    *
FROM "ELEPHANT_DB"."AOV"."MISSION_INTERACTION"

WHERE
    SERVER_TIME >= '{st_date}'
    AND SERVER_TIME < '{end_date}'
    AND FED_ID = '{account}'

ORDER BY CLIENT_TIME ASC

LIMIT 10000
;
'''