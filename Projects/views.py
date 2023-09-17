from django.shortcuts import render

def LandingPage(request):
    return render(request, "Login\\templates\\hello.html")