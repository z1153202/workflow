#!/usr/bin/env python
# coding=utf-8
import datetime
import requests
header = {
    'Host': 'www.zhihu.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'User-Agent': 'PostmanRuntime/7.17.1',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
}
url = 'https://www.zhihu.com/api/v4/members/guodongxiaren?include=follower_count%2cvoteup_count'
resp = requests.get(url)
data = resp.json()
print(data)