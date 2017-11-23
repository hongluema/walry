# encoding:utf-8
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import traceback

def wrap(func):
    @csrf_exempt
    def wrapper(request):
        content = {"status":200}
        response = HttpResponse(content_type='application/json')
        response["Access-Control-Allow-Origin"] = "*"
        try:
            func(request,response,content)
            response.content = json.dumps(content)
        except BaseException,e:
            content["status"] = 500
            content["msg"] = "服务器错误"
            response.content = json.dumps(content)
            traceback.print_exc()
        return response
    return wrapper

#获取微信用户信息
import urllib2
def code_token_(code):
    try:
        # appId = "wx3ba1c32fa31b5c3f"
        appId = "wx6ed0e6f2f53cbe23"
        # appSecrect = 'd393d094016593bf9c37cb71689d772a'
        appSecrect = '9f59bc443662c34c031c2fa69d4a8856'
        address = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=' + appId + '&secret=' + appSecrect + \
                  '&code=' + code + '&grant_type=authorization_code'
        # address = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appId + \
        #           "&secret=" + appSecrect
        temp = eval(urllib2.urlopen(url=address).read())
        print "1.temp",temp
        access_token = temp['access_token']
        open_id = temp['openid']
        info_address = 'https://api.weixin.qq.com/sns/userinfo?access_token=' + access_token + '&openid=' + open_id + '&lang=zh_CN'
        info_temp = eval(urllib2.urlopen(url=info_address).read())
    except Exception, e:
        print str(e)
        info_temp = {}
    return info_temp
