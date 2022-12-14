TYPE = "Alliance"
CREDENTIAL = "NO"
FILTER = "ITEM NAME"
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
    LOWER (NAME) LIKE LOWER('%{filter_value}%')
ORDER BY
    ITEM_NAME ASC
;
'''