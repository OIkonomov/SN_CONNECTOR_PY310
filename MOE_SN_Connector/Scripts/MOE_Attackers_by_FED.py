TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''

SELECT
    DATE(CLIENT_TIME) AS "DATE",
    DATA_CENTER_ID AS "SILO",
    REALM_ID_CURRENT AS "REALM",
    FED_ID AS "DEFENDER",
    REPLACE(REPLACE(REPLACE (INVOLVED_PLAYER_IDS:A::STRING,'"'),'['),']') AS "ATTACKER",
    COUNT(DISTINCT COMBAT_ID) AS "TOTAL_BATTLES"

FROM
    "ELEPHANT_DB"."MOE"."COMBAT_INTERACTION"

WHERE
    CLIENT_TIME >= '{st_date}'
    AND CLIENT_TIME < '{end_date}'
    AND FED_ID = '{account}'
    AND COMBAT_INT LIKE 'Defend%'
    AND BATTLE_TARGET = 'Stronghold (Owned by This Player)'
    AND COMBAT_RESULT = 'Lose'

GROUP BY
    DATE,
    SILO,
    REALM,
    DEFENDER,
    ATTACKER

ORDER BY
    TOTAL_BATTLES DESC
    
LIMIT 10000
;

'''