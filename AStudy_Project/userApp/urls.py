from django.urls import path
from . import views

urlpatterns = [
    path('body', views.body1, name = 'body'),
    path('index', views.index1, name = 'index'),
    path('layout1', views.lay1, name = 'layout1'),
    path('', views.login_user, name = 'login'),
    path('register1', views.register1, name = 'register1'),
    path('logout1', views.logout_user, name = 'logout1'),
    path('main' , views.main , name = "main") , 
    path('tags' , views.htmltags , name='tags') ,
    path('viewSubTopics/<int:id>' , views.viewSubTopics , name='viewSubtopics') ,
    path('viewContant/<int:ids>' , views.viewContent , name='viewContant') ,

]