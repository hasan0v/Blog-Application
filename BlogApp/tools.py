from sqlite3 import Cursor
from urllib import response
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json
from django.shortcuts import render
from django.template import loader
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def add_get_params(response):
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT'
    response["Access-Control-Allow-Headers"] = 'x-csrftoken, Content-Type'

@csrf_exempt
def stats(request, pk):
    # user = str(request.POST.get('user'))
    print('lolol', request.method, pk)
    if request.method == "POST":
        cursor = connection.cursor()
        
        print(pk)
        cursor.execute("""
            SELECT count(user_id) FROM blogapp_profiles_follower where profiles_id = 1;
        """)
        data_dict = dictfetchall(cursor)
        

        follow_count = dictfetchall(cursor)



        print(data_dict)
        response = {}
        response['data'] = data_dict
        print(response)
        context = {}
        context['data'] = response

        return render(request, "registration/user_stats.html", context)
        # return response












