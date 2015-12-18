
__author__ = 'agupta330'
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from active_login_required import active_login_required
from django.shortcuts import get_object_or_404

@login_required()
def index(request):
    return render(request,'index.html')

@login_required()
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')    

# Login Functionality
def user_login(request):

    if request.method == 'POST':
        # Get the username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username,password
        # Authenticate user based on entered username and password
        user = authenticate(username=username, password=password)

        # Check if user exists in database
        if user:
            # Check whether user is active or not
            if user.is_active:

                # Check whether user exists in entity or not
                # if user exists in entity give the user
                # a Survey Admin Staff Status
                # Render to User Dashboard page and redirect to restricted1 view('/Survey/restricted1')
                login(request, user)

                return render(request,"index.html")

            else:
                return HttpResponse("Your Rango account is disabled.")

        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict = {'boldmessage': "Invalid Login details "}
            return render(request, 'login.html', context_dict)

    else:
        # Render the login page
        context_dict = {'boldmessage': "Login"}
        return render(request, 'login.html', context_dict)




