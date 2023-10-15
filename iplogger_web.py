import secrets
import random
from time import sleep
from flet import *
import requests
 

def main(page : Page):
    def start(self):
        confirmations=['cmoFPcUHbIXf2044251SCMlM','vhj1CUsFzrxYBHqQH1inwWMs57YBNjXm','qBPhm33P0Dbzpp9px5ytd58b7zHLV7lF','FqFIfEJlay8EbDaUrti4X8CsrnwSJ2y9','olMB2rIVaXSRqKvaqzvBQPPLhxXcqmZH','m288DhKWj4o4BeOwyUXXe9yO3Np54Xsr']
        confirmation=random.choice(confirmations)
        url_target=INPUT.value
        for i in range(0,4):
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
        page.add(Text('https://2no.co/'+code_url2 ))
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
                address=''
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
                            page.add(Text(''))
                            page.add(Text('-----------------------------------------',color='Yellow'))
                            page.add(Text('address : '+address))
                            page.add(Text('browser : ' +browser))
                            page.add(Text('device : '+platform))
                            page.add(Text('Time : '+time))
                            page.add(Text('date : '+date))
                            page.add(Text('useragent : '+useragent))
                            page.add(Text('=====================================',color='Yellow'))
                            page.add(Text('============== IP INFO ==============',color='Yellow'))
                            res_ip=requests.get('http://ip-api.com/json/'+address).json()
                            page.add(Text('country : '+str(res_ip['country'])))
                            page.add(Text('regionName : '+str(res_ip['regionName'])))
                            page.add(Text('zip : '+str(res_ip['zip'])))
                            page.add(Text('timezone : '+str(res_ip['timezone'])))
                            page.add(Text('as : '+str(res_ip['as'])))
                            lat=str(res_ip['lat'])
                            lon=str(res_ip['lon'])
                            page.add(Text('location : '+lat+', '+lon))
                            page.add(Text('-----------------------------------------' , color='Yellow'))
                            page.add(Text('\n'*4))
                            ips.append(address)
                            page.update()
    page.scroll='always'
    page.spacing=0
    page.padding=0
    page.add(Text('\n'))
    page.add(Text('''

  •           ┓          
  ┓┏┓┃┏┓┏┓┏┓┏┓┏┓
  ┗┣┛┗┗┛┗┫┗┫┗ ┛ 
      ┛                  ┛    ┛           
                                       '''))
    page.add(Text())
    INPUT=TextField(
        label='url',
        width=700
        )
    
    but=ElevatedButton(text=' Run ',on_click=start , height=40,width=100)
    page.add(INPUT)
    
    page.add(but)


app(target=main ,view=WEB_BROWSER)