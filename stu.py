import requests
from extend.googletranslate import Translate

with open('./str') as f:
    text=f.read()
trans=Translate()

trans_text=trans.getResultByWords(text)

print(trans)