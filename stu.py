import requests
from extend.googletranslate import Translate
import re
def translate(text):
    trans=Translate()
    tk = trans.getTk(text=text)
    url = 'https://translate.googleapis.com/translate_a/t?anno=3&client=te_lib&format=html&v=1.0&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&logld=vTE_20170911_00&sl=auto&tl=zh-CN&sp=nmt&tc=5&sr=1&tk=%s&mode=1' % tk
    data = 'q=%s' % text
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Connection': 'close',
    }
    r = requests.post(url=url, data=data,headers=headers,timeout=10)
    result = r.text
    return result

text=translate('hello')


