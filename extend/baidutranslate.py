import requests
import json
import execjs
import re


class Translate:
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
        if len(li)==1:
            return li[0]
        else:
            return ''

    def getToken(self, html):
        li = re.findall("token: '(.*?)',", html)
        if len(li)==1:
            return li[0]
        else:
            return ''

    def getHtml(self):
        r = requests.get(url='http://fanyi.baidu.com/?aldtype=16047')
        r.encoding = 'UTF-8'
        self.cookie = r.cookies['BAIDUID']
        return r.text
    #sign的值，token和cookie自己获取的不行。
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

    #通过手机协议进行翻译
    def getResultByPhone(self,text):
        url='http://fanyi.baidu.com/basetrans'
        data={
            'from':'en',
            'to':'zh',
            'query':text,
        }
        headers={
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        }
        r=requests.post(url=url,data=data,headers=headers)
        json_data = json.loads(r.content.decode())
        result=json_data['trans'][0]['dst']
        return result