# -*- coding: utf-8 -*-
#encoding:utf-8
#!/usr/bin/python
#print a.decode('gbk')
#dict={"a":"apple","b":"banana","o":"orange"}
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dict={"error":"ä¸å¡å¼å¸¸","errorCode":"300001","errorDes":"","errorMessage":"","responseCommonDto":{"errorLevel":"5","lans":"","message":"300001","resultCode":"1","sessionKey":"","token":"a1dafd56-d5f7-45ba-a335-457daa57bdd3","tracerId":""}}
print "##########dict######################"
for i in dict:
    print "dict[%s]=" % i,dict[i]
    print str(dict[i]).decode('gbk')

print "###########items#####################"
for (k,v) in  dict.items():
    print "dict[%s]=" % k,v

print "###########iteritems#################"
for k,v in dict.iteritems():
    print "dict[%s]=" % k,v

print "###########iterkeys,itervalues#######"
for k,v in zip(dict.iterkeys(),dict.itervalues()):
    print "dict[%s]=" % k,v

dict1 = {1: {2: {3: {4: {}}}}}
dict2 = {1: {2: {4: {6: {}}}}}
dict3 = {1: {2: {3: {5: {}}}}}

def deepSearch(dict1, dict2):
    for key in dict2.keys():
        if key not in dict1.keys():
            dict1[key] = dict2[key]
        else:
            deepSearch(dict1[key], dict2[key])

for dictT in [dict2, dict3]:
    deepSearch(dict1, dictT)

print(dict1)


# -*- coding: utf-8 -*-
# file: example1.py
import string

# 这个是 str 的字符串
s = '关关雎鸠'

# 这个是 unicode 的字符串
u = u'关关雎鸠'

print isinstance(s, str)      # True
print isinstance(u, unicode)  # True

# 从 str 转换成 unicode
print s.decode('utf-8')   # 关关雎鸠

# 从 unicode 转换成 str
print u.encode('utf-8')   # 关关雎鸠

print s.__class__   # <type 'str'>
print u.__class__   # <type 'unicode'>


user = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
user_obj = eval( user )
print " the user_obj@@@@@@@@@@@@@@@@@@",user_obj


my_string = "abcdef"

assert "a" in my_string

a = 123
assert type(a) == int,'a is type of int'


# 常用
# assertEqual(a, b)     a == b
# assertNotEqual(a, b)     a != b
# assertTrue(x)     bool(x) is True
# assertFalse(x)     bool(x) is False
# assertIs(a, b)     a is b     2.7
# assertIsNot(a, b)     a is not b     2.7
# assertIsNone(x)     x is None     2.7
# assertIsNotNone(x)     x is not None     2.7
# assertIn(a, b)     a in b     2.7
# assertNotIn(a, b)     a not in b     2.7
# assertIsInstance(a, b)     isinstance(a, b)     2.7
# assertNotIsInstance(a, b)     not isinstance(a, b)     2.7
# 其它
# assertAlmostEqual(a, b)     round(a-b, 7) == 0
# assertNotAlmostEqual(a, b)     round(a-b, 7) != 0
# assertGreater(a, b)     a > b     2.7
# assertGreaterEqual(a, b)     a >= b     2.7
# assertLess(a, b)     a < b     2.7
# assertLessEqual(a, b)     a <= b     2.7
# assertRegexpMatches(s, re)     regex.search(s)     2.7
# assertNotRegexpMatches(s, re)     not regex.search(s)     2.7
# assertItemsEqual(a, b)     sorted(a) == sorted(b) and works with unhashable objs     2.7
# assertDictContainsSubset(a, b)     all the key/value pairs in a exist in b     2.7
# assertMultiLineEqual(a, b)     strings     2.7
# assertSequenceEqual(a, b)     sequences     2.7
# assertListEqual(a, b)     lists     2.7
# assertTupleEqual(a, b)     tuples     2.7
# assertSetEqual(a, b)     sets or frozensets     2.7
# assertDictEqual(a, b)     dicts     2.7
# assertMultiLineEqual(a, b)     strings     2.7
# assertSequenceEqual(a, b)     sequences     2.7
# assertListEqual(a, b)     lists     2.7
# assertTupleEqual(a, b)     tuples     2.7
# assertSetEqual(a, b)     sets or frozensets     2.7assertDictEqual(a, b)     dicts     2.7
fl = [ (lambda n,i=i: i+n) for i in range(5)]
for k in range(5):
    print "fl[%d]: " %k,fl[k](4)

# #B tree
# class TreeNode:
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None
#
# def builtTree():
#     root=None
#     val=input("Enter the value:")
#     if(val=='#'):
#         pass
#     else:
#         root=TreeNode(val)
#         root.left=builtTree()
#         root.right=builtTree()
#     return root
#
# def PreTraver(root):
#     if root==None:
#         return
#     else:
#         print(root.val,end=" ")
#         traver(root.left)
#         traver(root.right)
#
#     def MidTraver(root):
#         if root==None:
#             return
#         MidTraver(root.left)
#         print(root.val,end=" ")
#         MidTraver(root.right)
#
#     def ReTraver(root):
#         if root==None:
#             return
#         ReTraver(root.left)
#         ReTraver(root.right)
#         print(root.val,end=" ")
#
#         def deepth(root):
#             if root==None:
#                 return 1
#             leftDeepth=deepth(root.left)+1
#             rightDeepth=deepth(root.right)+1
#             if leftDeepth>rightDeepth:
#                 return leftDeepth
#             else:
#                 return rightDeepth
#
#         def main():
#             root=builtTree()
#             if(root==None):
#                 print("builtTree failed")
#
#
#         if __name__=='__main__':
#             main()
#         else:
#             print("test.py has worked")

str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);