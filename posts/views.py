from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import postBlog
from .forms import InputForms
from django.contrib.auth.decorators import login_required

# Create your views here.


# main page rendering
def home_page(request):
    return render(request,'index.html')

#sign-up page rendering

def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'SuccessFully Registered')
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form': form})

def signin_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            messages.success(request,'LoggedIn Successfully')
            return redirect('posts_page')
    else:
        form = AuthenticationForm()
    return render(request,'signin.html',{'form':form})

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'LoggedOut SuccessFully')
    return redirect('home_page')

def posts_page(request):
    return render(request,'posts.html')


def view_post_page(request):
    post_details = postBlog.objects.order_by('-date')
    return render(request,'viewpost.html',{'post_details':post_details})

def using_slug(request,slug):
    post_detail = postBlog.objects.get(slug = slug)
    return render(request,'posttable.html',{'post_detail':post_detail})


@login_required(login_url='/signin')
def add_post(request):
    if request.method == 'POST':
        form = InputForms(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.name = request.user
            new_post.save()
            messages.success(request,'Post Added Successfully')
            return redirect('viewpost')
    else:
        form = InputForms()
    return render(request, 'addpost.html',{'form':form})

def about_page(request):
    return render(request,'about.html')

@login_required(login_url='/signin')
def update_post(request, id):
    post = get_object_or_404(postBlog, id=id)
    if request.user != post.name:
        return redirect('viewpost')
    if request.method == 'POST':
        forms = InputForms(request.POST, request.FILES, instance=post)
        if forms.is_valid():
            forms.save()
            return redirect('viewpost')
    else:
        forms = InputForms(instance=post)
    return render(request, 'edit.html', {'form': forms, 'post_detail': post})



@login_required(login_url='/signin')
def delete_post(request, id):
    post = get_object_or_404(postBlog, id=id)
    if request.user == post.name or request.user.is_superuser:
        if request.method == 'POST':
            post.delete()
            return redirect('viewpost')
    else:
        return redirect('viewpost')
    return render(request, 'posttable.html', {'post': post})



    
    
    