from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(requests):
    return render(requests, "home.html")


def handlesignup(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("/signup")
            except User.DoesNotExist:
                if len(uname) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("/signup")
                if not uname.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("/signup")
                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("/signup")
