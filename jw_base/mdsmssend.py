# -*- coding: utf-8 -*-
import httplib


def mdsmssend(sn,pwd,mobile,context):
    #定义发送报文
    SoapMessage ='''<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <mdsmssend xmlns="http://entinfo.cn/">
      <sn>%s</sn>
      <pwd>%s</pwd>
      <mobile>%s</mobile>
      <content>%s</content>
    </mdsmssend>
  </soap:Body>
</soap:Envelope>'''

    SoapMessage=SoapMessage %(sn,pwd,mobile,context)
    #使用的WebService地址为sdk.entinfo.cn:8061/webservice.asmx，
    webservice = httplib.HTTP("sdk.entinfo.cn:8061")
    #连接到服务器后的第一个调用。它发送由request字符串到到服务器
    webservice.putrequest("POST", "/webservice.asmx")
    webservice.putheader("Host", "sdk.entinfo.cn:8061")
    webservice.putheader("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(SoapMessage))
    webservice.putheader("SOAPAction", "\"http://entinfo.cn/mdsmssend\"")
    #发送空行到服务器，指示header的结束
    webservice.endheaders()
    #发送报文数据到服务器
    webservice.send(SoapMessage)
    #获取返回HTTP 响应信息
    statuscode, statusmessage, header = webservice.getreply()
    print statuscode
    print statusmessage
    return statuscode