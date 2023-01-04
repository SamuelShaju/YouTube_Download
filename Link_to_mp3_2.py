
import requests
import urllib
import time
import json
import re



def convert_to_mp3(vid_url):
    cookies = {
        '_ym_uid': '1660582080866848066',
        '_ym_d': '1660582080',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'session': 'eyJfcGVybWFuZW50Ijp0cnVlfQ.Yvp5kw.nPmIlZ_0Z0Uct6sOHBEs97h9SOg',
    }

    headers = {
        'authority': 'ytmp3.cc',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7',
        'origin': 'https://ytmp3.cc',
        'referer': 'https://ytmp3.cc/90e46/',
        'sec-ch-ua': '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83',
        'uuid': 'eb03504f7f8a20479f81f834ccb3fbb8',
        'x-requested-with': 'XMLHttpRequest',
    }

    base_url = 'https://ytmp3.cc/event/parse_start/'

    

    while True:
        try:
            response = requests.post(base_url+urllib.parse.quote(vid_url, safe=''), cookies=cookies, headers=headers)
            break
        except Exception as e:
            print("ARGS: ", e.args)
            print("MSG: ", e.message)
            continue
    print("Parsing...")
    
    headers = {
        'authority': 'ytpp3.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7',
        'origin': 'https://ytmp3.cc',
        'referer': 'https://ytmp3.cc/',
        'sec-ch-ua': '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83',
        'uuid': 'eb03504f7f8a20479f81f834ccb3fbb8',
    }

    data = {
        'u': vid_url,
        'c': 'IN',
    }

    
    while True:
        try:
            print("Trying to fetch request...")
            response = requests.post('https://ytpp3.com/newp', headers=headers, data=data)
            break
        except Exception as e:
            print(e.args)
            continue


    print(response.json()['message'], "here")


    while True:
        print(response.json()['message'], "here")
        try:
            print("Trying to download")
            if(response.json()['data']['mp3']==None):
                new = requests.get(response.json()['data']['mp3_cdn'][0]['mp3_url'])
            else:
                new = requests.get('https://ytpp3.com'+response.json()['data']['mp3'][0]['mp3_url'])
            

            break
        except Exception as e:
            print(e.args)
            continue

    
    print(response.json()['data']['title'])

    name = 'songs/' +re.sub("_{1,}", "_", re.sub('[^a-zA-Z0-9]', '_', response.json()['data']['title'][:52]))+'.mp3'
    with open(name, 'wb') as f:
        f.write(new.content)


# convert_to_mp3('https://www.youtube.com/watch?v=co4YpHTqmfQ')