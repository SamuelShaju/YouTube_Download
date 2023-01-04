import Link_to_mp3_2
import requests
from bs4 import BeautifulSoup
import re
import json


cookies = {
    'VISITOR_INFO1_LIVE': 'Qys10dkIfU8',
    'wide': '1',
    'PREF': 'f4=4000000&tz=Asia.Calcutta&f6=40000000&f5=30000',
    'YSC': 'YMCa-KJw9_M',
    'SID': 'MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmA18xtU7xDX35mR-eWQb2g.',
    '__Secure-1PSID': 'MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmv8tL8H56TQtDjpJuUdHkw.',
    '__Secure-3PSID': 'MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zMquq9uS8Bm_4gCEC4-UeQA.',
    'HSID': 'ASCCZI3-CeXZg6lhJ',
    'SSID': 'A6zmEwYSBWrN5iTZl',
    'APISID': 'DFDKJfrDYbQwfeOa/AtsdlLWKvmoC6BRJy',
    'SAPISID': 'mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P',
    '__Secure-1PAPISID': 'mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P',
    '__Secure-3PAPISID': 'mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P',
    'LOGIN_INFO': 'AFmmF2swRQIhAKT89mMPSbcimVA1-KHbMScj-VERy7OlRF2sJYwIf82-AiBjT2CAzz03ZdpXVsVjXtIJGYaCDF3xJx1mtqL-O5R1pw:QUQ3MjNmd1pGaXBGbm55UmZtd1VsOVEzRkxya0RSMU85aGFtOHh3Vzd3MldDS1Fia1BDdUZ6Z2pkZ25UMVRUU3NoYm9ZV1BnalR3ZVBWZXVSUTZfS2V3NFpzMW9icGdNWHZjRTVfWUtiTXhGemZ5RDdzd3MtcVdGclVrU2EwT0d4aUtmdlZ5cDIzdHJMcHdSc1VSNm1MX192eW5oM0dvQ1dR',
    'CONSISTENCY': 'AGXVzq_qK-ySu50lIE3TGXJ1ZOA_b9Y8FuWfBOM5QyswX-kYwd4s-VQtmy0Pa5FDvfNZn2-dDYtHLlAmfEqCw_5ZuXyzja8RVGJ1I7HEomf6QAfkV_EYqfulMmnEis3Ty2EhLnbLzSCtgaMae83qnxyI',
    'SIDCC': 'AEf-XMRl1Y1EC1OcPLHi_jy3fVBjvNGTdzjFto5VxusDszTuQswr9Puzs3oLsw3r8rVgzNd6_SI',
    '__Secure-1PSIDCC': 'AEf-XMS-IRxnEjK3zA86V_x97ZzrnByYq-v_quN2TnCEv-jfre6IoLgw9bRYJ7Mcooi0qCa2AT8',
    '__Secure-3PSIDCC': 'AEf-XMQR3pTokSZj7BJ5BgF_G2vg_ynOlQmOiOkI03qAbMxQ6RteElx0yFzANUhguwHFuvdGQxo',
}

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'VISITOR_INFO1_LIVE=Qys10dkIfU8; wide=1; PREF=f4=4000000&tz=Asia.Calcutta&f6=40000000&f5=30000; YSC=YMCa-KJw9_M; SID=MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmA18xtU7xDX35mR-eWQb2g.; __Secure-1PSID=MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmv8tL8H56TQtDjpJuUdHkw.; __Secure-3PSID=MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zMquq9uS8Bm_4gCEC4-UeQA.; HSID=ASCCZI3-CeXZg6lhJ; SSID=A6zmEwYSBWrN5iTZl; APISID=DFDKJfrDYbQwfeOa/AtsdlLWKvmoC6BRJy; SAPISID=mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P; __Secure-1PAPISID=mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P; __Secure-3PAPISID=mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P; LOGIN_INFO=AFmmF2swRQIhAKT89mMPSbcimVA1-KHbMScj-VERy7OlRF2sJYwIf82-AiBjT2CAzz03ZdpXVsVjXtIJGYaCDF3xJx1mtqL-O5R1pw:QUQ3MjNmd1pGaXBGbm55UmZtd1VsOVEzRkxya0RSMU85aGFtOHh3Vzd3MldDS1Fia1BDdUZ6Z2pkZ25UMVRUU3NoYm9ZV1BnalR3ZVBWZXVSUTZfS2V3NFpzMW9icGdNWHZjRTVfWUtiTXhGemZ5RDdzd3MtcVdGclVrU2EwT0d4aUtmdlZ5cDIzdHJMcHdSc1VSNm1MX192eW5oM0dvQ1dR; CONSISTENCY=AGXVzq_qK-ySu50lIE3TGXJ1ZOA_b9Y8FuWfBOM5QyswX-kYwd4s-VQtmy0Pa5FDvfNZn2-dDYtHLlAmfEqCw_5ZuXyzja8RVGJ1I7HEomf6QAfkV_EYqfulMmnEis3Ty2EhLnbLzSCtgaMae83qnxyI; SIDCC=AEf-XMRl1Y1EC1OcPLHi_jy3fVBjvNGTdzjFto5VxusDszTuQswr9Puzs3oLsw3r8rVgzNd6_SI; __Secure-1PSIDCC=AEf-XMS-IRxnEjK3zA86V_x97ZzrnByYq-v_quN2TnCEv-jfre6IoLgw9bRYJ7Mcooi0qCa2AT8; __Secure-3PSIDCC=AEf-XMQR3pTokSZj7BJ5BgF_G2vg_ynOlQmOiOkI03qAbMxQ6RteElx0yFzANUhguwHFuvdGQxo',
    'referer': 'https://accounts.google.com/',
    'sec-ch-ua': '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83',
}

