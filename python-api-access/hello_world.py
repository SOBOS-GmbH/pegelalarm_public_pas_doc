from basic_api_access import BasicApiAccess
import datetime


# Enter your private data here. If you don't have a username/password, please write to office@sobos.at
username = "username"
password = "password"


baa = BasicApiAccess(username, password)

# Example to load current water level data and some meta data of a station
currentStationData = baa.query_current_data(station_name="Linz", water_name="Donau")
print("Result: " + str(currentStationData["stations"][0]))
result0CommonId = currentStationData["stations"][0]["commonid"]

# Example to load historic water level height for a specific station
loadStartDate = datetime.datetime(2020, 5, 31, 10, 30)
loadEndDate = datetime.datetime(2020, 5, 31, 16, 45)
df = baa.query_historic_data(result0CommonId, loadStartDate, loadEndDate)
print("Result: " + str(df))
