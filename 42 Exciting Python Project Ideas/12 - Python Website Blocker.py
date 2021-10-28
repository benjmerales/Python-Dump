# Run this script as root

import time
from datetime import datetime as dt

# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "youtube.com"]

now = dt.now()
if dt(now.year, now.month, now.day, 8) < now < dt(now.year, now.month, now.day, 16):
    print("Working hours")
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
else:
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)

            file.truncate()
    print("Fun hours!!!")
time.sleep(5)