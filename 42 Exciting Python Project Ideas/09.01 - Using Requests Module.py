import requests

data = None
try:
    data = requests.get("https://www.google.com/search?q=vaccination+statistics&rlz=1C1CHBD_enPH862PH862&oq=vaccination+statistics&aqs=chrome..69i57j0i433i512j35i39j0i131i433i512j0i433i512l2j0i131i433i512j0i433i512j0i131i433i512j0i512.6842j0j9&sourceid=chrome&ie=UTF-8")
except:
    print("Check your internet connection")


try:
    d = data.json
except:
    print("There was an error getting html contents")

for i in d:
    print(i)