TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''

WITH a AS 
    (SELECT
        CLIENT_TIME AS "TIME",    
        ARMY_ID,
        ARMY_PURPOSE,
        ARMY_INT,
        TARGET_TYPE,
        TARGET_TYPE_LEVEL AS "TARGET_LEVEL",
        COORD,
        FED_ID AS "FED",
        PROGRESS_INDEX01 AS "HERO_LEVEL",
        ALL_ID,
        USER_ID AS "DEVICE_ID",
        REALM,
        json_object.value AS "BONUSES",
        TRY_PARSE_JSON(BONUSES):id AS "HERO_ID",
        TRY_PARSE_JSON(BONUSES):level AS "LEVEL",
        TRY_PARSE_JSON(BONUSES):wounds AS "WOUNDS"

    FROM
        "ELEPHANT_DB"."AOV"."ARMY_INTERACTION",
        LATERAL FLATTEN(input => TRY_PARSE_JSON(ARMY_LOAD)) json_object

    WHERE
        SERVER_TIME >= '{st_date}'
        AND SERVER_TIME < '{end_date}'
        AND FED_ID = '{account}'
        )
        SELECT
            TIME,
            ARMY_PURPOSE,
            TARGET_TYPE,
            TARGET_LEVEL,
            ARMY_ID,
            COORD,
            ARMY_INT,
            HERO_ID,
            T_Element.NAME AS "HERO_NAME",
            HERO_LEVEL,
            WOUNDS,
            REALM,
            FED,
            ALL_ID,
            DEVICE_ID
            
        FROM a
        
        LEFT JOIN
            "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_Element
            ON (a.HERO_ID = T_Element.ID)

        ORDER BY TIME ASC, ARMY_ID ASC, HERO_NAME ASC
    
LIMIT 10000
;
'''