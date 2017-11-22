#encoding: utf-8
from django.shortcuts import render
import MySQLdb
from MySQLdb.cursors import DictCursor
from django.http import JsonResponse
import traceback
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from weixin.utils.common import wrap
# Create your views here.


def find_task(request):
    if request.method == "POST":
        user_id = request.POST["uid"]
        conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
        cursor = conn.cursor(DictCursor)
        cursor.execute("use community")
        sql = "select * from message where user_id=%s"
        cursor.execute(sql, (user_id,))
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        # for t in tasks:
        #     print "start..."
        #     print ">>>id:", t["id"], "uid:", t["user_id"], "时间：", t["pub_time"], "剩余金额：", t["r_amount"], "总金额:", t[
        #         "t_amount"]
        return render(request,'weixin/findTask.html',{"tasks":tasks})
    else:
        return render(request, 'weixin/findTask.html')

def delete_task(request):
    id = request.GET["id"]
    print "id:",id
    conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
    cursor = conn.cursor(DictCursor)
    cursor.execute("use community")
    sql = "update from message set status = 2 where id=%s"
    cursor.execute(sql, (id,))
    task = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return JsonResponse({"status":200,"task":task})

def recover_task(request):
    id = request.GET["id"]
    conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
    cursor = conn.cursor(DictCursor)
    cursor.execute("use community")
    sql = "update from message set status = 1 where id=%s"
    cursor.execute(sql, (id,))
    task = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return JsonResponse({"status":200,"task":task})

#展示座位的页面
@csrf_exempt
def show_zuowei(request):
    status = {'status': 300, "data": "", "msg": ""}
    response = HttpResponse(content_type='application/json')
    try:
        car_number = request.POST.get("car_number","") #车牌号
        status["status"] = 200
        status["msg"] = "测试"
    except BaseException, e:
        traceback.print_exc()
        print ">>>error", str(e)
        status["msg"] = "服务器错误"
    response.content = json.dumps(status)
    response["Access-Control-Allow-Origin"] = "*"
    return response

#创建车辆每日运营记录
@wrap
def create_log(requst,response,content):

    content["msg"] = "你好"