import threading, socket, colorama, os, requests
import os
from colorama import init, Fore
import time
init(convert=True)


url = "https://google.com"
try:
    response = requests.get(url)  
    print(Fore.WHITE + "Internet check")
    time.sleep(.4)
    os.system("cls")
except requests.exceptions.ConnectionError:
    input("Tu n'est pas connecté à internet, redémarre ta connexion ou connecte toi à internet \npour utiliser le logiciel\nPress enter to exit")
    exit()  

httpproxies = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http"
socks4proxies = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4"
socks5proxies = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5"
print(f"""{Fore.BLUE}

                                                  /$$          
                                                 |__/          
  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$   /$$$$$$  /$$ /$$   /$$
 /$$_____/ /$$_____/ /$$__  $$|____  $$ /$$__  $$| $$|  $$ /$$/
|  $$$$$$ | $$      | $$  \__/ /$$$$$$$| $$  \ $$| $$ \  $$$$/ 
 \____  $$| $$      | $$      /$$__  $$| $$  | $$| $$  >$$  $$ 
 /$$$$$$$/|  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/| $$ /$$/\  $$
|_______/  \_______/|__/      \_______/| $$____/ |__/|__/  \__/
                                       | $$                    
                                       | $$                    
                                       |__/                    
Dev by paskard#9768
join my github
https://github.com/paskardthegoat

""")
print(f"{Fore.RED}[{Fore.GREEN}>{Fore.RED}] {Fore.BLUE} Press enter to start grabbing proxies (socks4, socks5, http)")
input()
os.system("cls")
class Proxy(threading.Thread):
    def __init__(self, ip: str, port: int):
        threading.Thread.__init__(self)
        self.port = port
        self.ip   = ip
    
    def save(self, ip: str, port: int):
        with open('proxies.txt', 'a+') as file:
            file.write(f'{ip}:{port}\n')

    def prompt(self, color, past: str, ip: str, port: int):
        print(f"{f'{color}{past}{colorama.Fore.WHITE}':<1}  {f'{ip}':<15} {f'{port}':<5}")

    def online(self, ip: str, port: int):
        session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        session.settimeout(0.5)

        try:
            session.connect((ip, port))
            session.close()

            requests.get('https://google.com', proxies={'http': f'http://{ip}:{port}', 'https': f'http://{ip}:{port}'}, timeout= 5)
            return True
        except:
            return False

    def run(self):
        if self.online(self.ip, self.port):
            self.save(self.ip, self.port)
            self.prompt(colorama.Fore.GREEN, '+', self.ip, self.port)
        else:
            pass #self.prompt(colorama.Fore.RED, '-', self.ip, self.port)

class Checker:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.RED}[{Fore.GREEN}>{Fore.RED}] {Fore.BLUE} Scrapix dev by paskard#9768")
        print(f"{'?':<1}  {'IP':<14}  {'PORT':<5}")
        print(f"{'-'}  {'--'*7}  {'--'*2}")
        self.proxy = []

    def scrape_proxy(self):
        urls = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http"
        ]

        for url in urls:
            for proxy in requests.get(url).text.split('\n'):
                self.proxy.append(proxy.split('\n')[0].strip())
        
        self.proxy = list(set(self.proxy))
    
    def main(self):
        self.scrape_proxy()

        for proxy in self.proxy:
            try:
                Proxy(proxy.split(':')[0], int(proxy.split(':')[1])).start()
            except:
                pass
    
        

Checker().main()
pt = []
with open('proxies.txt', 'r+') as pf:
    for proxy in pf:
        pt.append(proxy.split('\n')[0])
    
    pf.truncate(0)
            
with open('proxies.txt', 'a+') as pf:
    for proxy in sorted(list(set(pt)), key=len, reverse= True):
        pf.write(proxy + '\n')
    










