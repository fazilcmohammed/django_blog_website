from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from blogpost.models import Post
# Create your views here.
def signup(request):
    user = None
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_psd = request.POST['confirmpassword']

        if password != confirm_psd:
            messages.error(request, 'Password does not match')
            return redirect('signup')

        user = User.objects.create_user(username=email, first_name=firstname, last_name=lastname, password=password)
        user.save()

        return redirect('signin')
    return render(request, 'signup.html', {'user' : user})

def signin(request):
    error_msg = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_msg = 'Invalid credentials'


    return render(request, 'signin.html', {'error_msg': error_msg})

def signout(request):
    logout(request)
    return redirect('home')

def profile(request):
    # Fetch the User object
    return render(request, 'my_profile.html')

def my_posts(request):
    if request.user.is_authenticated:
        # Fetch posts created by the logged-in user
        posts = Post.objects.filter(author=request.user, delete_status=Post.LIVE).order_by('-created_at')

        # Debugging: Print posts to console
        print("Posts for user:", request.user.username, posts)
        
        return render(request, 'my_profile.html', {'posts': posts})
    else:
        return redirect('signin')  # Redirect to login if user is not authenticated


# def editprofile(request, id):
#     # Fetch the User object using the username
#     user_obj = get_object_or_404(User, id=id)
#     # Fetch the Profile object related to the User
#     edit_profile = Profile.objects.get(user = user_obj)
#     if request.method == 'POST':
#         updated_profile_photo = request.POST['profile_picture']
#         edit_profile.profile_picture = updated_profile_photo
#         updated_bio = request.POST['bio']
#         edit_profile.bio = updated_bio
#         edit_profile.save()
#         return redirect('profile', user=user_obj.username)
    
#     return render(request, 'edit_profile.html', {'edit_profile': edit_profile})