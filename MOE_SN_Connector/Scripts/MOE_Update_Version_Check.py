TYPE = "Alliance"
CREDENTIAL = "NO"
FILTER = "GAME VERSION"
SILO = "YES"
REALM = "NO"
DATE = "YES"

SQL_REQ =   '''

SELECT DISTINCT
  DATE(T_Launch.SERVER_TIME) AS "DATE",
  T_Launch.DATA_CENTER_ID AS "SILO",
  T_Platform.NAME AS "PLATFORM",
  T_Launch.VERSION AS "VER",
  COUNT(DISTINCT T_Launch.FED_ID) AS "ACCOUNTS",
  SUM(ACCOUNTS) OVER(PARTITION BY DATE) "TOTAL_ACCOUNTS_PER_DATE",
  SUM(ACCOUNTS) OVER() "TOTAL_ACCOUNTS"

FROM "ELEPHANT_DB"."MOE"."LAUNCH_RESUME_RAW" AS T_Launch

LEFT JOIN
    "ELEPHANT_DB"."DIMENSIONS"."PLATFORM" AS T_PLatform
    ON (T_Launch.GAME_ID = T_Platform.GGI)

WHERE SERVER_TIME > '{st_date}'
AND SERVER_TIME < '{end_date}'
AND DATA_CENTER_ID LIKE '{silo}'
AND VERSION LIKE ('{filter_value}%')
GROUP BY 1,2,3,4

ORDER BY DATE DESC, ACCOUNTS DESC
LIMIT 10000
;
'''