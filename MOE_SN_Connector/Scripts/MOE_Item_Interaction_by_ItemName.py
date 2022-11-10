TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "ITEM_NAME"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ = '''
SELECT 
    DATE(T_II.CLIENT_TIME) AS DATE,
    T_II.CLIENT_TIME AS DATE_TIME,
    T_II.FED_ID AS FED,
    I_EL.NAME AS INTERACTION,
    T_II.EVENT_DATA:item_name::INT AS ITEM_ID,
    T_EL.NAME AS ITEM_NAME,
    TO_NUMBER(T_II.EVENT_DATA:item_amount, 20, 0) AS ITEM_AMOUNT
FROM "ELEPHANT_DB"."MOE"."ITEM_INTERACTION_RAW" AS T_II
    JOIN "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_EL
    ON (T_II.EVENT_DATA:item_name::INT = T_EL.ID AND T_EL.NAME LIKE '%{filter_value}%')
    
    JOIN "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS I_EL
    ON (T_II.EVENT_DATA:item_int::INT = I_EL.ID)
WHERE
    DATE_TIME > '{st_date}'
    AND DATE_TIME < '{end_date}'
    AND FED = '{account}'
    ORDER BY 2 ASC
    LIMIT 1000
    ;
    '''