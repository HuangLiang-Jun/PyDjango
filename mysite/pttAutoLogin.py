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
    pttStatus(telnet, account, pwd)

    # if "請輸入代號" in content:
    #     print('entering account')
    #     telnet.write((account + "\r\n").encode('big5'))
    #     time.sleep(1)
    #     content = telnet.read_very_eager().decode('big5','ignore')

        # if "請輸入您的密碼" in content:
        #     print('entering password')
        #     telnet.write((pwd + "\r\n").encode('big5'))
        #     time.sleep(1)
        #     content = telnet.read_very_eager().decode('big5','ignore')
        #     # print('content:', content)
            
        #     if "您想刪除其他重複登入的連線嗎" in content:
    
        #         print("不刪除其他登入...")
                
        #         telnet.write(("n\r\n").encode('big5'))
        #         time.sleep(1)
        #         content = telnet.read_very_eager().decode('big5','ignore')
                
        #         if "請按任意鍵繼續" in content:
        #             print("資訊頁面，按任意鍵繼續...")
        #             telnet.write(("\r\n").encode('big5'))
        #             time.sleep(2)
        #             content = telnet.read_very_eager().decode('big5','ignore')
            
        #     elif "請按任意鍵繼續" in content:
        #         print("資訊頁面，按任意鍵繼續...")
        #         telnet.write(("\r\n").encode('big5'))
        #         time.sleep(2)
        #         content = telnet.read_very_eager().decode('big5','ignore')
        #     else:
        #         print('other: ', content)
        #         time.sleep(2)
        #         content = telnet.read_very_eager().decode('big5','ignore')
        #         print('other 2:', content)
        #         if "請按任意鍵繼續" in content:
        #             print("資訊頁面，按任意鍵繼續...")
        #             telnet.write(("\r\n").encode('big5'))
        #             time.sleep(2)
        #             content = telnet.read_very_eager().decode('big5','ignore')

def pttStatus(telnet, u, p):
    content = telnet.read_very_eager().decode('big5','ignore')
    if "請輸入代號" in content:
        print('請輸入代號...')
        telnet.write((u + "\r\n").encode('big5'))
        time.sleep(1)
        pttStatus(telnet, u, p)
    elif "請輸入您的密碼" in content:
        print('請輸入您的密碼...')
        telnet.write((p + "\r\n").encode('big5'))
        time.sleep(1)
        pttStatus(telnet, u, p)
    elif "您想刪除其他重複登入的連線嗎" in content:
        print('您想刪除其他重複登入的連線嗎...')
        telnet.write(("n\r\n").encode('big5'))
        time.sleep(1)
        pttStatus(telnet, u, p)
    elif "請按任意鍵繼續" in content:
        telnet.write(("\r\n").encode('big5'))
        print('login finish.')
    elif "登入中，請稍候..." in content:
        print('登入中，請稍候...')
        time.sleep(2)
        pttStatus(telnet, u, p)


kids_json = os.environ.get('Kids', None)
kids_dict = json.loads(kids_json)
for kid in kids_dict:
    u = kid['user']
    p = kid['pwd']
    pttLogin(u, p)

