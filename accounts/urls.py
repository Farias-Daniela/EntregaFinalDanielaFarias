from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import reverse_lazy


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url=reverse_lazy('accounts:profile')
    ), name='change_password'),
]
