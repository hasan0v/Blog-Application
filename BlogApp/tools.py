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
def get_who_liked_this_post(post_id):
    cursor = connection.cursor()
    id = post_id
    cursor.execute("""
        SELECT username, blogapp_profile.id   from blogapp_post_likes
        INNER  JOIN auth_user on auth_user.id=blogapp_post_likes.user_id
        INNER  JOIN blogapp_profile on auth_user.id=blogapp_profile.user_id
        INNER  JOIN blogapp_post on blogapp_post.id=blogapp_post_likes.post_id
        where post_id = %s and 5=%s""", params=(str(id), 5))

    data_dict = dictfetchall(cursor)

    return data_dict



def user_profile_checker(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT auth_user.id FROM dbblog.auth_user
        INNER JOIN blogapp_profile on auth_user.id=blogapp_profile.user_id
        WHERE blogapp_profile.id = %s and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)

    return data_dict[0]['id']
def get_follows(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT username, blogapp_profile.id FROM dbblog.auth_user
        INNER JOIN blogapp_profile on auth_user.id=blogapp_profile.user_id
        WHERE blogapp_profile.id in(SELECT profile_id 
        FROM dbblog.blogapp_profile_follower 
        WHERE user_id=(SELECT auth_user.id FROM dbblog.auth_user
        INNER JOIN blogapp_profile on auth_user.id=blogapp_profile.user_id
        WHERE blogapp_profile.id = %s)) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict
def get_followers(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT username, blogapp_profile.id FROM dbblog.auth_user
        INNER JOIN blogapp_profile on auth_user.id=blogapp_profile.user_id
        WHERE auth_user.id in (SELECT user_id FROM dbblog.blogapp_profile_follower
        WHERE profile_id=%s) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict

def get_liked_posts(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT post_id, title FROM dbblog.blogapp_post_likes
        INNER  JOIN blogapp_post on blogapp_post.id=blogapp_post_likes.post_id
        INNER  JOIN auth_user on auth_user.id=blogapp_post_likes.user_id
        WHERE blogapp_post_likes.user_id in (SELECT user_id FROM dbblog.blogapp_profile
        WHERE id=%s) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict


def get_user_posts(profile_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, title FROM dbblog.blogapp_post
        WHERE author_id = (SELECT user_id FROM blogapp_profile WHERE id=%s) and 5=%s""", params=(str(profile_id), 5))
    
    data_dict = dictfetchall(cursor)
    return data_dict


