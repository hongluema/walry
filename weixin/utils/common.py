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
            content["status"] = 300
            content["msg"] = "服务器错误"
            response.content = json.dumps(content)
            traceback.print_exc()
        return response
    return wrapper