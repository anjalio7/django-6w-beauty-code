from email import message
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from adminApp.models import *
from adminApp.models import user , topics , subtopics


def body1(request):
    return render(request , 'userApp/body.html')

def lay1(request):
    return render(request , 'userApp/layout.html')

def index1(request):
    return render(request, 'userApp/index.html')

# Start login
def login_user(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("main") )

        else:
            return render(request, "userApp/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "userApp/login.html")

# End login

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register1(request):
    if request.method == "POST":
       
        username = request.POST["username"] 
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "userApp/register.html", {
                "message": "Passwords must match."
            })


        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
            print(users)
        except ValidationError as v:
                return render(request, 'userApp/register.html', {'message': 'Characters must be greater than 3.'})
        except IntegrityError:
            return render(request, "userApp/register.html", {
                "message": "Username already taken."
            })
        
        return render(request, 'userApp/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "userApp/register.html")

def main(request):
    return render(request , 'userApp/index.html')


#HTML tags
def htmltags(request):
    data = topics.objects.all()
    # sub = subtopics.objects.all()
    # print(sub)
    return render(request , 'userApp/htmltags.html',{'obj':data}) 



def viewSubTopics(request, id):
    if data.key<0 :
        datas = topics.objects.all()
        selTopic = topics.objects.get(id = id)
        data = subtopics.objects.filter(topic_id = selTopic)
        return render(request, 'userApp/htmltags.html', {'data': data, 'obj':datas})
    else:
        return render(request, "userApp/htmltags.html" , {"message": ' Something went wrong.'})

def viewContent(request , ids):
    selCon = subtopics.objects.get(id=ids)
    cont = content.objects.filter(subtopic_id = selCon)
    return render(request , 'userApp/htmltags.html' , {'content':cont})

