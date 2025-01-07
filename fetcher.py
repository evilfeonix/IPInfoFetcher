from datetime import datetime
import os, sys, time, requests, argparse
global location


# Versoin: 1.7
# Author: evilfeonix
# Name: IPInfoFetcher
# Date: 27 - NOVEMBER - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


####   IP Information Fetcher Powered by ipinfo.io, 
####   This is an IP lookup tool that enables you to trace but IPv4 and IPv6 (including your public IP address), 
####   Which can then reveal your device's IP address, location, internet service provider (ISP), 
####   Approximate location (city or country) and other details.
####   However, this wouldn't typically reveal your device model or network carrier.


stop="\033[0m"
red="\033[91;1m"
cyan="\033[96;1m"
blue="\033[94;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"


err=f"{blue}[{stop}-{blue}]{red}"
note=f"{blue}[{stop}!{blue}]{red}"
info=f"{blue}[{stop}+{blue}]{green}"


def load(y):
    for a in '...'+'\n':
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1)


def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False


def F30N1X():
    return """
Usage: python3 fetcher.py [OPTION... [-i], [-p], [-m], [-a], [-u]]
-------
OPTION:
    -i  Specify the target IP address
    -p  This option will fetch your public IP address
    -m  Map the target IP address after fetching it information
    -a  About Tool and Author's Contact Information
    -u  Update IPInfoFetcher Script for Better performance
EXAMPLES:
    python3 fetcher.py -a
    python3 fetcher.py -u
    python3 fetcher.py -p
    python3 fetcher.py -p -m
    python3 fetcher.py -i 192.168.15.25
    python3 fetcher.py -i 192.168.15.25 -m
    """


def banner():
    os.system("clea" + "r || cls")
    print(f"""{cyan}
 ___ ____ ___        __       _____    _       _
|_ _|  _ \_ _|_ __  / _| ___ |  ___|__| |_ ___| |__   ___ _ __
 | || |_) | || '_ \| |_ / _ \| |_ / _ \ __/ __| '_ \ / _ \ '__|
 | ||  __/| || | | |  _| (_) |  _|  __/ || (__| | | |  __/ |
|___|_|  |___|_| |_|_|  \___/|_|  \___|\__\___|_| |_|\___|_|
{purple}Coded by {green}EvilFeonix{stop}\t\t\t\t\tv[{green}1.7{stop}]
    """)
    print(f"{red}===========================================================")
    print(f"{green}Welcome to IPInfoFetcher ({stop}Powered by ipinfo.io{green})!".center(75," "))
    print(f"{red}===========================================================")


def aboutus():
    banner()
    print(f'{green}[+] Version: v[1.7]')
    print(f'[+] Author: EvilFeonix')
    print(f'[+] Github: Evil FeoniX')
    print(f'[+] Youtube: Evil FeoniX')
    print(f'[+] Tool Name: IPInfoFetcher')
    print(f'[+] Email: evilfeonix@gmail.com')
    print(f'[+] Website: www.evilfeonix.com')
    print(f"{red}===========================================================")
    os.sys.exit()
    

def updateus():
    banner()
    load(f"\n{green}[+] Checking For Update")
    server=requests.get("https://github.com/evilfeonix/IPInfoFetcher/blob/main/fetcher.py")
    sertxt=server.text
    sertxt=sertxt.replace("\n","")
    server=sertxt.replace("\r","")

    with open(sys.argv[0], 'r') as fr:
        client = fr.read()
        if not server==client:
            print("[+] Update Found!")
            time.sleep(1)
            act=input(f'[+] Press {purple}[{stop}ENTER{purple}]{green} To Continue')
            load("[+] Updating IPInfoFetcher")
            time.sleep(4)
            with open(sys.argv[0], 'w+') as fw:
                fw.write(sertxt)
            print(f"[+] IPInfoFetcher Successfully Updated.{stop}")
            os.sys.exit()
        print(f"[+] IPInfoFetcher is up-to date!{stop}")
        os.sys.exit()


def fetcher(ip_addr):
    try:
        token = ""
        base_url = f"https://ipinfo.io/{ip_addr}"
        # base_url = f"https://ipinfo.io/{ip_addr}/json"
        url = f"{base_url}?token={token}" if token else f"{base_url}"

        global location
        resp = requests.get(url)

        if resp.status_code == 200:
            data = resp.json()
            location = data.get("loc", "N/A")
            location = location.replace(" ","")

            return {
                "IP Address": data.get("ip"),
                "Hostname": data.get("hostname", "N/A"),
                "Status":"Success",
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Timezone": data.get("timezone", "N/A"),
                "Postal Code": data.get("postal", "N/A"),
                "Organization": data.get("org", "N/A"),
                "Date and Time": datetime.now().strftime('%H:%M:%S %d-%m-%Y'),
                "Location (Lat, Lon)": data.get("loc", "N/A"),
            }
        else:
            return {
                "Status": "Failed"
                "Error": f"HTTP {resp.status_code} - Unable to fetch IP info."
            }
    except Exception as e:
        return {"Error": str(e)}

def ipmapper(ip_addr,mapper):
    banner()
    ip_addr = ip_addr.strip()
    load(f"{info} Fetching IP information")
    infoga = fetcher(ip_addr)

    for key, value in infoga.items():
        if not value == ("Failed"):
            print(f"{info} {key}: {value}")
        else:
            print(f"{err} {key}: {value}")
            os.sys.exit()

    if not mapper == True:
        print(f"{red}===========================================================")
        print(f"    	    {green}Thanks for using IPInfoFetcher{stop}		    ")
        print(f"{red}===========================================================")
        os.sys.exit()

    global location
    location = f"https://google.com/maps/place/{location}/@{location},16z"
    load(f"{info} Mapping IP address, Please wait")
    os.system(f"xdg-open {location}")
    print(f"{info} Google map will be loaded on your browser.{stop}")
    print(f"{red}===========================================================")
    print(f"	    	{green}Thanks for using IPInfoFetcher{stop}		    ")
    print(f"{red}===========================================================")
    
def main():
    parser = argparse.ArgumentParser( description = "an information gathering tool that enables users to gathers information, track and map a target IP address from around the world.")
    parser.add_argument ( "-i" , "--ip-addr" , dest= "ip_address", type=str, help='Specify the target IP address')
    parser.add_argument ( "-p" , "--public" , dest= "public_ip", action ="store_true", help='This option fetch your public IP address')
    parser.add_argument ( "-m" , "--map_ip" , dest= "map_ip", action ="store_true", help="Map the target IP address after fetching information")
    parser.add_argument ( "-a" , "--about" , dest= "about",  action ="store_true", help="About Tool and Author's Contact Information")
    parser.add_argument ( "-u" , "--update" , dest= "update",  action ="store_true",help='Update IPInfoFetcher Script for Better performance')
    argument = parser.parse_args()
    about = argument.about
    mapip = argument.map_ip
    update = argument.update
    pub_ip = argument.public_ip
    ip_addr = argument.ip_address
    # if not internet():
    if internet():
        print(f"\n{err} Error: Please check your internet connection{stop}")
        os.sys.exit()
    if update:updateus()
    elif about:aboutus()
    elif ip_addr and mapip:ipmapper(ip_addr,mapper=True)
    elif pub_ip and mapip:ipmapper(ip_addr="",mapper=True)
    elif ip_addr:ipmapper(ip_addr,mapper=False)
    elif pub_ip:ipmapper(ip_addr="",mapper=False)
    else:print(F30N1X())


if __name__ == "__main__":
    main()
    # Please Report for any Bug/Error if Found