from django.shortcuts import render, redirect
from .forms import UserProfileForm

# Create your views here.
def signup_page(request):
    doc = '/static/media/doctor.png'
    donate = '/static/media/donate.png'
    icon = '/static/media/icon.svg'
    css = '/static/donate.css'
    js = '/static/donate.js'
    return render(request, "donate.html", {'doc':doc, 'donate':donate, 'icon':icon, 'css':css, 'js':js})

def signup_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('termsandconditions')
    else:
        form = UserProfileForm()
        return render(request, 'donate.html', {'form': form})
    
def display_tac(request):
    return render(request, 'TERMS_PAGE.html')

from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserModel

def login_view(request):
    users = UserModel.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']  # Use 'uname' to match your form field
            password = form.cleaned_data['password']    # Use 'pwd' to match your form field
            for user in users:
                if(username==user.email and password==user.Password):
                    #login(request, user)
                    #redirect("dashboard/donor/")
                    return render(request, 'dashboard.html')
    else:
        form = UserForm()
        return render(request, 'dashboard.html')