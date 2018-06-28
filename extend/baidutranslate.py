import requests
import json

class Translate:

    def getResult(self,text):
        url = "http://fanyi.baidu.com/v2transapi"
        data = {}
        data['from'] = 'en'
        data['to'] = 'zh'
        data['query'] = text
        data['transtype'] = 'translang'
        data['simple_means_flag'] = '3'
        r=requests.post(url=url,data=data)
        r.encoding='UTF-8'
        target = json.loads(r.text)
        tgt = target['trans_result']['data'][0]['dst']

        return tgt
