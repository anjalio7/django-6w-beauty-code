from django.shortcuts import *
from django.db import IntegrityError
from adminApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User , auth
def signin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            data = topics.objects.all()
            return render(request,'userApp/inner.html',{'data':data})
            # return HttpResponse(username + password)
        else:
            message = "invalid credentials"
            return render(request,'userApp/signin.html',{'message':message})
    else:
        return render(request,'userApp/signin.html')

def logout_view(request):
    logout(request)
    return redirect('signin')

def home(request):
    data = topics.objects.all()
    return render(request,'userApp/inner.html',{'data':data})

def index(request,id):
    obj = subtopics.objects.filter(topic_id_id=id)
    data = topics.objects.all()
    contentData = content.objects.filter(subtopic_id = obj[0].id)
    return render(request,'userApp/home.html',{'data':data,'value':obj, 'val': contentData})

# def techdata(request,id):
#     data = topics.objects.all()
#     obj = subtopics.objects.all()
#     subData = subtopics.objects.get(id = id)
#     value = content.objects.filter(subtopic_id = subData)
#     return render(request,'userApp/techdata.html',{'data':data,'value':obj,'val':value})
def techdata(request,id):
    subData = subtopics.objects.get(id = id)
    selTopic = topics.objects.get(id = subData.topic_id.id)
    subTopicData = subtopics.objects.filter(topic_id = selTopic)
    value = content.objects.filter(subtopic_id = subData)
    data = topics.objects.all()
    return render(request,'userApp/techdata.html',{'data':data, 'value':subTopicData,'val':value})


def register(request):
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password == confirmation:
            # Attempt to create new user
            try:
                user_reg = user.objects.create_user(username=username,email=email, password=password)
                user_reg.save()
            except IntegrityError:
                message = "Username already taken."
                return render(request, "userApp/register.html", {'message' : message})
            message = "Registered successfully.."
            return render(request, 'userApp/signin.html', {"message": message})
        else:
            message = "Passwords must match."
            return render(request, "userApp/register.html", {
                            "message": message
                        })
    else:
        return render(request, "userApp/register.html")