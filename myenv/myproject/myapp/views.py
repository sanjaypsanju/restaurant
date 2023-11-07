from django.shortcuts import render
from.models import Register,Login
from.forms import RegisterForm,LoginForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'login.html')
    else:
        form = RegisterForm()
    return render(request,'register.html')
def login(request):
    if request.method == "POST":
        username = form['username'].valid()
        password = form['password'].valid()
        try:
            user=Login.object.get(username=username,passwords=password)
            if user is not None:
                return render (request,'home.html')
        except:
            pass
    else:
        return render(request,'login.html')