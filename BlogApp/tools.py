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
    if request.method == "POST":
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT count(user_id) FROM blogapp_profiles_follower where profiles_id = 1;
        """)
        data_dict = dictfetchall(cursor)
        

        follow_count = dictfetchall(cursor)

        response = {}
        response['data'] = data_dict
        context = {}
        context['data'] = response

        return render(request, "registration/user_stats.html", context)
        # return response


def get_who_liked_this_post(post_id):
    cursor = connection.cursor()
    id = post_id
    cursor.execute("""
        SELECT username, blogapp_profiles.id   from blogapp_posts_likes
        INNER  JOIN auth_user on auth_user.id=blogapp_posts_likes.user_id
        INNER  JOIN blogapp_profiles on auth_user.id=blogapp_profiles.user_id
        INNER  JOIN blogapp_posts on blogapp_posts.id=blogapp_posts_likes.posts_id
        where posts_id = %s and 5=%s""", params=(str(id), 5))

    data_dict = dictfetchall(cursor)

    return data_dict



def user_profile_checker(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT auth_user.id FROM dbblog.auth_user
        INNER JOIN blogapp_profiles on auth_user.id=blogapp_profiles.user_id
        WHERE blogapp_profiles.id = %s and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)

    return data_dict[0]['id']
def get_follows(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT username, blogapp_profiles.id FROM dbblog.auth_user
        INNER JOIN blogapp_profiles on auth_user.id=blogapp_profiles.user_id
        WHERE blogapp_profiles.id in(SELECT profiles_id 
        FROM dbblog.blogapp_profiles_follower 
        WHERE user_id=(SELECT auth_user.id FROM dbblog.auth_user
        INNER JOIN blogapp_profiles on auth_user.id=blogapp_profiles.user_id
        WHERE blogapp_profiles.id = %s)) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict
def get_followers(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT username, blogapp_profiles.id FROM dbblog.auth_user
        INNER JOIN blogapp_profiles on auth_user.id=blogapp_profiles.user_id
        WHERE auth_user.id in (SELECT user_id FROM dbblog.blogapp_profiles_follower
        WHERE profiles_id=%s) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict

def get_liked_posts(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT posts_id, title FROM dbblog.blogapp_posts_likes
        INNER  JOIN blogapp_posts on blogapp_posts.id=blogapp_posts_likes.posts_id
        INNER  JOIN auth_user on auth_user.id=blogapp_posts_likes.user_id
        WHERE blogapp_posts_likes.user_id in (SELECT user_id FROM dbblog.blogapp_profiles
        WHERE id=%s) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict





