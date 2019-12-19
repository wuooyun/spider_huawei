#!/usr/bin/python3

import requests
import re
import html
import lxml
from bs4 import BeautifulSoup,Comment


url = 'https://ilearningx.huawei.com/courses/course-v1:HuaweiX+EBGTC00000001+2018.7/courseware/81e26868fb984af9954f68873575564c/29186e587e4f47799482734869b7201c/'
host = 'https://ilearningx.huawei.com' 
## define request header
headers = {
    'Cookie' : '',
    'Connection' : 'keep-alive',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
unitNames = []



def get_mp4Url(PageUrls):
    result = []
    count = 0
    for url in PageUrls:
        result.append(unitNames[count])
        count += 1
        r =  requests.get(url,headers=headers)
        htmldate = html.unescape(r.text)
        soup = BeautifulSoup(htmldate)    ## 解析
        comments = soup.findAll(text=lambda text:isinstance(text,Comment)) ## 由于需要的内容在注释里，这里对注释提取后再lxml解析
        res = BeautifulSoup(str(comments),'lxml')
        ### 提取所在tag
        sources = res.find_all('source')        
        #ps 是不是考虑用yied 返回个生成器？
        for sou in sources: ### 最后提取该tag内的链接
            result.append(sou.get('src'))

        
    return result

def get_allPageUrl(url,headers):
    PageUrl = [] 
    #获取所有顶级Url内容
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.content,'lxml')
    allPages =  soup.find_all('a','accordion-nav')
    for page in allPages:
        full_url = host+page.get('href')
        PageUrl.append(full_url)
    pass
    #获取顶级url对应名称
    urlnames = soup.find_all('p',class_='accordion-display-name')
    for urlname in urlnames:
        unitName =  urlname.get_text("|", strip=True)
        unitNames.append(unitName)

    return PageUrl

PageUrl = get_allPageUrl(url,headers)
mp4Url = get_mp4Url(PageUrl)

fpath = r'C:\Users\Yun\Desktop\mp4url.txt'
with open(fpath,'w',encoding='utf-8') as f:
    for line in mp4Url:
        f.write(line+'\n')
    f.close()








