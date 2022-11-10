TYPE = "Player"
CREDENTIAL = "YES"
FILTER = "Combat ID"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ = '''
SELECT * FROM "ELEPHANT_DB"."WPO"."COMBAT_INTERACTION"
WHERE DATE(SERVER_TIME) >= '{st_date}' AND DATE(SERVER_TIME) <= '{end_date}' AND FED_ID = '{account}' AND COMBAT_ID = '{filter_value}'
ORDER BY SERVER_TIME;
'''