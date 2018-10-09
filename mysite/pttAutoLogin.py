import telnetlib
import sys
import time
import json
import os


host = 'ptt.cc'

def pttLogin(account, pwd):
    telnet = telnetlib.Telnet(host)
    time.sleep(1)
    content = telnet.read_very_eager().decode('big5', 'ignore')
    print('content:', content)

    if "請輸入代號" in content:
        print('entering account')
        telnet.write((account + "\r\n").encode('big5'))
        time.sleep(1)
        content = telnet.read_very_eager().decode('big5','ignore')
        print('content:', content)
        if "請輸入您的密碼" in content:
            print('entering password')
            telnet.write((pwd + "\r\n").encode('big5'))
            time.sleep(1)
            content = telnet.read_very_eager().decode('big5','ignore')
            print('content:', content)


kids_json = os.environ.get('Kids', None)
# print(kids_json)
for kid in kids_json:
    u = kid['user']
    p = kid['pwd']
    print(u,p)
    # pttLogin(u, p)
        

