import requests
import chardet
import random
url = 'https://www.baidu.com'
response = requests.get(
    url,
    headers={'User-Agent':random.choice(user_agent)},
    proxies = random.choice(ips)
    )
#print(response.text)  #打印成文本格式
#获取编码
code = chardet.detect(response.content)['encoding']
#解码
response.encoding = code
print(response.text)#打印信息
