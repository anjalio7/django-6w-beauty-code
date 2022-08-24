from django.urls import path
from . import views

urlpatterns = [
    path('body', views.body, name = 'body'),
    path('index', views.index, name = 'index'),
    path('', views.login_view, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout_view, name = 'logout'),
    path('addtopics' , views.addTopics_name , name = "addtopics" ) , 
    path('allTopic' , views.allTopics , name= "allTopic") ,
    path('editTopic/<int:ids>' , views.editTopics , name= "edit-topic") ,
    path('deletetopic/<int:ids>' , views.deleteTopic , name= "delete-topic") ,
    path('subtopics' , views.sub_topicName , name = 'subtopics') ,
    path('addsubtopics' , views.addsub_topics , name = 'addsubtopics') ,
    path('allsubTopic' , views.all_subTopics , name= "allsubTopic") ,
    path('edit-subTopic/<int:ids>' , views.edit_subTopics , name= "edit-subtopic") ,
    path('delete-subtopic/<int:ids>' , views.delete_subTopic , name= "delete-subtopic") ,
    path('add-content' , views.add_content , name = 'add-content'),
    path('viewContent' , views.view_content , name = 'viewContent') ,
    path('editContent/<int:idss>' , views.edit_content , name = 'editContent') ,
    path('deleteContent/<int:idss>' , views.delete_content , name = 'deleteContent'), 
    ]
