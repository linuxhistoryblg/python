# Weather class
import requests
from datetime import datetime


class Weather:
    def __init__(self, zipcode):
        self.zipcode = zipcode
        self.api_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.api_key = 'f8bc480f429a85e53cd55484482ee194'
        self.call_url = self.api_url + "zip=" + zipcode + ",us&" + "&units=imperial&" + "appid=" + self.api_key
        try:
            self.api_req = requests.get(self.call_url)
            self.wx_json = self.api_req.json()
            if self.api_req.status_code == 200:
                good_response = True
            else:
                good_response = False
        except Exception:
            print("Could not communicate with openweathermap")

    def get_temp(self):
        # Get temp from json
        temp_fht = self.wx_json['main']['temp']
        # Format output truncate to hundreds
        return f'{temp_fht:.2f}'

    def get_feels_like(self):
        # Get relative temp from json
        temp_feels_like = self.wx_json['main']['feels_like']
        # Format output truncate to hundreds
        return f'{temp_feels_like:.2f}'

    def get_temp_min(self):
        # Get temp low from json
        temp_min = self.wx_json['main']['temp_min']
        # Format output truncate to hundreds
        return f'{temp_min:.2f}'

    def get_temp_max(self):
        # Get temp max from json
        temp_max = self.wx_json['main']['temp_max']
        # Format output truncate to hundreds
        return f'{temp_max:.2f}'

    def get_wx_time(self):
        timestamp = self.wx_json['dt']
        dt_obj = datetime.fromtimestamp(timestamp)
        return f'{dt_obj.year}_{dt_obj.month}_{dt_obj.day} {dt_obj.hour}:{dt_obj.minute:02d}'

    def get_wx_sunrise(self):
        timestamp = self.wx_json['sys']['sunrise']
        dt_obj = datetime.fromtimestamp(timestamp)
        return f'{dt_obj.hour}:{dt_obj.minute:02d}'

    def get_wx_sunset(self):
        timestamp = self.wx_json['sys']['sunset']
        dt_obj = datetime.fromtimestamp(timestamp)
        return f'{dt_obj.hour}:{dt_obj.minute:02d}'


x = Weather('37203')
print(x.wx_json['name'])
print(x.get_wx_time())
print(x.get_temp())
print(x.get_wx_sunrise())
print(x.get_wx_sunset())
