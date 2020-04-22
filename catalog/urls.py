from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name = "detail")

]