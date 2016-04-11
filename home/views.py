from django.shortcuts import render
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.models import User
# Create your views here.
def login(request):
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
			if user:
				if user.check_password(password):
					login(request,user)
					result=True
					msg='You are logged in'
				else:
					result=False
					msg='Invalid password!!'
			else:
				result=False
				msg='You are not registered'
		else:
			result=False
			msg='Invalid values'
		if not result:
			data['form']=loginForm
		data['result']=result
		data['msg']=msg
	return render(request,'login.html',data);