from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
def register(request):
    # if it is a POST request (a registration form is being submitted)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # if it passes validation:
        if form.is_valid():
            form.save()
            # automatically authenticate the new user after registration
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            # redirect to the homepage with a success message
            return HttpResponseRedirect('/?account=success')
    # if it is a GET request (a registration form is just being loaded)
    else:
        form = UserRegisterForm()
    # if it is a GET request or the form doesn't pass validation, then return the registration form page
    return render(request, 'users/register.html', {'form': form})


# adding more context to the default 'LoginView' class-based view
class LoginLogout(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'message': 'You have logged out!',
            'tag': 'success'
        })
        return context


# adding a custom logout function
def logout_view(request):
    # logging the user out
    logout(request)
    # calling the 'LoginLogout' that has updated context for the 'LoginView'
    return LoginLogout.as_view(template_name='users/login.html')(request)
class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
      template_name = 'users/password_reset_complete.html'