# Any Public playlist url
playlist_url = 'https://playlist.link.here'

# You can also take the link for the playlist as an input directly from user for a fron end application.
# playlist_url = input()




while True:
    try:
        response = requests.get(playlist_url, cookies=cookies, headers=headers)
        break
    except:
        continue



soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('script')



source = ''
for result in results:
    if('ytInitialData' in str(result)):
        source = result
        break



source = re.sub('<.{0,50}>', '', str(source))
json_source = json.loads(source[20:-1])


# Serializing json
json_object = json.dumps(json_source, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
list = json_source['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['playlistVideoListRenderer']['contents']
print("some")



for item in list[:-1]:
    url = 'https://www.youtube.com/watch?v='+item['playlistVideoRenderer']['videoId']
    Link_to_mp3_2.convert_to_mp3(url)



# 
# 
# 
# 
# 

# Make a request for remaining videos, playlist only returns first 100 videos, further videos need to be requested separatly.


cookies = {
    'VISITOR_INFO1_LIVE': 'Qys10dkIfU8',
    'PREF': 'f4=4000000&tz=Asia.Calcutta&f6=40000000&f5=30000',
    'YSC': 'YMCa-KJw9_M',
    'SID': 'MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmA18xtU7xDX35mR-eWQb2g.',
    '__Secure-1PSID': 'MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmv8tL8H56TQtDjpJuUdHkw.',
    '__Secure-3PSID': 'MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zMquq9uS8Bm_4gCEC4-UeQA.',
    'HSID': 'ASCCZI3-CeXZg6lhJ',
    'SSID': 'A6zmEwYSBWrN5iTZl',
    'APISID': 'DFDKJfrDYbQwfeOa/AtsdlLWKvmoC6BRJy',
    'SAPISID': 'mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P',
    '__Secure-1PAPISID': 'mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P',
    '__Secure-3PAPISID': 'mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P',
    'LOGIN_INFO': 'AFmmF2swRgIhAN9JNCl0UOMS3FZ6MAFhvGTmGEep33HT6ICJIiHmpjThAiEA-_wZGhCPgtO1OfgpT2phhh4J1jjhZ9nXPuuUmN24oKA:QUQ3MjNmeHc0WHdqSUs0eHdTblVKNDhmMGdvbDh0MDh4enhBcUh6RlNwcDBTdjNsOG1jZ1J1U3NIOV9ZaWxkOHFBemdEaXNhNzFnNFpwSWhnOUU2MExyTmgtclhHRGQza3BLbnR5TndYaVdxRm02SEhEb3ZJSjNqSC1NQ3FvaWFlN0lJaTl1NTVHdHhRWWpxcTZzNDNncVp6WTV5cGRNNlNR',
    'wide': '1',
    'SIDCC': 'AEf-XMQj8U0evTp12AtWqnnYHOANa-FgOe8cRYNAn8nGJC1PevWAxgeY8fwRm6aOa2CId8_wi_M',
    '__Secure-1PSIDCC': 'AEf-XMRF1r-8W3nrw3rE6PWid9SmGGk73bg-0OQGAL9NjUH-hRh1oPmvhn8yGJc1vHDfK5DK2Nc',
    '__Secure-3PSIDCC': 'AEf-XMSJ0bK6xVb5TZss84xolvEVeVZPTw-09xFkDbwGKYoLHDfv4WQFFBSsG7VCemPYQG6ycSk',
}

headers = {
    'authority': 'www.youtube.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7',
    'authorization': 'SAPISIDHASH 1660589287_152d93a3beeac96e5bb623818d43f3690c4d92ae',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'VISITOR_INFO1_LIVE=Qys10dkIfU8; PREF=f4=4000000&tz=Asia.Calcutta&f6=40000000&f5=30000; YSC=YMCa-KJw9_M; SID=MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmA18xtU7xDX35mR-eWQb2g.; __Secure-1PSID=MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zmv8tL8H56TQtDjpJuUdHkw.; __Secure-3PSID=MwhM5KMHXb98MGztrly0-Q5rXFIv8UZfK40akTID1-E1IL5zMquq9uS8Bm_4gCEC4-UeQA.; HSID=ASCCZI3-CeXZg6lhJ; SSID=A6zmEwYSBWrN5iTZl; APISID=DFDKJfrDYbQwfeOa/AtsdlLWKvmoC6BRJy; SAPISID=mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P; __Secure-1PAPISID=mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P; __Secure-3PAPISID=mgSqS0b_tUuu2_EG/AX5-oH3OQQcCpp74P; LOGIN_INFO=AFmmF2swRgIhAN9JNCl0UOMS3FZ6MAFhvGTmGEep33HT6ICJIiHmpjThAiEA-_wZGhCPgtO1OfgpT2phhh4J1jjhZ9nXPuuUmN24oKA:QUQ3MjNmeHc0WHdqSUs0eHdTblVKNDhmMGdvbDh0MDh4enhBcUh6RlNwcDBTdjNsOG1jZ1J1U3NIOV9ZaWxkOHFBemdEaXNhNzFnNFpwSWhnOUU2MExyTmgtclhHRGQza3BLbnR5TndYaVdxRm02SEhEb3ZJSjNqSC1NQ3FvaWFlN0lJaTl1NTVHdHhRWWpxcTZzNDNncVp6WTV5cGRNNlNR; wide=1; SIDCC=AEf-XMQj8U0evTp12AtWqnnYHOANa-FgOe8cRYNAn8nGJC1PevWAxgeY8fwRm6aOa2CId8_wi_M; __Secure-1PSIDCC=AEf-XMRF1r-8W3nrw3rE6PWid9SmGGk73bg-0OQGAL9NjUH-hRh1oPmvhn8yGJc1vHDfK5DK2Nc; __Secure-3PSIDCC=AEf-XMSJ0bK6xVb5TZss84xolvEVeVZPTw-09xFkDbwGKYoLHDfv4WQFFBSsG7VCemPYQG6ycSk',
    'origin': 'https://www.youtube.com',
    'referer': 'https://www.youtube.com/playlist?list=PLiJCNvqYLhaQ_yu69ZX_NxvIzkftktuxC',
    'sec-ch-ua': '"Opera";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83',
    'x-goog-authuser': '0',
    'x-goog-visitor-id': 'CgtReXMxMGRrSWZVOCiQqeqXBg%3D%3D',
    'x-origin': 'https://www.youtube.com',
    'x-youtube-bootstrap-logged-in': 'true',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20220815.01.00',
}

params = {
    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    'prettyPrint': 'false',
}

json_data = {
    'context': {
        'client': {
            'hl': 'en-GB',
            'gl': 'IN',
            'remoteHost': '109.228.49.100',
            'deviceMake': '',
            'deviceModel': '',
            'visitorData': 'CgtReXMxMGRrSWZVOCiQqeqXBg%3D%3D',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20220815.01.00',
            'osName': 'Windows',
            'osVersion': '10.0',
            'originalUrl': 'https://www.youtube.com/playlist?list=PLiJCNvqYLhaQ_yu69ZX_NxvIzkftktuxC',
            'screenPixelDensity': 1,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': 'CJCp6pcGELiLrgUQy-z9EhC-tq4FEJOvrgUQt8utBRDLoq4FEK-zrgUQ1bGuBRDUg64FEKj6_RIQ16KuBRDYvq0FEJH4_BI%3D',
            },
            'screenDensityFloat': 1.25,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
            'timeZone': 'Asia/Calcutta',
            'browserName': 'Opera',
            'browserVersion': '89.0.4447.83',
            'screenWidthPoints': 764,
            'screenHeightPoints': 754,
            'utcOffsetMinutes': 330,
            'connectionType': 'CONN_CELLULAR_2G',
            'memoryTotalKbytes': '8000000',
            'mainAppWebInfo': {
                'graftUrl': 'https://www.youtube.com/playlist?list=PLiJCNvqYLhaQ_yu69ZX_NxvIzkftktuxC',
                'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_UNKNOWN',
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': True,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [],
        },
        'clickTracking': {
            'clickTrackingParams': 'CCsQ7zsYACITCLyNnOvAyfkCFUNeFgodZBIPqQ==',
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': '1660589252633',
                },
                {
                    'key': 'flash',
                    'value': '0',
                },
                {
                    'key': 'frm',
                    'value': '0',
                },
                {
                    'key': 'u_tz',
                    'value': '330',
                },
                {
                    'key': 'u_his',
                    'value': '6',
                },
                {
                    'key': 'u_h',
                    'value': '864',
                },
                {
                    'key': 'u_w',
                    'value': '1536',
                },
                {
                    'key': 'u_ah',
                    'value': '824',
                },
                {
                    'key': 'u_aw',
                    'value': '1536',
                },
                {
                    'key': 'u_cd',
                    'value': '24',
                },
                {
                    'key': 'bc',
                    'value': '31',
                },
                {
                    'key': 'bih',
                    'value': '754',
                },
                {
                    'key': 'biw',
                    'value': '750',
                },
                {
                    'key': 'brdim',
                    'value': '0,0,0,0,1536,0,1536,824,764,754',
                },
                {
                    'key': 'vis',
                    'value': '1',
                },
                {
                    'key': 'wgl',
                    'value': 'true',
                },
                {
                    'key': 'ca_type',
                    'value': 'image',
                },
            ],
            'bid': 'ANyPxKp7wszlzFKhzxJL9DIVaxOfYIfJCgvLN_OvHH7C1BenmGDR6yOMNl7n2Z_y8k0O9xu-0hv4KcITAC5wA8MT4ZUQtS86qw',
        },
    },
    'continuation': '4qmFsgJhEiRWTFBMaUpDTnZxWUxoYVFfeXU2OVpYX054dkl6a2Z0a3R1eEMaFENBRjZCbEJVT2tOSFVRJTNEJTNEmgIiUExpSkNOdnFZTGhhUV95dTY5WlhfTnh2SXprZnRrdHV4Qw%3D%3D',
}



while True:
    try:
        response = requests.post('https://www.youtube.com/youtubei/v1/browse', params=params, cookies=cookies, headers=headers, json=json_data)
        break
    except:
        continue

for item in response.json()['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']:
    url = 'https://www.youtube.com/watch?v='+item['playlistVideoRenderer']['videoId']
    Link_to_mp3_2.convert_to_mp3(url)
    # print(item['playlistVideoRenderer']['videoId'])