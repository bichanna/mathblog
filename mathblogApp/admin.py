
# Register your models here.
"""
Blogアプリ
admin用の設定

Filename admin.py
Date: Feb 15, 2021
Written by Nobuharu Shimazu
"""
from django.contrib import admin
from .models import Post


admin.site.register(Post)
