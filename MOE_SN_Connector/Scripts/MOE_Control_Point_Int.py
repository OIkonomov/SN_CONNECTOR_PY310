TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ = '''
SELECT
   T_CPI.CLIENT_TIME AS "TIME",
   T_EVENT.EVENT_NAME AS "EVENT",
   T_CPI.EVENT_DATA:realm_id_current::INT AS "REALM",
   T_ELEMENT_4.NAME AS "REALM_EFFECT",
   T_CPI.FED_ID AS "FED",
   T_CPI.EVENT_DATA:progress_index02::INT AS "CASTLE_LEVEL",
   T_ELEMENT.NAME AS "ACTION",
   T_ELEMENT_3.NAME AS "TARGET_TYPE",
   T_CPI.EVENT_DATA:target_fed_id::STRING AS "TARGET_FED",
   T_CPI.EVENT_DATA:target_level::INT AS "TARGET_LEVEL",
   T_CPI.EVENT_DATA:attacker_all_id::INT AS "ATTACKE_ALL_ID",
   T_CPI.EVENT_DATA:coord::STRING AS "COORD",
   T_ELEMENT_2.NAME AS "IMP_TITLE",
   T_CPI.EVENT_DATA:occupator_fed_id::STRING AS "OCCUPATOR_FED",
   T_CPI.EVENT_DATA:occupator_all_id::INT AS "OCUPATOR_ALL_ID"
   
FROM "CC_DB"."MOE"."GAMESERVERS" AS T_CPI

LEFT JOIN
    "ELEPHANT_DB"."DIMENSIONS"."EVENT" AS T_EVENT
    ON (T_EVENT.GAME_ID = 55126 
       AND T_CPI.EVENT_ID = T_EVENT.EVENT_ID)
LEFT JOIN
    "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_ELEMENT
    ON (T_CPI.EVENT_DATA:controlpoint_int::INT = T_ELEMENT.ID)
LEFT JOIN
    "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_ELEMENT_2
    ON (T_CPI.EVENT_DATA:imperial_title::INT = T_ELEMENT_2.ID)
LEFT JOIN
    "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_ELEMENT_3
    ON (T_CPI.EVENT_DATA:target_type::INT = T_ELEMENT_3.ID)
LEFT JOIN
    "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_ELEMENT_4
    ON (T_CPI.EVENT_DATA:realm_effect::INT = T_ELEMENT_4.ID)

WHERE
    T_CPI.CLIENT_TIME >= '{st_date}'
    AND T_CPI.CLIENT_TIME < '{end_date}'
    AND T_CPI.EVENT_ID = '361101'
    AND T_CPI.FED_ID = '{account}'

ORDER BY T_CPI.CLIENT_TIME ASC
LIMIT 10000
;
'''