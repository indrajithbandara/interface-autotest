
# -*- encoding: utf8 -*-

/*
Copyright 2016 JointWisdom Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

import json #导入json格式


data1 = {'b': 789, 'c': 456, 'a': 123}
encode_json = json.dumps(data1)
print type(encode_json), encode_json

decode_json = json.loads(encode_json)
print type(decode_json)
print decode_json['a']
print decode_json


data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
data_string = json.dumps(data)
print 'ENCODED:', data_string
decoded = json.loads(data_string)
print 'DECODED:', decoded
print 'ORIGINAL:', type(data[0]['b'])
print 'DECODED :', type(decoded[0]['b'])


data=[{'a':"A",'b':(2,4),'c':3.0}]    //list数据类型
 print data
//输出为：[{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
print len(data)
//输出1
print data[0]
//输出{'a': 'A', 'c': 3.0, 'b': (2, 4)}


//编码
data_dump=json.dumps(data)    //编码
print len(data_dump)    //转换为字符串了
//输出 35
 print data_dump
//输出 [{"a": "A", "c": 3.0, "b": [2, 4]}]
print data_dump[0]
//输出： [

//进行解码
data_loads=json.loads(data_dump)
print data_loads
//输出：[{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]
print len(data_loads)
//输出 1
print data_loads[0]
//输出：{u'a': u'A', u'c': 3.0, u'b': [2, 4]}


dict_ = {1:2, 3:4, "55":"66"}

# test json.dumps

print type(dict_), dict_
json_str = json.dumps(dict_)
print "json.dumps(dict) return:"
print type(json_str), json_str

# test json.loads
print "\njson.loads(str) return"
dict_2 = json.loads(json_str)
print type(dict_2), dict_2


if __name__ == "__main__":
   #datas = get_multiple_data()
   #print(datas)
   datas = {"text":"中文","polyline":"116.621248,41.02831"}
   fl=open('../out/map_polyline.js', 'w')
   #fl=open('../out/map_polyline.js', 'a')
   fl.write("var polyline_data=")
   #fl.write(json.dumps(datas))
   fl.write(json.dumps(datas,ensure_ascii=False,indent=2))
   fl.close()
