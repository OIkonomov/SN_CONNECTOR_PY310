TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''

WITH DET AS
    (SELECT
        DATE(CLIENT_TIME) AS "DATE",
        HOUR(CLIENT_TIME) AS "HOUR",
        COUNT(DISTINCT HOUR) OVER(PARTITION BY DATE) AS "TOTAL_HOURS",
        REALM,
        FED_ID,
        TARGET_TYPE,
        COMBAT_ID,
        COUNT(DISTINCT COMBAT_ID) AS "BATTLES",
        SUM(BATTLES) OVER(PARTITION BY DATE) AS "TOTAL_BATTLESPER_DAY"

    FROM
        "ELEPHANT_DB"."AOV"."COMBAT_INTERACTION"

    WHERE
        CLIENT_TIME >= '{st_date}'
        AND CLIENT_TIME < '{end_date}'
        AND FED_ID = '{account}'

    GROUP BY
        DATE,
        HOUR,
        REALM,
        FED_ID,
        TARGET_TYPE,
        COMBAT_ID

    ORDER BY
        DATE ASC,
        HOUR ASC

    LIMIT 10000)

SELECT
    DATE,
    TOTAL_HOURS,
    TOTAL_BATTLESPER_DAY,
    TARGET_TYPE,
    SUM(BATTLES) AS "NUBER_OF_BATTLES"

FROM 
    DET

GROUP BY
    DATE,
    REALM,
    FED_ID,
    TOTAL_HOURS,
    TARGET_TYPE,
    TOTAL_BATTLESPER_DAY

ORDER BY
    DATE ASC,
    TOTAL_BATTLESPER_DAY DESC
;
'''