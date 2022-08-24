from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('<int:id>',views.index,name="index"),
    path('techdata/<int:id>',views.techdata,name="techdata"),
    path('log',views.signin,name="signin"),
    path('register',views.register,name="register"),
    path('logout',views.logout_view,name="logout"),
]