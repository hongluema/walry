#encoding: utf-8
from django.shortcuts import render
import MySQLdb
from MySQLdb.cursors import DictCursor
from django.http import JsonResponse
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
    conn = MySQLdb.connect(host="570ddef683032.sh.cdb.myqcloud.com", user='root', passwd='N205U89KSY8X', port=5394)
    cursor = conn.cursor(DictCursor)
    cursor.execute("use community")
    sql = "select * from message where id=%s"
    cursor.execute(sql, (id,))
    task = cursor.fetone()
    cursor.close()
    conn.close()
    return JsonResponse({"status":200,"task":task})