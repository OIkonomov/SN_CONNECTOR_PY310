TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "NO"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''
SELECT 
    DATE(T_II.CLIENT_TIME) AS "DATE",
    T_II.CLIENT_TIME AS "TIME",
    T_II.DATA_CENTER_ID AS "SILO",
    T_II.FED_ID AS "FED",
    TO_NUMBER(SPLIT_PART(T_II.EVENT_DATA:item_data::STRING, '_', 2), 20, 0) AS "TRANSACTION_ID",
    T_Res.GOLD_EARNED AS "GOLD_EARNED",
    I_EL.NAME AS "INTERACTION",
    T_II.EVENT_DATA:item_name::INT AS "ITEM_ID",
    T_EL.NAME AS "ITEM_NAME",
    TO_NUMBER(T_II.EVENT_DATA:item_amount, 20, 0) AS "ITEM_AMOUNT",
    T_CNTRY.NAME AS "COUNTRY",
    T_IAP.PLATFORM AS "STORE",
    T_IAP.ORIGINAL_CONTENT_ID AS "PACK_NAME",
    TO_NUMBER (T_IAP.REVENUE_EUR, 10, 2) AS "REVENUE_EUR"
FROM "ELEPHANT_DB"."MOE"."ITEM_INTERACTION_RAW" AS T_II
    LEFT JOIN "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS T_EL 
    ON (T_II.EVENT_DATA:item_name::INT = T_EL.ID)
    LEFT JOIN "ELEPHANT_DB"."DIMENSIONS"."ELEMENT" AS I_EL
    ON (T_II.EVENT_DATA:item_int::INT = I_EL.ID)
    LEFT JOIN "ELEPHANT_DB"."MOE"."IAP" AS T_IAP 
    ON (TO_NUMBER(SPLIT_PART(T_II.EVENT_DATA:item_data::STRING, '_', 2)) = TO_NUMBER(T_IAP.TRANSACTION_ID))
    LEFT JOIN "ELEPHANT_DB"."DIMENSIONS"."COUNTRY" AS T_CNTRY 
    ON (T_IAP.COUNTRY = T_CNTRY.CODE)
    
LEFT JOIN (SELECT DISTINCT
            FED_ID,
            CLIENT_TIME,
            EVENT_DATA:hard_currency_earned::INT AS "GOLD_EARNED"
           FROM "ELEPHANT_DB"."MOE"."RESOURCE_CHANGE_RAW"
           WHERE
            CLIENT_TIME >= '{st_date}'
            AND CLIENT_TIME < '{end_date}'
            AND FED_ID = '{account}'
            AND EVENT_DATA:change_int::INT = 354526) AS T_Res
           ON (T_II.FED_ID = T_Res.FED_ID AND T_II.CLIENT_TIME = T_Res.CLIENT_TIME)
WHERE
    "TIME" >= '{st_date}'
    AND "TIME" < '{end_date}'
    AND T_II.FED_ID = '{account}'
    AND T_II.EVENT_DATA :item_int::INT = 199840
ORDER BY TIME ASC
LIMIT 10000
;
'''