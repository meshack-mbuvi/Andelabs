import requests
'''
This program use a weather api to obtain weather information for various cities across the world
The output contains the country code,city name,coordinates of the city,sunset and sunrise time,
minimum and maximum temperatures and pressure experienced in the city in question
:Author:Meshack Mbuvi
:Email:meshmbuvi@gmail.com
:Phone:+254719800509
'''
def get_weather_data(acity):
	city=acity
	resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=c8c1059a447fa66e786c945155f30aa2' %(city))
	weather=resp.json()
	print('Country \t\t:{sys[country]} \
	\nCity\t\t\t:{name} \
	\nCoordinates\t\t:["latitude":{coord[lat]},"longitude":{coord[lon]}]\
	\nSunrise\t\t\t:{sys[sunrise]}\
	\nSunset\t\t\t:{sys[sunset]}\
	\nTemperatures\t:["min_temp":{main[temp_min]},"max_temp":{main[temp_max]}]\
	\nPressure\t\t:{main[pressure]}'.format(**weather))
	print'*******************************************************'
if __name__=='__main__':
	cities=['Nairobi','Kampala','London']
	for city in cities:
		get_weather_data(city)