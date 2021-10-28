import datetime
import time
import requests
from plyer import notification

covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/Philippines")
except:
    print("Please check your internet connection...")

if(covidData != None):
    data = covidData.json()['Success']

    contents = covidData.content
    print(contents)    
    # while(True):
    #     notification.notify(
    #         title = "COVID19 Stats on {}".format(datetime.date.today()),
    #         message = """Total cases: {totalcases}\n
    #                     Today cases: {todaycases}\n
    #                     Today Deaths: {todaydeaths}\n
    #                     Active: {active}""".format(
    #                         totalcases = data['cases'],
    #                         todaycases = data['todayCases'],
    #                         todaydeaths = data['todayDeaths'],
    #                         active = data['active']),
    #         timeout = 30
    #     ) 
    #     time.sleep(3000)

