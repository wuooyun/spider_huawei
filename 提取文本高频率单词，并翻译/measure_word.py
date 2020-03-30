#拿到文件路径 输入目录或文件
#格式化内容（全小写、空白取代特殊字符）  输入文件路径 输出格式化内容
#对单词进行统计 对单词和单词出现次数做映射存储
#按照需求展现数据

import os
import string
import re
import sys
import json,requests

def filepath(filespath):
    dirs = os.listdir(filespath)
    for dir in dirs:
        full_path = filespath + dir
        if os.path.isdir(full_path):
            yield from filepath(full_path+'\\')
        elif os.path.isfile(full_path):
            yield full_path

def format_content(filenames):
    rule = re.compile('[%s]' % re.escape(string.punctuation))
    words={}
    for fname in filenames:
        txt = open(fname,'r',encoding="utf-8").read()
        txt = rule.sub(' ',txt).lower()
        all_words = txt.split(' ')
        for word in all_words:
            if word in words:
                words[word] = words[word] +1
            else :
                words[word] = 1
    return words

def translate(word):
    """发出请求"""
    url = 'http://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q='
    response = requests.get(url + word)
    raw = json.loads(response.text)
    if raw[0][0][0]:
        return raw[0][0][0]
    else:
        return ' '

if __name__ == "__main__":
    thepath = "E:\\win10下载\\python-3.8.2-docs-text\\"
    fnames =  filepath(thepath)
    words = format_content(fnames)
    words = list(words.items())
    words.sort(key=lambda k: k[1],reverse=True)
    with open('E:\\words.txt','w',encoding='utf-8') as f:
        for word in words:
            if word[0]:
                print(type(word))
                fword = word[0]+str(word[1])+translate(word[0])
                f.write(word[0]+str(word[1])+translate(word[0])+'\n')
        
