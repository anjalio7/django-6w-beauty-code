from email import message
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.

def body(request):
    return render(request , 'adminApp/body.html')

def index(request):
    topic = models.topics.objects.all().count()
    contents = models.content.objects.all().count()
    subtopics = models.subtopics.objects.all().count()
    return render(request, 'adminApp/index.html',{'topic':topic,'subtopics':subtopics,'contents':contents})

# Start login
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            if user.is_superuser :
                login(request, user)
                return HttpResponseRedirect(reverse("index") )
            else :
                return render(request, "adminApp/login.html", {
                "message": "Invalid username and/or password."
                })
        else:
            return render(request, "adminApp/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "adminApp/login.html")

# End login

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "adminApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = user.objects.create_user(username, email, password)
            user.save()
        except ValidationError as v:
                return render(request, 'adminApp/register.html', {'message': 'Characters must be greater than 3.'})
        except IntegrityError:
            return render(request, "adminApp/register.html", {
                "message": "Username already taken."
            })
        return render(request, 'adminApp/register.html', {"message": 'Registered successfully.'})
    else:
        return render(request, "adminApp/register.html")

@login_required(login_url="/")
def addTopics_name(request):
    if request.method == 'POST' :
        Topic_name = request.POST ['topic_name']
        add = models.topics(topic_name = Topic_name)
        add.save()
        return HttpResponseRedirect (reverse('allTopic') , )
    else:
        return render (request , 'adminApp/topic_name.html')

@login_required(login_url="/")
def allTopics(request): #view_topics
    allTopic = models.topics.objects.all()
    return render(request , 'adminApp/view_topics.html' , {'topic' : allTopic})

@login_required(login_url="/")
def editTopics (request , ids):
    topic = models.topics.objects.get(id=ids) #to fetch a paticular line
    if request.method == 'POST' :
        Topic = request.POST['topic_name']
        topic.topic_name = Topic
        topic.save()
        return HttpResponseRedirect(reverse('allTopic'))
    else:
        return render(request , 'adminApp/edit_topic.html' , {'data':topic})

@login_required(login_url="/")
def deleteTopic(request , ids):
    topic = models.topics.objects.get(id=ids)
    topic.delete()
    return HttpResponseRedirect(reverse('allTopic'))

@login_required(login_url="/")
def sub_topicName(request):
    topic = models.topics.objects.all()
    return render(request , 'adminApp/sub_topics.html', {'data': topic})

# End  topics

# Start sub topics
@login_required(login_url="/")
def addsub_topics(request): # view_subtopics
    topic = models.topics.objects.all()
    print(topic)
    if request.method == 'POST' :
        subTopic = request.POST['subtopics']
        selTopic = models.topics.objects.get(id = subTopic)
        name = request.POST['subtopic_name']
        iframeLink = request.POST['iframe']
        
        a = models.subtopics(topic_id = selTopic, subtopic_name = name, iframe = iframeLink)
        a.save()
        return HttpResponseRedirect(reverse('allsubTopic'))
    else:
        return render(request , 'adminApp/edit_subtopics.html' , {'data':topic})

@login_required(login_url="/")
def all_subTopics(request): #view_subtopics
    allsubTopic = models.subtopics.objects.all()
    print(allsubTopic)
    return render(request , 'adminApp/view_subtopics.html' , {'subtopic' : allsubTopic})

@login_required(login_url="/") 
def edit_subTopics (request , ids):
    subtopic = models.subtopics.objects.get(id=ids) #to fetch a paticular line
    topicss = models.topics.objects.all()
    if request.method == 'POST' :
        top = request.POST['subtopics']
        selTop = models.topics.objects.get(id = top)
        name = request.POST['subtopic_name']
        iframes = request.POST['iframe']

        subtopic.topic_id = selTop
        subtopic.subtopic_name = name
        subtopic.iframe = iframes
        subtopic.save()
        # subtopic.subtopic_name = subTopic
        # subtopic.save()
        return HttpResponseRedirect(reverse('allsubTopic'))
    else:
        return render(request , 'adminApp/edit_subtopics.html' , {'data':subtopic, 'topics': topicss})

@login_required(login_url="/")
def delete_subTopic(request , ids):
    subtopic = models.subtopics.objects.get(id=ids)
    subtopic.delete()
    return HttpResponseRedirect(reverse('subtopics'))

# Start Content
@login_required(login_url="/")
def add_content(request):
    subtopic = models.subtopics.objects.all()
    print(subtopic)
    if request.method == 'POST' :
        sub_Topic = request.POST['sub_Topics']
        selsubTopic = models.subtopics.objects.get(id = sub_Topic)
        title = request.POST['title']
        content = request.POST['content']
        print(selsubTopic,content)
        a = models.content(subtopic_id = selsubTopic, data = content,title =title)
        a.save()
        return HttpResponseRedirect(reverse('viewContent'))
    else:
        return render(request , 'adminApp/add_content.html', {'content':subtopic })

@login_required(login_url="/")
def view_content(request):
    data = models.content.objects.all()
    return render(request , 'adminApp/view_content.html', {'content': data})

@login_required(login_url="/")
def edit_content(request , idss):
    contents  =models.content.objects.get(id=idss)
    subtopic=models.subtopics.objects.all()
    if request.method == 'POST' :
        sub  = request.POST['sub_Topics']
        selSub = models.subtopics.objects.get(id = sub)
        title = request.POST['title']
        data = request.POST['contents']
        contents.data = data
        contents.title = title
        contents.subtopic_id = selSub
        contents.save()
        return HttpResponseRedirect(reverse('viewContent'))
    else :
        return render(request , 'adminApp/edit_content.html' , {'data':contents , 'sub' : subtopic})

@login_required(login_url="/")   
def delete_content(request , idss):
    contents = models.content.objects.get(id=idss)
    contents.delete()
    return HttpResponseRedirect(reverse('viewContent'))

# End Content