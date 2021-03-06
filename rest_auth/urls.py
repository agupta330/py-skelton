from django.conf.urls import patterns, url
from rest_auth import views
from axes.decorators import watch_login

from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView,LockUserView,UnlockUserView
)

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
    url(r'^handlecsv/$',views.handlecsv,name='handlecsv'),
    url(r'^rest_lock/$', LockUserView.as_view(), name='rest_lock'),
    url(r'^rest_unlock/$', UnlockUserView.as_view(), name='rest_unlock'),
]