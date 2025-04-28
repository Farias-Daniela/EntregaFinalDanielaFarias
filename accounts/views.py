from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm, ProfileForm
from .models import Profile
from .forms import UserCreationFormCustom

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user)
        return response

def signup(request):
    if request.method == 'POST':
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('accounts:profile')
    else:
        form = UserCreationFormCustom()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': request.user.profile})

@login_required
def edit_profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('accounts:profile')

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
