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
    FED_ID AS "FED",
    MAX(PROGRESS_INDEX01) AS "PLAYER_LEVEL",
    REPLACE(REPLACE(REPLACE(EVENT_NAME,'TEXT_EVENTS_MENU_'),'_HEADER'),'_',' ') AS "EVENT_NAME",
    EVENT_DATA_EVENT_ID AS "TLE_EVENT_ID",
    RESOURCE_INT AS "ACTION",
    EVENT_REWARD_TYPE AS "REWARD_TYPE",
    ITEM_NAME AS "REWARD",
    ITEM_LEVEL,
    SUM(ITEM_EARNED) AS "QNTY"

FROM
    "ELEPHANT_DB"."AOV"."RESOURCES_REWARDS"

WHERE
    CLIENT_TIME >= '{st_date}'
    AND CLIENT_TIME < '{end_date}'
    AND (RESOURCE_INT = 'Receive TLE Reward'OR RESOURCE_INT = 'Receive TLE Reward - Milestone' OR RESOURCE_INT = 'Reward from Leaderboard')
    AND FED_ID = '{account}'

GROUP BY
    TIME,
    DATE,
    FED,
    EVENT_NAME,
    TLE_EVENT_ID,
    REWARD_TYPE,
    ACTION,
    REWARD,
    ITEM_LEVEL

ORDER BY
    TIME ASC,
    FED_ID ASC,
    EVENT_REWARD_TYPE ASC,
    ITEM_NAME ASC

LIMIT 10000
;
'''