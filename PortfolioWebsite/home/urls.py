from django.urls import path
from home import views
urlpatterns = [
    path('', views.home,name="home"),
    path('myclick', views.myClick,name="myclick"),
    path('project', views.project,name="project"),
    path('contact', views.contact,name="contact"),
    path('login', views.loginPage,name="login"),
    path('logout', views.logoutPage,name="logout"),
    path('logged', views.logged,name="logged"),
    path('logged/loggedsettings', views.loggedsettings,name="loggedsettings"),
    path('logged/passwordchange', views.passwordChange,name="passwordchange"),
    path('signup', views.signupPage,name="signup"),
    path('myphoto', views.myphoto,name="myphoto"),
    path('myclick', views.myClick,name="myclick"),
    path('logged/purchase', views.purchase,name="purchase"),
]