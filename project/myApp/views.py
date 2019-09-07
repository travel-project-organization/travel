

#首页
def index(request):
    return render(request,'myApp/index.html')


#显示地图界面
def map(request):
    return render(request,'myApp/map.html')

def arrange(request):
    return render(request,'myApp/arrange.html')

from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import user
 # Create your views here.
class UserForm(forms.Form):
     username = forms.CharField(label='用户名',max_length=50)
     password = forms.CharField(label='密码',widget=forms.PasswordInput())
     email = forms.EmailField(label='邮箱')


#注册
def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
             username = userform.cleaned_data['username']
             password = userform.cleaned_data['password']
             email = userform.cleaned_data['email']

             user1 = user.objects.filter( uemail__exact=email)
             if user1:
                 return HttpResponse('该邮箱已注册')
             else:
                User.objects.create_user(username=username, password=password, email=email)
                user.objects.create(uname=username,upass=password,uemail=email)
                #User.save()
                return HttpResponseRedirect('login')

                #return render_to_response('myApp/login.html', {'userform': userform})
    else:
        userform = UserForm()
    return render_to_response('myApp/regist.html',{'userform':userform})
from django.contrib.auth import login, authenticate
from  django.contrib.auth.models import User
from .models import user
#登录时获取的数据
class UserLog(forms.Form):
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    username = forms.CharField(label='用户名', max_length=50)

#登录
def Login(request):
     if request.method == 'POST':
         userform = UserLog(request.POST)
         if userform.is_valid():
             username = userform.cleaned_data['username']
             password = userform.cleaned_data['password']


             #user1 = user.objects.filter(uemail__exact=email,upass__exact=password).first()
             user2 = authenticate(username=username, password=password)
             if user2 is not None:
                 login(request,user2)
                 #request.session["login_user"] = user.uname
                 return HttpResponseRedirect('index')
                 #return render(request, 'myApp/index.html',{'userform':userform})
                 #return render_to_response('myApp/index.html',{'userform':userform})
             else:
                 return HttpResponse('用户名或密码错误,请重新登录')

     else:
         userform = UserForm()
     return render_to_response('myApp/login.html',{'userform':userform})