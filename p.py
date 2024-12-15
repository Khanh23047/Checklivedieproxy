import requests
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
from time import sleep
import pystyle
import random


import time

def slow_type(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    slow_type("""

            
\033[1;31m ██████╗ ██╗   ██╗██╗   ██╗██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗
\033[1;36m ██╔══██╗██║   ██║╚██╗ ██╔╝██║ ██╔╝██║  ██║██╔══██╗████╗  ██║██║  ██║
\033[1;32m ██║  ██║██║   ██║ ╚████╔╝ █████╔╝ ███████║███████║██╔██╗ ██║███████║
\033[1;34m ██║  ██║██║   ██║  ╚██╔╝  ██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║██╔══██║
\033[1;35m ██████╔╝╚██████╔╝   ██║   ██║  ██╗██║  ██║██║  ██║██║ ╚████║██║  ██║
\033[1;31m ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 
               BOX ZALO: https://zalo.me/g/nguadz335
               ADMIN : DUY KHÁNH 
               YTB : REVIEWTOOL247NDK
                                   
""", delay=0.00)



def clear():
    os.system("cls" if os.name == "nt" else "clear")


def thanh():
    print("\033[1;37m —————————————————————————————————————————————")



# Bắt đầu chay tool
sleep(3)
clear()
banner()
thanh()
slow_type(" ")
sleep(3)
proxy_list = input("\033[1;32m Vui lòng nhập file chứa Proxy: \033[1;33m")
with open(proxy_list, 'r') as file:
    proxy_list = file.read().split("\n")
    proxy_count = len(proxy_list)
luu = input("\033[1;31m Vui lòng nhập tệp để lưu Proxy Live: \033[1;37m")
slow_type(f" \033[1;31mFound: \033[1;37m{proxy_count} \033[1;31mproxy in your proxy file")
sleep(2)
slow_type(" \033[1;31mPlease \033[1;37mwait \033[1;31mfor \033[1;37ma \033[1;31msec")
sleep(3)
print(" \033[1;37mStart \033[1;31mrunning \033[1;37mthe \033[1;31mtool\033[1;37m. \033[1;31mPlease \033[1;37mdon't \033[1;31mpress \033[1;37manything")
print("\033[1;37m ———————————————————————————————————————————————")
sleep(3)
list = []
for p in proxy_list:
    prx = p.strip("\n")
    list.append(prx)


def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=20)
        if response.status_code == 200 or response.status_code == 202 or response.status_code == 504 or response.status_code == 503 or response.status_code == 502 or response.status_code == 500:
            detect_location(proxy)
            open(luu,'a').write(proxy+'\n')
            return True
    except requests.exceptions.RequestException:
        pass

    print(f" \033[1;37m[\033[1;31m🌸\033[1;37m] \033[1;37m{proxy} \033[1;31m• \033[1;37mUnknown/Unknown \033[1;31m• \033[1;31mBAD")
    return False


def detect_location(proxy):
    ip_address = proxy.split(':')[0]
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            print(f" \033[1;37m[\033[1;31m🌸\033[1;37m] \033[1;37m{proxy} \033[1;31m• \033[1;37m{data['country']}/{data['city']} \033[1;31m• \033[1;32mLIVE")
            open(luu,'a').write(proxy+'\n')
        else:
            print(" \033[1;37m[\033[1;31m🌸\033[1;37m] \033[1;31mFailed to detect location for proxy.")


def process_proxy(proxy):
    if check_proxy(proxy):
        pass


num_workers = 200

with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(process_proxy, proxy_list)

print(
    f" \033[1;31mScanning proxies successfully. Currently on the proxy list \033[1;37m{luu} \033[1;31mis having \033[1;37m%s \033[1;31mproxies-live"
    % (len(open(f"{luu}").readlines()))
)
print("\033[1;31m Thanks for using my tool<3")
logout = input(" Press enter to exit!")
exit()