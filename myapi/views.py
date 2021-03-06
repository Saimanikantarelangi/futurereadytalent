from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserForm,CommentForm,UpdateForm
from .models import Posts,User
import requests

def home(request):
    data = Posts.objects.all().order_by('title')
    return render(request,'home.html',{'data':data,})




def register(request):
   if request.method == "POST":

     form=UserForm(request.POST)
     if form.is_valid():
        form.save()
        return render(request,"login.html")

     else:
        return HttpResponse("invalid")

   else:
      form=UserForm()


   return render(request, 'register.html',{"form":form})
def login(request):
   if request.method == 'POST':
      username=request.POST["uname"]
      pass1=request.POST["upass"]
      ex=User.objects.get(Username=username)

      if username==ex.Username and pass1==ex.pass1:
         request.session['username'] = ex.Username
         data = Posts.objects.all().order_by('title').filter(Username=ex)
         return render(request,"home.html",{'data':data,'username':username})
      else:
         return HttpResponse("invalid")
   else:
    return render(request,"login.html")

def search(request):
    res = request.GET['query']
    respons = Posts.objects.filter(Q(title__icontains=res) | Q(content__icontains=res) | Q(aurt__icontains=res))
    return render(request,'search.html',{'respons':respons,'res':res})

def contact(request):
    return HttpResponse(request,'contact.html')
def latest(request):
    ldata = Posts.objects.all().order_by('-date')
    return render(request,'welcome.html',{'ldata':ldata})
def addpost(request):
    if request.method == "POST":
        title = request.POST["utitle"]
        content = request.POST["ucontent"]
        image=request.POST["uimage"]
        username = request.session['username']

        ex = User.objects.get(Username=username)
        request.session['username'] = ex.Username

        p = Posts(title=title, content=content,Username=ex,image=image)
        p.save()
        data=Posts.objects.filter(Username=ex)
        context={
            "data":data,
        }

        return render(request,"home.html",context)
        #
    else:

        return render(request,"addpost.html")
def postdetail(request,id):

    pdata= Posts.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = pdata
            comment.save()

            return redirect('postdetail',id=pdata.id)
    else:
        form = CommentForm()

    return render(request, "post_detail.html", {'pdata': pdata, 'form': form,"id":pdata.id})

def delete(request,id):
        dat = get_object_or_404(Posts, id=id)
        dat.delete()
        return  redirect("show")
def show(request):
    e = request.session['username']
    ex = User.objects.get(Username=e)
    data = Posts.objects.all().order_by('title').filter(Username=ex)
    return render(request, "home.html", {'data': data, 'username': ex})

def update(request,id):
    data = get_object_or_404(Posts, id=id)



    form = UpdateForm(request.POST or None, instance=data)
    if form.is_valid():
            form.save()
            e=request.session['username']
            ex=User.objects.get(Username=e)
            return redirect("show")
    context = {
        "form": form,
        'data':data

    }
    return render(request, 'update.html', context)








# Create your views here.
