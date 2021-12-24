
from django.urls import path,include
from. import views

urlpatterns = [

    path('',views.signup,name="signup"),
    path('handlesignup/', views.handlesignup, name="handlesignup"),
]
