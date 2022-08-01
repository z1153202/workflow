#!/usr/bin/env python
# coding=utf-8
import datetime
import requests
url = 'http://httpbin.org/get'
resp = requests.get(url)
data = resp.json()
print(data)