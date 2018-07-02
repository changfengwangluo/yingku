import execjs
import requests, re, json


class GGTranslate:
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
            # 'x-client-data': 'CK61yQEIi7bJAQiltskBCKmdygEInp/KAQioo8oBCKKkygE=',
        }
        tk = self.getTk(text)
        try:
            r = requests.get(
                'https://translate.google.cn/translate_a/single?client=t&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=2&ssel=0&tsel=0&kc=1&tk=%s&q=%s' % (
                    tk, text), headers=headers, timeout=10, verify=False)
            r.encoding = 'UTF-8'
            return r.json()  # 返回一个list列表，r.text返回一个str不好处理
        except requests.exceptions.ReadTimeout:
            return ['']
        except requests.exceptions.ConnectionError:
            return ['']

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
        except requests.exceptions.ConnectionError:
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
    # post方式
    def getResultPostByLines(self, text):
        result = ''
        str_len = len(text)
        if str_len > 4000:
            str_list = str.split(text, '\n')  # 根据段落分割
            # 遍历段落进行翻译
            for s in str_list:
                if s != '':
                    trans_list = self.translate_post(s)  # 返回的是一个列表
                    part = self.extract_get(trans_list)
                    result += part + '\n'  # 组合成文章

        else:
            trans_list = self.translate_post(text)
            result = self.extract_post(trans_list)
        return result

    def getResultGetByLines(self, text):
        result = ''
        str_len = len(text)
        if str_len > 4000:
            str_list = str.split(text, '\n')  # 根据段落分割
            # 遍历段落进行翻译
            for s in str_list:
                if s != '':
                    trans_list = self.translate_get(s)  # 返回的是一个列表
                    part = self.extract_get(trans_list)
                    result += part + '\n'  # 组合成文章

        else:
            trans_list = self.translate_get(text)
            result = self.extract_get(trans_list)
        return result

    # 根据一些零散的文字组合凑齐5000个字符的限制，组合在一起翻译后再返回，这样减少翻译的次数，减少限制
    # 约定词组之间的分割符为换行符号
    def getResultByWords(self, text):
        trans_str = ''
        if len(text) > 4000:
            while True:
                positon = 0
                index = text.find('#', positon)
                split_str = text[0:index]
                if len(split_str) > 4000:
                    temp_trans_str = self.translate_post(split_str)
                    trans_str += temp_trans_str
                    positon = index
        else:
            trans_str = self.translate_post(text)
        return trans_str


class BDTranslate:
    cookie = ''

    def __init__(self):
        self.js = execjs.compile("""
            function sign(r) {
        var window = [];

        function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var a = o.charAt(t + 2);
                a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                    a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                    r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
            }
            return r
        }

        var i = null;

        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))

        var u = void 0
            , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
        u = null !== i ? i : (i = window[l] || "") || "";
        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
            var A = r.charCodeAt(v);
            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                S[c++] = A >> 18 | 240,
                S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                S[c++] = A >> 6 & 63 | 128),
                S[c++] = 63 & A | 128)
        }
        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
            p += S[b],
                p = n(p, F);
        return p = n(p, D),
            p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
            p %= 1e6,
        p.toString() + "." + (p ^ m)

    }
            """)

    # 计算js加密tk值
    def getSign(self, text):
        return self.js.call("sign", text)

    # 获取token
    def getGtk(self, html):
        li = re.findall("window.gtk = '(.*?)';", html)
        if len(li) == 1:
            return li[0]
        else:
            return ''

    def getToken(self, html):
        li = re.findall("token: '(.*?)',", html)
        if len(li) == 1:
            return li[0]
        else:
            return ''

    def getHtml(self):
        r = requests.get(url='http://fanyi.baidu.com/?aldtype=16047')
        r.encoding = 'UTF-8'
        self.cookie = r.cookies['BAIDUID']
        return r.text

    # sign的值，token和cookie自己获取的不行。
    def getResultByPC(self, text):
        html = self.getHtml()
        token = self.getToken(html)
        # gtk=self.getGtk(html)
        # sign=self.getSign(text)
        sign = '54706.276099'
        url = 'http://fanyi.baidu.com/v2transapi'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Cookie': 'BAIDUID=' + self.cookie,
            # 'Cookie':'BAIDUID=03B27B8BDC40FABA64046D65784F8CFE:FG=1',
        }
        data = {
            'from': 'en',
            'to': 'zh',
            'query': text,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': sign,
            'token': '9b8bb341109338ba7e875bd9a9dd88ba',
        }

        r = requests.post(url=url, data=data, headers=headers)
        r.encoding = 'UTF-8'
        result = r.text

        print(result)

    # 通过手机协议进行翻译
    def getResultByPhone(self, text):
        url = 'http://fanyi.baidu.com/basetrans'
        data = {
            'from': 'en',
            'to': 'zh',
            'query': text,
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        }
        r = requests.post(url=url, data=data, headers=headers)
        json_data = json.loads(r.content.decode())
        result = json_data['trans'][0]['dst']
        return result


class Translate(GGTranslate, BDTranslate):

    def get_result_by_baidu(self, text):
        bdTrans=BDTranslate()
        result = bdTrans.getResultByPhone(text)
        return result

    def get_result_by_google(self, text):
        ggTrans=GGTranslate()
        result = ggTrans.getResultGetByLines(text)
        return result
