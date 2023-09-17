from django.shortcuts import render, redirect
from .forms import UserForm
from .models import UserModel

def login_view(request):
    users = UserModel.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uname']  # Use 'uname' to match your form field
            password = form.cleaned_data['pwd']    # Use 'pwd' to match your form field
            for user in users:
                if(username==user.Username and password==user.Password):
                    #login(request, user)
                    return render(request, 'hello.html')
    else:
        form = UserForm()
    return render(request, 'hello.html')

def login_page(request):
    return render(request, 'index.html')