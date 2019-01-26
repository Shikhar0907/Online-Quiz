"""Handy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path

from userlogin import views
from userlogin.views import QuesListSearchAPIView, QuesCreateAPIView, QuesDetailAPIView, QuesUpdateAPIView, QuesDeleteAPIView

urlpatterns = [
    path('', views.indexpage,name='index'),
    path('loginpage/', views.loginpage,name='login'),
    path('quiz/', views.quiz,name='Quiz'),
    path('loginpage/result/', views.answers,name='result'),
    path('userresults/', views.resultpage,name='userresult'),
    path('admin/view', views.question_view,name='QuestionView'),
    path('admin/leaders', views.leaders,name='Leaders'),
    path('admin/create', QuesCreateAPIView.as_view()),
    re_path(r'admin/(?P<id>\d+)/$', QuesDetailAPIView.as_view()),
    re_path(r'admin/(?P<id>\d+)/update/$', QuesUpdateAPIView.as_view()),
    re_path(r'admin/(?P<id>\d+)/delete/$', QuesDeleteAPIView.as_view()),
    path('admin/search',QuesListSearchAPIView.as_view()),
    path('admin/', admin.site.urls),
]
