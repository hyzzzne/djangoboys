from django.urls import path
# 장고 함수인 path와 blog 애플리케이션에서 사용할 모든 views 를 import함(가져옴)
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]