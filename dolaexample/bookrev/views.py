from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse 
from .models import Book 

def index(request):
#for loop here
	return render(request, "index.html" ,locals())

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user= auth.authenticate(username=username, password=password)

		if user is not None:
			if user.is_authenticated or user.is_active:
				auth.login(request,user)
				return redirect('/homepage/')
			else:
				message = 'User Not Found'

	return render(request,"login.html",locals())

def register(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		try:
			user = User.objectsget(username=username)
		except:
			user = None
		if user is not None:
			message = 'The Name is Taken'
		else:
			user = User.objects.create_user(username,password)

			user.save()

			message = "You can login now"
			return redirect('/homepage/')

	return render(request,'register.html',locals())

def homepage(request):
	book = Book.objects.all()
	bookname = request.POST.get('bookname',False)
	author = request.POST.get('author',False)
	genre = request.POST.get('genre',False)
	ratings = request.POST.get('ratings',False)
	Book.objects.create(bookname=bookname, author=author, genre=genre, ratings=ratings)
	review = Book.objects.all()

	return render(request,'homepage.html',{'book':book, 'bookname':bookname, 'author':author, 'genre':genre,'ratings':ratings, 'review':review})

def myprofile(request):

	return render(request,)

def logout(request):
	auth.logout(request)
	return redirect('/index/')



