from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from blog.forms import PostForm,CommentForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . models import Post


# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('posts')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('username does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
            print('Username or password is incorrect')
    return render(request, 'registration/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def posts(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html',{'post':post})

def post(request,pk):
    postObject = Post.objects.get(id=pk)
    return render(request, 'blog/post_single.html',{'postObject':postObject})

def about(request):
    return render(request, 'blog/about.html')

@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form':form}
    return render(request, 'blog/post_form.html',context)


@login_required(login_url='login')
def update_post(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form':form}
    return render(request, 'blog/post_form.html',context)

@login_required(login_url='login')
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'object':post}
    return render(request, 'blog\delete_object.html',context)


@login_required(login_url='login')
def draft(request):
    post = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/draft_list.html',{'post':post})

@login_required(login_url='login')
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('posts')


@login_required(login_url='login')
def add_comment(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post =  post
            comment.save()
            return redirect('post',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html',{"form":form})



@login_required(login_url='login')
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post',pk=comment.post.pk)

@login_required(login_url='login')
def comment_remove(request,pk):
    comment =get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post',pk=comment.post_pk)