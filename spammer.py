import httpx,os,datetime,threading,random
from fake_useragent import UserAgent



def main(token, channel, message, payloadchannel, proxylist):
    while True:
        agent = UserAgent().chrome
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": f"bearer {token}",
            "content-type": "application/json; charset=UTF-8",
            "cookie": "__ca__chat=phgjishpivr",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sentry-trace": "2d4554edba863606c91f43c0e264edb3c-a3116150hd5e0eb1-0",
            "user-agent":  str(agent) 
        }
        payload = {
            "action": "set",
            "attachments": [],
            "convJid": f"{payloadchannel}@{channel}",
            "convType": "channel",
            "replyId": "",
            "richContent": "",
            "team": "cunnies",
            "tempId": "",
            "text": f"{message}"
        }
        proxy = random.choice(proxylist)
        proxies = {
            "http://": f"http://{proxy}",
            "https://": f"http://{proxy}",
        }
        time = datetime.datetime.now().strftime("%M:%S")
        with httpx.Client(proxies=proxies) as client:
            while True:
                try:
                    x = client.post(f"https://{channel}/api/v1/message/post", headers=headers, json=payload)
                    if x.status_code == 200:
                        print(f"""{clr_reset}({clr_cyan}+{clr_reset}) Sent Message   {clr_cyan}|{clr_reset}{time}{clr_cyan}|""")
                    else:
                        print(f"""{clr_reset}({clr_yellow}?{clr_reset}) Failed To Send {clr_yellow}|{clr_reset}{time}{clr_yellow}|""")
                except Exception as err:
                    print(err)

def menu():
    print(logo)
    proxylist = open("proxies.txt", "r").read().splitlines()
    tokens = open("tokens.txt", "r").read().splitlines()
    channel = input(f"<{clr_cyan}/{clr_reset}> channel Link: ")
    payloadchannel = input(f"<{clr_cyan}/{clr_reset}> Channel Name: ")
    message = input(f"<{clr_cyan}/{clr_reset}> message: ")
    if message == "!random":
        message = os.urandom(363).hex()
    threads = input(f"<{clr_cyan}/{clr_reset}> threads: ")
    for token in tokens:
        for i in range(int(threads)):
            threading.Thread(target=main, args=(token, channel, message, payloadchannel, proxylist)).start()


logo = """\033[36m
         ▄▄·  ▄ .▄ ▄▄▄·  ▐ ▄ ▄▄▄▄▄ ▄· ▄▌
        ▐█ ▌▪██▪▐█▐█ ▀█ •█▌▐█•██  ▐█▪██▌
        ██ ▄▄██▀▀█▄█▀▀█ ▐█▐▐▌ ▐█.▪▐█▌▐█▪
        ▐███▌██▌▐▀▐█▪ ▐▌██▐█▌ ▐█▌· ▐█▀·.
        ·▀▀▀ ▀▀▀ · ▀  ▀ ▀▀ █▪ ▀▀▀   ▀ • 
        \033[39m\n
"""
clr_yellow  = '\033[33m'
clr_cyan    = '\033[36m'
clr_blue    = '\033[34m'
clr_green   = '\033[32m'
clr_magenta = '\033[35m'
clr_red     = '\033[31m'
clr_reset   = '\033[39m'
os.system("clr||cls")
menu()
