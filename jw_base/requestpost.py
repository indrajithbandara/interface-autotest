#!/usr/bin/env python
#coding=utf8
import json
import requests

url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
print r.text

#http://www.yiibai.com/html/postgresql/2013/080998.html