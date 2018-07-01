import requests
from extend.googletranslate import Translate as GGTrans
from extend.baidutranslate import Translate as BDTrans
with open('./str') as f:
    text=f.read()
    text='Gwyneth Paltrow'
trans=BDTrans()
trans_text=trans.getResultByPhone(text)
print(trans_text)
trans=GGTrans()
trans_text=trans.getResultPostByLines(text)
print(trans_text)

