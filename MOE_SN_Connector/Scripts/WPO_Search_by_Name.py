TYPE = "Player"
CREDENTIAL = "NO"
FILTER = "Name"
SILO = "NO"
REALM = "NO"
DATE = "YES"

SQL_REQ = '''
SELECT * FROM "ELEPHANT_DB"."WPO"."PLAYER_CONNECTION_REPORT"
WHERE DATE(SERVER_TIME) >= '{st_date}' AND DATE(SERVER_TIME) <= '{end_date}' and INGAME_NICKNAME_ACTIVE LIKE LOWER('%{filter_value}%')
ORDER BY SERVER_TIME;
'''