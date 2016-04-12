from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def userLogin(request):
	data={}
	if request.method=='GET':
		data={'form':LoginForm()}
	elif request.method=='POST':
		loginForm=LoginForm(request.POST)
		result=False
		msg=''
		if loginForm.is_valid():
			email=loginForm.cleaned_data['email']
			password=loginForm.cleaned_data['password']
			user=None
			try:
				user=User.objects.get(email=email)
			except User.DoesNotExist:
				user=None
			user=authenticate(username=user.username, password=password)
			if user:
				login(request,user)
				result=True
				msg='You are logged in'
				print msg
			else:
				result=False
				msg='Invalid email and password combination.'
		else:
			result=False
			msg='Invalid values'
		if not result:
			data['form']=loginForm
			data['result']=result
			data['msg']=msg
			return render(request,'login.html',data);
		else:
			return render(request,'list_expense.html',data);

def userLogout(request):
	logout(request)
	data={'form':LoginForm()}
	return redirect('/login/')