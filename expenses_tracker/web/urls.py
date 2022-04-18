from django.urls import path

from expenses_tracker.web.views import show_home, create_expense, edit_expense, delete_expense, show_profile, \
    profile_edit, create_profile, delete_profile

urlpatterns = [
    path('', show_home, name='show home'),
    path('create/', create_expense, name='expense create'),
    path('edit/<int:pk>', edit_expense, name='expense edit'),
    path('delete/<int:pk>', delete_expense, name='expense delete'),
    path('profile/', show_profile, name='show profile page'),
    path('profile/edit/', profile_edit, name='profile edit page'),
    path('profile/delete/',delete_profile , name='profile delete page'),
    path('profile/create',create_profile, name='create profile' )

]




