from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for key, values in errors.items():
                messages.error(request, values)
            return redirect('/')
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['name'] = new_user.first_name
        ## ADDED ID STORAGE IN SESSION
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        logged_user = User.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            if logged_user.password == request.POST['password']:
                request.session['name'] = logged_user.first_name
                request.session['user_id'] = logged_user.id
                return redirect('/success')
    return redirect('/')



def success(request):
    return render(request, 'success.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def albums(request):
    return render(request, 'albums.html')

def create_album(request):
    return render(request, 'create_album.html')

def upload(request):
# create a create command, post object
## CORRECTED CREATE COMMAND
## REVIEW CRUD SYNTAX, Class_Name.objects.create(field=value, field=value)
    post = Post.objects.create(image=request.POST['image'], author=User.objects.get(id=request.session['user_id']), desc=request.POST['description'])
## Corrected PRINT statement to print image url
    print(post.image)
# print image attribute
    return redirect('/albums')

def back(request):
    return redirect('/success')