"""apartket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls import url
from django.shortcuts import redirect
from django.contrib import admin
from django.conf import settings
from blog import views as views1
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from apartapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('home',views.home,name='home'),
    # path('register',views.register,name='register'),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout"),
    path("credits",views.credits,name="credits"),
    path("refer-and-earn",views.referandearn,name="refer-and-earn"),
    #path("earn-credits",views.earncredits, name="earn_credits"),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='blog/change-password.html'),
    ),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="blog/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="blog/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="blog/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="blog/password_reset_done.html"),name="password_reset_complete"),
    # path("addproduct",views1.addProduct,name="productadd"),
    # path('accounts/login/',lambda request: redirect('/login', permanent=False)),

    # path('accounts/password_change/',name='password_change'),
    path("dashboard",views1.dashboard, name="dashboard"),
    path("earn_credits",views1.earncredits, name="earn_credits"),
    path("addproduct",views1.addproduct, name="addproduct"),
    path("registermarketer",views1.registermarketer, name="registermarketer"),
    path("registermanufacturer",views1.registermanufacturer, name="registermanufacturer"),
    url(r'^$', views1.post_list_view),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views1.post_detail_view,name='post_detail'),
    path('password_change_done',lambda request: redirect('/', permanent=False),name="password_change_done"),
    # path('accounts/', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
