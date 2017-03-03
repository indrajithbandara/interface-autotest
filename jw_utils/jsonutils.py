# -*- coding: utf-8 -*-
import json
import time


info={}
info["code"]=1
info["id"]=1900
info["name"]='张三'
info["sex"]='男'

list=[info,info,info]


data={}

data["code"]=1
data["id"]=1900
data["name"]='张三'
data["sex"]='男'
data["info"]=info
data["data"]=list

jsonStr = json.dumps(data)

print "jsonStr:",jsonStr


def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)


def load():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data



if __name__ == "__main__":

    data = {}
    data["last"]=time.strftime("%Y%m%d")
    store(data)

    data = load()
    print data["last"]