from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required(login_url='signIn')
def home(request):
    user_profile =  Profile.objects.get(user=request.user)
    posts = Post.objects.all()
    return render(request, 'home/index.html',locals())
@login_required(login_url='signIn')
def profile(request):
    user_profile =  Profile.objects.get(user=request.user)
    return render(request, 'settings/profile.html',locals())
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')

@login_required(login_url='signIn')
def upload(request):
    if request.method == "POST":
        user = request.user.username
        image = request.FILES.get('upload_file')
        caption = request.POST['caption']
        
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')
@login_required(login_url='signIn')
def settings(request):
    edit_profile =  Profile.objects.get(user=request.user)
    if request.method =="POST":
        if request.FILES.get('image','cover') == None:
            profile_image = edit_profile.profile_image
            profile_cove = edit_profile.profile_cove
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email = request.POST.get('email')
            user_about = request.POST.get('about')
            location = request.POST.get('location')
            bio = request.POST.get('bio')
            working = request.POST.get('working')
            relationship = request.POST.get('relationship')
            
            edit_profile.profile_image = profile_image
            edit_profile.profile_cove = profile_cove
            edit_profile.user.first_name = first_name
            edit_profile.user.last_name = last_name
            edit_profile.user.email = email
            edit_profile.user_about = user_about
            edit_profile.location = location
            edit_profile.bio = bio
            edit_profile.working = working
            edit_profile.relationship = relationship
            edit_profile.save()
            return redirect('profile')
        else:
            profile_image = request.FILES.get('image')
            profile_cove = request.FILES.get('cover')
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            email = request.POST.get('email')
            user_about = request.POST.get('about')
            location = request.POST.get('location')
            bio = request.POST.get('bio')
            working = request.POST.get('working')
            relationship = request.POST.get('relationship')
            
            edit_profile.profile_image = profile_image
            edit_profile.profile_cove = profile_cove
            edit_profile.user.first_name = first_name
            edit_profile.user.last_name = last_name
            edit_profile.user.email = email
            edit_profile.user_about = user_about
            edit_profile.location = location
            edit_profile.bio = bio
            edit_profile.working = working
            edit_profile.relationship = relationship
            edit_profile.save()
            return redirect('profile')
    else:
        return render(request, 'settings/setting.html', locals())
def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signIn')
    else:
        return render(request, 'settings/signin.html')
def signUp(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['confirm_password']
        
        # password validator
        SpecialSym =['$', '@', '&', '!', '^', '*', '~' '#', '%']
        if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username Taken')
                return redirect('signup')
        elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Taken')
                return redirect('signup')
        elif password and password1 is None:
            messages.warning(request, 'Password cannot be empty')
            return redirect('signup')
        elif password != password1:
            messages.warning(request, 'Passwords not match!')
            return redirect('signup')
        elif len(password) < 6:
            messages.warning(request, 'Passwords less then 6 character')
            return redirect('signup')
        elif not any(char.isdigit() for char in password):
            messages.warning(request, 'Password should have at least one numeral')
            return redirect('signup')
        elif not any(char.isupper() for char in password):
            messages.warning(request, 'Password should have at least one uppercase letter')
            return redirect('signup')
        elif not any(char.islower() for char in password):
            messages.warning(request, 'Password should have at least one lowercase letter')
            return redirect('signup')
        elif not any(char in SpecialSym for char in password):
            messages.warning(request, 'Password should have at least one of the symbols $@#')
            return redirect('signup')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            
            #log user in and redirect to settings page
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)
            
            #create a Profile object for the new user
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('settings')
    else:
        return render(request, 'settings/signup.html')
    
@login_required(login_url='signIn')
def logout(request):
    auth.logout(request)
    return redirect('signIn')