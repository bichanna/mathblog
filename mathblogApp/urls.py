"""
	math blog app

	Filename: urls.py
	Date: Feb 16th, 2021
	Written by Nobuharu Shimazu 
"""

from django.urls import path
from . import views

app_name = "mathblogApp"

urlpatterns = [
	path("", views.post_list, name="post_list"),
]