from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from apartapp.models import MarketerDetail

# Create your views here.
def credits(request):
    u = User.objects.get(username=request.user.username)
    post_list=u.marketerdetail
    print(post_list.credits)
    print(post_list.username)
    return render(request,"blog/credits.html",{'post_list':post_list})
def referandearn(request):
    return render(request,"blog/referandearn.html")
def earncredits(request):
    return render(request,"blog/earn_credits.html",)
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login1.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
