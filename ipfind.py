#! /usr/bin/python3

# ___    ____        _____   ___    _   _    ____
#|_ _|  |  _  \     |  ___| |_ _|  | \ | |  |  _ \
# | |   | |_) ) --- | |_     | |   |  \| |  | | | |
# | |   |  __/  --- |  _|    | |   | |\  |  | |_| |
#|___|  |_|         |_|     |___|  |_| \_|  |____/


# MADE WITH LOVE BY KOBBISTAN
# This program displays your current ip address on the terminal which is very necessary
# in penetration testing
#
## SUPPORT
# BTC : 15J8YsEKTWoLyZYsoop2Cyn3NpAfEsAyc6 
# ETH : 0x4B67440415E12C6b6833F35199DA51fFCcE2e4Ad
#
# DISCLAIMER NOTICE THIS PROGRAM SHOULD NOT BE USED FOR ILLEGAL PURPOSES

import requests
import json
import sys
from subprocess import call

class color:
    red    = "\033[31m"
    green  = "\033[32m"
    yellow = "\033[33m"
    blue   = "\033[34m"
    plight = "\033[37m"
    reset  = "\033[0m"

def ConnectionStart():
    req = requests.request('get',"http://free.ipwhois.io/json/", timeout=1.5).json()
    global inow
    inow = dict(req)

def Pretty():
    ip      = inow['ip']
    country = inow['country']
    isp     = inow['isp']
    city    = inow['city']

    print("\n\tYour ip address is {}{}{} ".format(color.yellow, ip, color.reset), "  Country is {}{}{} and city is {}{}{}\n".format(color.red, country, color.reset, color.blue, city, color.reset))

if __name__ == '__main__':

    if sys.version_info.major < 3:
        print("\n\t{}Sorry for the inconvenience, Please run the program in python 3{}\n".format(color.yellow,color.reset))
        exit()

    try:
        call(["clear"])
        ConnectionStart()
        Pretty()
    except KeyboardInterrupt:
        print("{}\n\tYou have terminated the program. Please re-run to access your ip address{}".format(color.red, color.reset))
    except requests.ConnectionError:
        print("{}\n\t\tYou are not properly connected to the internet\n{}".format(color.blue, color.reset))
    except requests.HTTPError:
        print("{}\n\tSORRY{} {}You have exceeded your daily limit{}\n".format(color.red, color.reset, color.yellow, color.reset))
    except requests.ConnectTimeout:
        print("{}\n\tConnection to the server has timed out{}\n".format(color.green, color.reset))
    except requests.ReadTimeout:
        print("{}\n\tThe Server failed to send the required data. Reload to solve problem{}\n".format(color.red, color.reset))
