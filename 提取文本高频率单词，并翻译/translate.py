
"""google 单词翻译 API"""

# ringsaturn
# 2017-12-22

import json
import sys

import requests

def translate(word):
    """发出请求"""
    url = 'http://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q='
    response = requests.get(url + word)
    raw = json.loads(response.text)
    return raw[0][0][0]

