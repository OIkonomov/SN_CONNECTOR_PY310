TYPE = "Alliance"
CREDENTIAL = "NO"
FILTER = "TRACKING_ID"
SILO = "NO"
REALM = "NO"
DATE = "NO"

SQL_REQ =   '''
SELECT DISTINCT
    ID AS "TRACKING_ID",
    NAME AS "ITEM_NAME"
FROM
    "ELEPHANT_DB"."DIMENSIONS"."ELEMENT"

WHERE
    TRACKING_ID = {filter_value}
ORDER BY
    ITEM_NAME ASC
;
'''