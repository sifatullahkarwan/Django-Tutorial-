# Create your views here
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm# create HTML forms for us  contain username and password
from django.contrib import messages #import flash messagesn = easy weay to send one time alret message template
from django.contrib.auth.decorators import login_required# it requier decorator labray
from . forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm


def register(request):
    if request.method == 'POST':# post is http type request method
        form = UserRegisterForm(request.POST)# it let's to use UserRegisterForm and use POST backend http method
        if form.is_valid():# it is check if the form is fill valid when submited
            form.save()# it save the valid form
            username = form.cleaned_data.get('username')# it then cleand the data and get username in database
            messages.success(request,'Your account has been created ! and you can login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})# we can access form from this dictionary


# some flash messages

# messages.success
# messages.warning
# messages.error
# messages.info
@login_required 
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'you account hasbeent updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request , 'users/profile.html',context)