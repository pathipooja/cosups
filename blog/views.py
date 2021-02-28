from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Orders,EarnCredits
from django.contrib.auth.models import User
from apartapp.models import MarketerDetail
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from blog import forms
from django.contrib.auth.decorators import login_required
def searchMatch(community,pincode,state,district,sub_colony,item):
    if item.available_in=="all":
        if (str(pincode).lower() in item.available_region.lower()) or (state.lower() in item.available_region.lower()) or (district.lower() in item.available_region.lower()) or (sub_colony.lower() in item.available_region.lower()):
            return True
        else:
            return False
    else:
        if (community==item.available_in) and ( (str(pincode).lower() in item.available_region.lower()) or (state.lower() in item.available_region.lower()) or (district.lower() in item.available_region.lower()) or (sub_colony.lower() in item.available_region.lower())):
            return True
        else:
            return False
# Create your views here.
# def addProduct(request):
#     form=forms.ProductForm
#     if request.method=="POST":
#         print(forms.ProductForm(request.POST))
#     return render(request,'blog/addproduct.html',{'form':form})
@login_required(login_url='login')
def post_list_view(request):
    try:
        marketerdetails = MarketerDetail.objects.get(username=request.user.id)
    except ObjectDoesNotExist:
        return redirect("addproduct")
    if not marketerdetails.verified:
        return render(request, 'blog/notverified.html')
    post_tot_list = Post.objects.all()
    if marketerdetails:
        post_list = [item for item in post_tot_list if
                     searchMatch(marketerdetails.Type_of_community, marketerdetails.pincode, marketerdetails.state,
                                 marketerdetails.district, marketerdetails.sub_colony, item)]
    else:
        post_list = post_tot_list
    if request.method == "GET":
        return render(request, 'blog/index1.html', {'post_list': post_list})
        return render(request, 'blog/post_list.html', {'post_list': post_list})
    # if request.method=="POST":
    #     username = request.POST['username']
    #     product_name= request.POST['product_name']
    #     address= request.POST['address']
    #     flatnumber= request.POST['flatnumber']
    #     print(username,flatnumber,product_name)
    #     if flatnumber=='self' and Orders.objects.filter(dealername=username).filter(productname=product_name).filter(flataddress="self").exists():
    #         messages.info(request,'Only one sample order allowed')
    #         return render(request,'blog/post_list.html',{'post_list':post_list})
    #     order_details=Orders.objects.create(dealername=username,flataddress=flatnumber,apartmentaddress=address,productname=product_name)
    #     order_details.save()
    #     messages.info(request,'Order placed successfully')
    #     return render(request,'blog/post_list.html',{'post_list':post_list})

@login_required(login_url='login')
def dashboard(request):
    order_list=Orders.objects.filter(dealername=request.user.username).order_by("-id")
    return render(request,"blog/cart.html",{'order_list':order_list})
def addproduct(request):
    return render(request,"blog/addproduct.html")
def registermarketer(request):
    return render(request,"blog/marketerform.html")
def registermanufacturer(request):
    return render(request,"blog/manifacturerform.html")
def earncredits(request):
    post_list= EarnCredits.objects.all()
    return render(request, 'blog/earn_credits.html', {'post_list':post_list})
@login_required(login_url='login')
def post_detail_view(request,year,month,day,post):
    print("++++++++++++"+request.user.username)
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    post1=post
    if request.method=="POST":
        u = User.objects.get(username=request.user.username)
        username = request.POST['username']
        product_name= post.title
        address= u.marketerdetail.address
        credits=u.marketerdetail.credits
        flatnumber= request.POST['flatnumber']
        if flatnumber=="share":
            sh={}
            phonenumber=request.POST['phonenumber']
            sh["show"]=True
            sh["amount"]=((post1.product_price)*(100+int(phonenumber)))//100
            return render(request,"blog/single-product.html",{"post":post,"share":sh})
        print(username,flatnumber,product_name)
        name=request.POST["name"]
        if flatnumber=='self' and Orders.objects.filter(dealername=username).filter(productname=product_name).filter(flataddress="self").exists():
            messages.info(request,'Only one sample order allowed')
            return render(request,"blog/single-product.html",{"post":post})
        if name=="delar_name":
            name=post1.marketer
            quantity="1"
            phonenumber=post1.marketer_phonenumber
        else:
            quantity=request.POST["qty"]
            phonenumber=request.POST['phonenumber']
        order_details=Orders.objects.create(dealername=username,flataddress=flatnumber,phonenumber=phonenumber,buyername=name,quantity=quantity,apartmentaddress=address,productname=product_name)
        product_price=post1.product_price
        quantity = int(request.POST["qty"])
        if(credits>=quantity*product_price):
            order_details.save()
            #MarketerDetail.objects.filter(username=username).update(credits=(int)(credits-quantity*product_price))
            MarketerDetail.objects.filter(username__username=username).update(credits=credits - quantity*product_price)
            messages.info(request,'Order placed successfully')
            #print('order placed'+credits+" "+username+" "+product_price)
        else:
            messages.info(request, 'Order cancelled due to insufficient credits')
            print('order placement failed')
        return redirect("dashboard")
    sh={}
    sh["show"]=False
    sh["amount"]=0
    return render(request,"blog/single-product.html",{"post":post,"share":sh})
    return render(request,'blog/post_detail.html',{'post':post})
