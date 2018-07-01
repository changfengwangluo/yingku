import execjs
import requests
import re


class Translate:

    def __init__(self):
        self.js = execjs.compile("""
    function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 
         
        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 
     
        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 
     
    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    }
    """)

    # 计算js加密tk值
    def getTk(self, text):
        return self.js.call("TL", text)

    # http请求翻译
    def translate_get(self, text):
        headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Connection': 'close',
            'Referer': 'https://translate.google.cn/',
            'x-client-data': 'CK61yQEIi7bJAQiltskBCKmdygEInp/KAQioo8oBCKKkygE=',
        }
        tk = self.getTk(text)
        r = requests.get(
            'https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=1&tk=%s&q=%s' % (
                tk, text), headers=headers, timeout=10, verify=False)
        r.encoding = 'UTF-8'

        return r.json()  # 返回一个list列表，r.text返回一个str不好处理

    def translate_post(self, text):

        tk = self.getTk(text=text)
        url = 'https://translate.googleapis.com/translate_a/t?anno=3&client=te_lib&format=html&v=1.0&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&logld=vTE_20170911_00&sl=auto&tl=zh-CN&sp=nmt&tc=5&sr=1&tk=%s&mode=1' % tk
        data = 'q=%s' % text
        headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Connection': 'close',
        }
        try:
            r = requests.post(url=url, data=data, headers=headers, timeout=10)
            result = r.text
        except requests.exceptions.ReadTimeout:
            result = ''

        return result

    # google返回的翻译结果很复杂阿，需要提取提取出翻译结果。
    def extract_get(self, trans_list):
        if len(trans_list) > 0:
            temp_list = trans_list[0]  # 也是一个list，其中包含了一个段落
            part = ''
            for temp in temp_list:
                if temp[0] is not None:
                    part += temp[0]  # 组合成段落
        return part

    def extract_post(self, trans_list):
        li = re.findall('\["(.*?)",".*?"\]', trans_list)
        if len(li) > 0:
            trans_str = li[0]
        else:
            trans_str = ''
        return trans_str

    # 根据整行或者段落翻译
    # google翻译每一次请求是有字数限制的，是5000个字符，保险一点规定4000个为一段
    def getResultByLines(self, text):
        result = ''
        str_len = len(text)
        if str_len > 4000:
            str_list = str.split(text, '\n')  # 根据段落分割
            # 遍历段落进行翻译
            for s in str_list:
                if s != '':
                    trans_list = self.translate_post(s)  # 返回的是一个列表
                    part = self.extract(trans_list)
                    result += part + '\n'  # 组合成文章

        else:
            trans_list = self.translate_post(text)
            result = self.extract_post(trans_list)

        return result

    # 根据一些零散的文字组合凑齐5000个字符的限制，组合在一起翻译后再返回，这样减少翻译的次数，减少限制
    # 约定词组之间的分割符为换行符号
    def getResultByWords(self, text):
        trans_str = ''
        while True:
            positon = 0
            index = text.find('\n', positon)
            split_str = text[0:index]
            if len(split_str) > 4000:
                temp_trans_str = self.translate_post(split_str)
                trans_str += temp_trans_str
            else:
                trans_str = self.translate_post(text)
            return trans_str
